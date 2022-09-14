---
description: The WMContainer objects provide low-level control over parsing and writing an Advanced Systems Format (ASF) file.
ms.assetid: 258ea139-581f-4b94-9655-43ecf1e77f10
title: WMContainer ASF Components
ms.topic: article
ms.date: 05/31/2018
---

# WMContainer ASF Components

The WMContainer objects provide low-level control over parsing and writing an Advanced Systems Format (ASF) file.

The [Pipeline Layer ASF Components](pipeline-layer-asf-components.md) use the WMContainer objects internally. Most applications should use the pipeline components, rather than using WMContainer objects. Use WMContainer only if you require low-level control over parsing and writing an ASF file.

The WMContainer layer includes the following objects:

-   [ASF Profile](asf-profile.md)
-   [ASF ContentInfo Object](asf-contentinfo-object.md)
-   [ASF Splitter](asf-splitter.md)
-   [ASF Multiplexer](asf-multiplexer.md)
-   [ASF Indexer](asf-index-object.md)

The following topics contain step-by-step instructions about using WMContainer to read or write ASF files.

-   [Tutorial: Reading an ASF File by Using WMContainer Objects](tutorial--reading-an-asf-file.md)
-   [Tutorial: Copying ASF Streams by Using WMContainer Objects](tutorial--copying-asf-streams-from-one-file-to-another.md)
-   [Tutorial: Writing a WMA File by Using WMContainer Objects](tutorial--writing-a-wma-file-by-using-cbr-encoding.md)

## About WM Container

The WMContainer objects interact directly with ASF file objects. The following diagram shows the ASF file structure and the corresponding WMContainer objects.

![diagram showing the asf file structure and corresponding media foundation objects](images/asf-components01.png)

Except for the splitter and multiplexer, each of these objects supports both parsing (reading) and writing ASF files. The splitter is used only for reading ASF files. The multiplexer is used only for authoring new ASF files.

All operations performed by WMContainer objects are synchronous, meaning they block the calling thread.

## Related topics

<dl> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 



