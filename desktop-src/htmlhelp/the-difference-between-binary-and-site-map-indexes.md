---
title: The Difference Between Binary and Site Map Indexes
description: There are two types of indexes available for help authors to use, a binary index or a site map index. Each type of index has its own unique features.
ms.assetid: 'B5489B75-E4B9-44f4-9F16-9495C5825F56'
---

# The Difference Between Binary and Site Map Indexes

There are two types of indexes available for help authors to use, a [binary index](creating-an-index-file.md) or a [site map index](to-create-an-index-that-uses-a-site-map.md). Each type of index has its own unique features.

## Binary index

This type of index is used only with compiled help (.chm) files. The following are some characteristics a binary index:

-   Good for large indexes because its compiled size is very small.
-   Is automatically sorted during compile. A help author cannot customize how a binary index is sorted.
-   Can be [merged](merging-help-files-at-run-time.md) with other indexes. All indexes are then sorted at compile time as one.
-   Can be used with [KLinks](working-with-klinks.md) to create links to specific topics.
-   Will automatically merge [keywords](create-keywords-for-a-binary-index.md) added to HTML files with Keyword links (KLinks) added to the index file.

## Site map index

This type of index must be used when authoring an index for a Web site. It can also be used with compiled help files. The following are some characteristics of a site map index:

-   Works on a Web site.
-   Help author has complete control over how the index is sorted.
-   Works without being compiled (but can also be compiled).
-   Same index can be used for Web site and compiled help file.
-   Is better to use with smaller indexes because site map indexes are larger than binary indexes.
-   [Keywords](create-keywords-for-a-site-map-index.md) are not merged with other indexes or sorted during compile.
-   KLinks do not work with site map indexes.

## Note

The method you use for creating keywords depends on whether you are creating an index that will be used in a compiled help file, on a Web site, or in a situation where there are multiple indexes.

## Related topics

<dl> <dt>

[About Creating Index Files](create-an-index-file.md)
</dt> </dl>

 

 




