import json
import tempfile
import unittest
from pathlib import Path

from tools.content_index import content_index


class ContentIndexTests(unittest.TestCase):
    def test_build_search_and_exact_duplicate_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".github").mkdir()
            (root / "current").mkdir()
            (root / "legacy").mkdir()
            config = {
                "schema_version": 1,
                "repository": "example/docs",
                "index_path": ".github/index.jsonl",
                "docsets": [
                    {
                        "name": "current",
                        "root": "current",
                        "url_prefix": "https://learn.microsoft.com/current",
                        "status": "current",
                    },
                    {
                        "name": "legacy",
                        "root": "legacy",
                        "url_prefix": "https://learn.microsoft.com/legacy",
                        "status": "legacy",
                    },
                ],
                "exclude_path_parts": ["includes"],
                "exclude_filenames": ["README.md"],
                "exclude_topics": ["include"],
                "exclude_metadata_keys": ["api_name", "topic_type"],
                "exclude_generated_api_reference": True,
                "max_terms": 20,
            }
            (root / ".github/config.json").write_text(json.dumps(config))
            article = """---
title: Manage app windows
description: Use window management APIs to position an app window.
ms.topic: how-to
---
# Manage app windows

Use the window management APIs to position and resize an app window.
"""
            (root / "current/windows.md").write_text(article)
            (root / "legacy/windows.md").write_text(article)
            (root / "current/includes").mkdir()
            (root / "current/includes/ignored.md").write_text(article)

            loaded = content_index.load_config(root, ".github/config.json")
            records = content_index.build_records(root, loaded)

            self.assertEqual(2, len(records))
            self.assertEqual(
                "https://learn.microsoft.com/current/windows", records[0]["url"]
            )
            self.assertEqual(
                "Manage app windows",
                content_index.search(records, "app window management", 1)[0][1]["title"],
            )
            findings = content_index.audit(
                records, threshold=0.9, limit=10, min_words=0
            )
            self.assertEqual(1, len(findings))
            self.assertEqual("identical normalized content", findings[0]["reason"])

    def test_generated_api_reference_is_excluded(self):
        metadata = {"ms.topic": "reference"}
        body = """# Widget.Run Method

## Definition

Namespace: Example.Tools

## Parameters
"""
        self.assertTrue(content_index.generated_api_reference(metadata, body))

    def test_api_metadata_is_excluded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            article = """---
title: Widget API
ms.topic: article
api_name:
- Widget
---
# Widget API
"""
            path = root / "docs/widget.md"
            path.write_text(article)
            config = {
                "schema_version": 1,
                "repository": "example/docs",
                "exclude_topics": [],
                "exclude_metadata_keys": ["api_name"],
                "exclude_generated_api_reference": True,
                "max_terms": 20,
            }
            docset = {
                "name": "docs",
                "root": "docs",
                "url_prefix": "https://learn.microsoft.com/docs",
                "status": "current",
            }
            self.assertIsNone(
                content_index.record_for_file(root, docset, path, config)
            )

    def test_headings_ignore_fenced_code(self):
        body = """# Real heading

```powershell
# This is a command comment
```

## Another real heading
"""
        self.assertEqual(
            ["Real heading", "Another real heading"],
            content_index.extract_headings(body),
        )

    def test_path_tokens_split_slug_components(self):
        record = {"path": "hub/apps/develop/manage-app-windows.md"}
        self.assertTrue(
            {"manage", "app", "window"}
            <= content_index.field_tokens(record, "path")
        )

    def test_index_page_uses_directory_url(self):
        self.assertEqual(
            "https://learn.microsoft.com/windows/apps/develop",
            content_index.published_url(
                "https://learn.microsoft.com/windows",
                Path("apps/develop/index.md"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
