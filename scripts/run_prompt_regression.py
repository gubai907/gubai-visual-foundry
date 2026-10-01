#!/usr/bin/env python3
"""Run deterministic prompt-contract traces for media-free regression cases."""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "prompt-only-fixtures.json"
REPORT = ROOT / "tests" / "prompt-only-regression.md"


def joined(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def source_hash(paths: set[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(str(path.relative_to(ROOT)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes() if path.is_file() else b"<missing>")
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--report-date", type=date.fromisoformat, default=None, help="Optional YYYY-MM-DD for reproducible reports")
    args = parser.parse_args()

    try:
        data = json.loads(FIXTURES.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("cases"), list) or not data["cases"] or not isinstance(data.get("version"), str):
            raise ValueError("invalid fixture inventory")
        for case in data["cases"]:
            if not isinstance(case, dict) or not all(key in case for key in ("id", "title", "actual")):
                raise ValueError("incomplete fixture case")
            for key in ("must_contain", "must_not_contain"):
                if not isinstance(case.get(key, []), list) or not all(isinstance(t, str) for t in case.get(key, [])):
                    raise ValueError("invalid assertion list")
            if not isinstance(case.get("source_checks", []), list):
                raise ValueError("invalid source check list")
            for check in case.get("source_checks", []):
                if not isinstance(check, dict) or not isinstance(check.get("path"), str):
                    raise ValueError("invalid source check")
                if not isinstance(check.get("contains", []), list) or not all(isinstance(t, str) for t in check.get("contains", [])):
                    raise ValueError("invalid source assertion")
                source_path = ROOT / check["path"]
                if source_path.is_symlink() or ROOT not in source_path.resolve().parents:
                    raise ValueError("source check must remain inside the package")
    except (OSError, UnicodeError, ValueError):
        print("FAIL: fixture file is missing, unreadable or malformed")
        return 1
    failures: list[str] = []
    rows: list[tuple[str, str, str]] = []
    checked_sources: set[Path] = {FIXTURES}

    for case in data["cases"]:
        actual = joined(case["actual"])
        case_failures: list[str] = []

        for token in case.get("must_contain", []):
            if token not in actual:
                case_failures.append(f"actual missing {token!r}")
        for token in case.get("must_not_contain", []):
            if token in actual:
                case_failures.append(f"actual contains forbidden {token!r}")

        for check in case.get("source_checks", []):
            path = ROOT / check["path"]
            checked_sources.add(path)
            if not path.is_file():
                case_failures.append(f"source missing: {check['path']}")
                continue
            source = path.read_text(encoding="utf-8")
            for token in check.get("contains", []):
                if token not in source:
                    case_failures.append(f"{check['path']} missing {token!r}")

        status = "PASS" if not case_failures else "FAIL"
        evidence = "all output and source assertions matched" if not case_failures else "; ".join(case_failures)
        rows.append((case["id"], case["title"], status))
        failures.extend(f"{case['id']}: {item}" for item in case_failures)
        print(f"{status} {case['id']} {case['title']}: {evidence}")

    if args.write_report:
        digest = source_hash(checked_sources)
        lines = [
            "# Prompt-only Deterministic Regression",
            "",
            f"版本：{data['version']}；执行日期：{args.report_date or date.today()}。",
            "",
            "## 方法与边界",
            "",
            "本记录执行的是可重复的规则合同追踪：为每个无媒体案例固定实际路由、编译结果或冲突决策，逐条断言必须保留、必须排除的内容，并核对对应运行规则仍存在。它验证规则与编译样例的一致性，不是独立模型行为测试、平台实测或真实生图验收。",
            "",
            f"规则与夹具源哈希（SHA-256）：`{digest}`。",
            "",
            "## 结果",
            "",
            "| ID | 案例 | 结果 |",
            "|---|---|---|",
        ]
        lines.extend(f"| {case_id} | {title} | {status} |" for case_id, title, status in rows)
        lines.extend([
            "",
            f"合计：{sum(status == 'PASS' for _, _, status in rows)}/{len(rows)} PASS。",
            "",
            "## 实际追踪产物",
            "",
        ])
        for case in data["cases"]:
            lines.extend([
                f"### {case['id']} — {case['title']}",
                "",
                "```json",
                json.dumps(case["actual"], ensure_ascii=False, indent=2),
                "```",
                "",
                "断言：必须包含 " + "、".join(f"`{item}`" for item in case.get("must_contain", [])) + "。",
                "",
                "禁止包含 " + "、".join(f"`{item}`" for item in case.get("must_not_contain", [])) + "。",
                "",
            ])
        lines.extend([
            "## 未运行",
            "",
            "真实图片生成、平台能力、像素区域比对、失败图九维评分与独立模型遵循性均未运行；这些项目需要相应媒体夹具、平台和明确生成测试任务。",
            "",
        ])
        REPORT.write_text("\n".join(lines), encoding="utf-8")

    if failures:
        print("\nFAIL")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print(f"\nPASS: {len(rows)}/{len(rows)} deterministic prompt-contract cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
