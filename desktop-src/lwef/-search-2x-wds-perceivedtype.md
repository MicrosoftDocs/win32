---
title: Perceived Types (Legacy Windows Environment Features)
description: PerceivedType is a property that classifies an item in the index.
ms.assetid: 47a5cf55-79f6-48e7-a585-72fc3d7d53d4
ms.topic: article
ms.date: 05/31/2018
---

# Perceived Types (Legacy Windows Environment Features)

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

`PerceivedType` is a property that classifies an item in the index. This classification is different from the "kind" classification used by the [Advanced Query Syntax](-search-2x-wds-aqsreference.md) but similarly lets users refine their search results. The AQS kind lets users limit their search query while the PerceivedType property lets users filter their result set.

## Types

Use the PerceivedType property to classify your file type so that users can filter their search results by type. The output must be one of the following strings:

-   contact
-   communications
-   communications/email
-   communications/calendar
-   communications/task
-   communications/im
-   document
-   document/note
-   document/text
-   document/spreadsheet
-   document/presentation
-   music
-   images
-   images/picture
-   images/video
-   folder
-   program

For example, when you want to create a filter add-in for a new picture file type, you need to implement the following in your [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface:

-   **GetChunk** to return a FULLPROPSPEC that includes: D5CDD505-2E9C-101B-9397-08002B2CF9AE/PerceivedType
-   **GetValue** to return a PROPVARIANT that includes: VT\_LPWSTR = "images/picture"

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Developing IFilter Add-ins](-search-2x-wds-ifilteraddins.md)
</dt> <dt>

[Developing Protocol Handlers](-search-2x-wds-phaddins.md)
</dt> <dt>

[Advanced Query Syntax](-search-2x-wds-aqsreference.md)
</dt> <dt>

[SchemaTable](-search-2x-wds-schematable.md)
</dt> </dl>

 

 
