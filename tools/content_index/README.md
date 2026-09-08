# Conceptual content index

The conceptual content index helps authors and agents find existing coverage before they create or substantially duplicate a topic. It includes current and legacy content so migration work can identify overlap.

## Build and check the index

```console
python tools/content_index/content_index.py build
python tools/content_index/content_index.py check
```

The build reads `.github/content-index-config.json` and writes the deterministic `.github/content-index.jsonl` catalog. Commit the updated catalog with conceptual content changes.

## Search before creating content

```console
python tools/content_index/content_index.py search "manage windows with AppWindow"
```

Search results include current and legacy topics. Review the closest matches before deciding to create a page. Prefer updating an existing canonical page or linking to it when that meets the reader need.

To search catalogs aggregated from other repositories, repeat `--index`:

```console
python tools/content_index/content_index.py search "package an unpackaged app" \
  --index .github/content-index.jsonl \
  --index ../win32-pr/.github/content-index.jsonl
```

The Windows developer conceptual catalog set consists of:

- `MicrosoftDocs/windows-dev-docs-pr`
- `MicrosoftDocs/win32-pr`
- `MicrosoftDocs/windows-driver-docs-pr`
- `MicrosoftDocs/windows-ai-docs-pr`

When the repositories or downloaded catalogs are available, include all four indexes before deciding that a topic has no existing coverage.

## Audit likely duplication

```console
python tools/content_index/content_index.py audit --threshold 0.72 --limit 100
```

The audit generates candidates for human review. By default, it excludes pages with fewer than 50 normalized words so navigation and stub pages don't obscure substantive overlap. Use `--min-words` to adjust that threshold. Similarity does not prove that two topics should be combined; product, audience, language, version, and lifecycle differences can justify separate coverage.
