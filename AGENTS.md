# Win32 documentation agent instructions

This repository contains the conceptual Win32 documentation published under [learn.microsoft.com/windows/win32](https://learn.microsoft.com/windows/win32/). Content is stored under `desktop-src/`.

## Check for existing content before adding a topic

Before you create a conceptual article or add substantial standalone guidance, search the generated content catalog:

```console
python tools/content_index/content_index.py search "describe the proposed topic"
```

Review the closest matches and prefer, in this order:

1. Update an existing canonical article if it serves the same audience and scenario.
2. Add the missing information to an existing article and link to it from related pages.
3. Create a new article only when existing coverage has a materially different audience, technology, version, programming language, or reader goal.

For a new topic, also search the available catalogs from `MicrosoftDocs/windows-dev-docs-pr`, `MicrosoftDocs/windows-driver-docs-pr`, and `MicrosoftDocs/windows-ai-docs-pr`. Pass each downloaded or locally checked-out catalog with an additional `--index` argument as described in `tools/content_index/README.md`.

When you create a topic, include the catalog search terms and the reason existing pages do not meet the reader need in the pull request description. Do not copy explanations or procedures into multiple articles when a link to canonical coverage is sufficient.

After you change conceptual Markdown, regenerate the catalog and commit the result:

```console
python tools/content_index/content_index.py build
```

Use `python tools/content_index/content_index.py audit` to produce likely duplicate pairs for human review. Similarity is not proof of duplication; account for audience, technology, language, version, and lifecycle differences before consolidating content.

The conceptual catalog intentionally excludes API and language-reference pages. Do not replace required CLSIDs, IIDs, GUIDs, schema identifiers, or other public platform identifiers with synthetic values.
