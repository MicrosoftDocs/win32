---
title: Create Keywords for a Binary Index
description: A binary index is automatically generated whenever you compile an index into a compiled help (.chm) file. You can create keywords either by adding them to the index file or as Keyword links (KLinks) that are added to target files.
ms.assetid: 29669B4F-E200-4557-A7E9-0E3245B443A3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create Keywords for a Binary Index

A binary index is automatically generated whenever you compile an index into a compiled help (.chm) file. You can create keywords either by [adding them to the index file](to-add-a-keyword-to-an-index-file.md) or as [Keyword links (KLinks)](to-add-a-klink-keyword-to-an-html-file.md) that are added to target files.

Keywords in the index will be merged with any that you have added to HTML files when the index is compiled. If you are merging indexes from multiple compiled help files, be sure to consider how to [manage the index files](managing-merged-index-files.md) in the collection.

## Notes

-   Binary indexes are automatically sorted by the compiler.
-   A binary index will not be created if you select "1.0" as the version in the **Compatibility** box, on the **Compiler** tab, in the **Project Options** dialog box, or if the **Create a binary index** check box is cleared.

## What do you want to do?

-   [Create a keyword with multiple targets](creating-a-keyword-with-multiple-targets.md)
-   [To set an index keyword to jump to another keyword](to-set-an-index-keyword-to-jump-to-another-keyword.md)
-   [Create a binary index](creating-an-index-file.md)
-   [Learn about the difference between binary and site map indexes](the-difference-between-binary-and-site-map-indexes.md)

## Related topics

<dl> <dt>

[About Creating Index Files](create-an-index-file.md)
</dt> </dl>

 

 




