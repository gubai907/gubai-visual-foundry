#!/usr/bin/env python3
"""Validate the V2 skill package without third-party dependencies."""

from pathlib import Path
import argparse
import json
import os
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
VERSION = "2.0.0-public.5"

REQUIRED = [
    "SKILL.md",
    "agents/openai.yaml",
    "core/task-router.md",
    "core/reference-role-matrix.md",
    "core/prompt-compiler.md",
    "locks/product-lock.md",
    "locks/prop-lock.md",
    "modules/fashion.md",
    "modules/refine-upscale.md",
    "platforms/tapnow.md",
    "platforms/jimeng.md",
    "profiles/user-defaults.md",
    "profiles/profile-schema.md",
    "examples/brand-profile-example.md",
    "qa/quality-gate.md",
    "qa/single-variable-repair.md",
    "tests/regression-cases.md",
    "tests/prompt-only-fixtures.json",
    "tests/prompt-only-regression.md",
    "scripts/run_prompt_regression.py",
]

REFERENCE_ROLES = [
    "Face Reference",
    "Full Body Reference",
    "Style Reference",
    "Product Reference",
    "Prop Reference",
    "Environment Reference",
]

QA_DIMENSIONS = [
    "Identity",
    "Body Proportion",
    "Wardrobe",
    "Product / Prop",
    "Hands / Anatomy",
    "Expression / Gaze",
    "Composition",
    "Lighting",
    "Material",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--private-terms-file', type=Path, help='Optional external file: one confidential term per line')
    args = parser.parse_args()
    errors: list[str] = []
    private_terms: list[str] = []
    if args.private_terms_file:
        term_path = args.private_terms_file.resolve()
        if term_path == ROOT or ROOT in term_path.parents:
            errors.append('private terms file must be outside the public package')
        else:
            try:
                private_terms = [s.strip() for s in term_path.read_text(encoding='utf-8').splitlines() if s.strip()]
            except (OSError, UnicodeError):
                errors.append('private terms file cannot be read as UTF-8')

    def display(rel: str) -> str:
        for term in private_terms:
            rel = re.sub(re.escape(term), '[redacted]', rel, flags=re.I)
        return rel

    def fail() -> int:
        print('FAIL')
        print('\n'.join('- ' + item for item in errors))
        return 1

    # Walk without following links. Git metadata is local repository state;
    # release archives must exclude it separately.
    texts: dict[str, str] = {}
    for directory, dirs, files in os.walk(ROOT, followlinks=False):
        for name in list(dirs) + files:
            path = Path(directory) / name
            rel = path.relative_to(ROOT).as_posix()
            label = display(rel)
            if any(term.casefold() in rel.casefold() for term in private_terms):
                errors.append(f'confidential term found in filename: {label}')
            if path.is_symlink():
                errors.append(f'symlink not allowed: {label}')
                if name in dirs:
                    dirs.remove(name)
                continue
            if name == '.git':
                if name in dirs:
                    dirs.remove(name)
                continue
            if name.startswith('.') and rel != '.gitignore':
                errors.append(f'unexpected hidden entry: {label}')
            if name in {'private', 'local', 'evidence', 'project-profiles', 'backups', '__pycache__', '__MACOSX'}:
                errors.append(f'excluded release entry: {label}')
                if name in dirs:
                    dirs.remove(name)
                continue
            if name in dirs:
                continue
            if path.suffix not in {'.md', '.py', '.yaml', '.json'} and rel not in {'.gitignore', 'LICENSE', 'NOTICE'}:
                errors.append(f'unsupported release file: {label}')
                continue
            try:
                value = path.read_text(encoding='utf-8')
            except (OSError, UnicodeError):
                errors.append(f'file cannot be read as UTF-8: {label}')
                continue
            texts[rel] = value
            if any(term.casefold() in value.casefold() for term in private_terms):
                errors.append(f'confidential term found in content: {label}')
            if re.search(r'/(?:Users|home)/[^\s]+|[A-Za-z]:\\Users\\[^\s]+', value):
                errors.append(f'local account path found: {label}')
            credential_patterns = [
                r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b',
                r'''(?i)(?:api[_-]?key|password|secret|access[_-]?token)\s*[:=]\s*["'][^"']{6,}["']''',
            ]
            if any(re.search(pattern, value) for pattern in credential_patterns):
                errors.append(f'possible credential found: {label}')

    for rel in REQUIRED:
        if not texts.get(rel, '').strip():
            errors.append(f'missing or empty: {rel}')
    # Do not read incomplete packages or rejected links during deeper checks.
    if errors:
        return fail()

    skill = texts['SKILL.md']
    if f'版本 {VERSION}' not in skill:
        errors.append('SKILL.md version mismatch')
    match = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
    if not match:
        errors.append('SKILL.md frontmatter is missing or malformed')
    else:
        frontmatter = match.group(1)
        if not re.search(r'^name: gubai-visual-foundry$', frontmatter, re.M):
            errors.append('unexpected skill name')
        if not re.search(r'^description: .+', frontmatter, re.M):
            errors.append('description is missing')

    for rel, value in texts.items():
        if not rel.endswith('.md'):
            continue
        if len(re.findall(r'^```', value, re.M)) % 2:
            errors.append(f'unbalanced code fence: {display(rel)}')
        for target in re.findall(r'\]\(([^)]+)\)', value):
            if '://' in target or target.startswith('#'):
                continue
            clean = target.split('#', 1)[0]
            resolved = (ROOT / rel).parent.joinpath(clean).resolve()
            if clean and (ROOT not in resolved.parents or not resolved.is_file()):
                errors.append(f'broken or external local link: {display(rel)}')

    matrix = texts['core/reference-role-matrix.md']
    for role in REFERENCE_ROLES:
        if role not in matrix:
            errors.append(f'reference role missing: {role}')
    for dimension in QA_DIMENSIONS:
        if dimension not in texts['qa/quality-gate.md']:
            errors.append(f'QA dimension missing: {dimension}')
    if len(re.findall(r'^\| R\d{2} \|', texts['tests/regression-cases.md'], re.M)) < 30:
        errors.append('fewer than 30 regression cases')
    try:
        data = json.loads(texts['tests/prompt-only-fixtures.json'])
        if not isinstance(data, dict):
            raise ValueError('fixture root must be an object')
        if data.get('version') != VERSION:
            errors.append('prompt-only fixture version mismatch')
        if not isinstance(data.get('cases'), list) or len(data['cases']) < 12:
            errors.append('fewer than 12 deterministic prompt-only cases')
    except ValueError:
        errors.append('invalid prompt-only fixture JSON or schema')
    if errors:
        return fail()
    print('PASS: V2 structure, links, reference roles, QA, regression inventory and release privacy checks')
    return 0


if __name__ == '__main__':
    sys.exit(main())
