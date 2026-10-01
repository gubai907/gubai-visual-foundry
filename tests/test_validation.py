#!/usr/bin/env python3
"""Exercise release validation failures using isolated, anonymous fixtures."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidationBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skill-validation-')
        self.addCleanup(self.temp.cleanup)
        self.sandbox = Path(self.temp.name)
        self.root = self.sandbox / 'skill'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.term = 'AnonymousConfidentialFixture'
        self.terms = self.sandbox / 'terms.txt'
        self.terms.write_text(self.term + '\n', encoding='utf-8')

    def run_script(self, script='validate_skill.py', *args):
        result = subprocess.run(
            [sys.executable, str(self.root / 'scripts' / script), *args],
            capture_output=True, text=True,
            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
        )
        self.assertNotIn('Traceback', result.stderr)
        self.assertNotIn(self.term, result.stdout + result.stderr)
        return result

    def assert_rejected(self, message):
        result = self.run_script('validate_skill.py', '--private-terms-file', str(self.terms))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)

    def test_complete_package(self):
        self.assertEqual(self.run_script().returncode, 0)

    def test_missing_entrypoint(self):
        (self.root / 'SKILL.md').unlink()
        self.assert_rejected('missing or empty: SKILL.md')

    def test_empty_required_file(self):
        (self.root / 'qa/quality-gate.md').write_text('')
        self.assert_rejected('missing or empty: qa/quality-gate.md')

    def test_private_term_in_json(self):
        (self.root / 'examples/probe.json').write_text(json.dumps({'value': self.term}))
        self.assert_rejected('confidential term found in content')

    def test_private_term_in_filename(self):
        (self.root / 'examples' / (self.term + '.md')).write_text('Example')
        self.assert_rejected('confidential term found in filename')

    def test_private_term_in_gitignore(self):
        with (self.root / '.gitignore').open('a') as stream:
            stream.write(self.term)
        self.assert_rejected('confidential term found in content')

    def test_private_term_in_license(self):
        (self.root / 'LICENSE').write_text(self.term)
        self.assert_rejected('confidential term found in content')

    def test_terms_file_inside_package(self):
        path = self.root / 'terms.json'
        path.write_text('[]')
        result = self.run_script('validate_skill.py', '--private-terms-file', str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn('must be outside', result.stdout)

    def test_symlink_to_external_file(self):
        outside = self.sandbox / 'outside.md'
        outside.write_text(self.term)
        (self.root / 'SKILL.md').unlink()
        (self.root / 'SKILL.md').symlink_to(outside)
        self.assert_rejected('symlink not allowed')

    def test_private_directory(self):
        (self.root / 'private').mkdir()
        self.assert_rejected('excluded release entry')

    def test_hidden_directory(self):
        (self.root / '.cache').mkdir()
        self.assert_rejected('unexpected hidden entry')

    def test_repository_metadata_allowed(self):
        metadata = self.root / '.git'
        metadata.mkdir()
        (metadata / 'config').write_text('local state')
        self.assertEqual(self.run_script().returncode, 0)

    def test_binary_json(self):
        (self.root / 'examples/binary.json').write_bytes(bytes([255, 254]))
        self.assert_rejected('cannot be read as UTF-8')

    def test_unsupported_file(self):
        (self.root / 'examples/asset.png').write_bytes(b'fixture')
        self.assert_rejected('unsupported release file')

    def test_credential_detection(self):
        value = 'gh' + 'p_' + 'A' * 32
        (self.root / 'examples/probe.json').write_text(json.dumps({'value': value}))
        self.assert_rejected('possible credential found')

    def test_local_account_path_detection(self):
        value = '/' + 'Users/' + 'anonymous/project'
        (self.root / 'examples/probe.json').write_text(json.dumps({'value': value}))
        self.assert_rejected('local account path found')

    def test_regression_missing_source_with_report(self):
        (self.root / 'core/task-router.md').unlink()
        result = self.run_script('run_prompt_regression.py', '--write-report')
        self.assertEqual(result.returncode, 1)
        self.assertIn('source missing', result.stdout)
        self.assertIn('FAIL', (self.root / 'tests/prompt-only-regression.md').read_text())

    def test_regression_malformed_inventory(self):
        (self.root / 'tests/prompt-only-fixtures.json').write_text('[]')
        result = self.run_script('run_prompt_regression.py')
        self.assertEqual(result.returncode, 1)
        self.assertIn('malformed', result.stdout)


if __name__ == '__main__':
    unittest.main()
