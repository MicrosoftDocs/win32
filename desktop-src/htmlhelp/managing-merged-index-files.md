---
title: Managing Merged Index Files
description: Managing Merged Index Files
ms.assetid: 55A71903-7D3D-44fb-B1C1-CAF940B16957
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Merged Index Files

Merging index (.hhk) files from [multiple compiled help (.chm) files](merging-help-files-at-run-time.md) requires some management of each index. Consider the following when creating the index files for each compiled help file in the collection:

-   Index authors for each compiled help file should use similar indexing guidelines to avoid unwanted repetition of similar index entries.
-   [Keyword links (KLinks)](working-with-klinks.md) and [Associative links (ALinks)](working-with-alinks.md) should be standardized for all the index files in the collection.
-   Abbreviations should be standardized for all the index files being merged.
-   [site map](the-difference-between-binary-and-site-map-indexes.md) index files cannot be merged with binary index files.
-   If used, [information types](assign-information-types.md) should be standardized for all the index files in the collection.
-   Merged indexes are created at run time and any edits or customization to individual index files will be lost when the merged index is resorted.

## Related topics

<dl> <dt>

[About Managing Large Document Sets](manage-large-document-sets.md)
</dt> </dl>

 

 




