---
description: Writing DirectShow Filters
ms.assetid: ffbc92b2-4f45-439b-b140-49a66fc4d914
title: Writing DirectShow Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing DirectShow Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you are developing a filter for use in a Microsoft DirectShow filter graph, read the articles in this section. In general, you do not have to read this section if you are writing a DirectShow application. Most applications do not access filters or the filter graph at the level discussed in this section.

-   [Introduction to DirectShow Filter Development](introduction-to-directshow-filter-development.md)
-   [Building DirectShow Filters](building-directshow-filters.md)
-   [How Filters Connect](how-filters-connect.md)
-   [Data Flow for Filter Developers](data-flow-for-filter-developers.md)
-   [Threads and Critical Sections](threads-and-critical-sections.md)
-   [Quality-Control Management](quality-control-management.md)
-   [DirectShow and COM](directshow-and-com.md)
-   [Writing Source Filters](writing-source-filters.md)
-   [Writing Transform Filters](writing-transform-filters.md)
-   [Writing Video Renderers](writing-video-renderers.md)
-   [Writing Capture Filters](writing-capture-filters.md)
-   [Exposing Capture and Compression Formats](exposing-capture-and-compression-formats.md)
-   [Registering a Custom File Type](registering-a-custom-file-type.md)
-   [Creating a Filter Property Page](creating-a-filter-property-page.md)

 

 



