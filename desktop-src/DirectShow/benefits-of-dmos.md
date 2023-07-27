---
description: Benefits of DMOs
ms.assetid: 7ff3fd9c-9423-4915-8ce2-22783ed455fb
title: Benefits of DMOs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Benefits of DMOs

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DMOs offer the following advantages:

-   They are generally smaller and simpler than DirectShow filters, because they support less functionality.
-   They are more flexible than DirectShow filters because they do not require a filter graph. You can use them with DirectShow when you need the services that DirectShow provides, such as synchronization, intelligent connection, automatic handling of data flow, and thread management. Clients that do not need these services can access DMOs directly.
-   DMOs always perform synchronous data processing, which eliminates many of the threading issues that you must consider if you write a filter.
-   Unlike traditional ACM and VCM codecs, DMOs are based on the Component Object Model (COM), so they can be extended through **QueryInterface**.
-   DMOs support a more generalized streaming model than ACM or VCM codecs. Like DirectShow filters, DMOs can support multiple inputs and multiple outputs.

For these reasons, DMOs are now recommended as the solution for writing encoders, decoders, and audio effects. Many other scenarios are possible as well, depending on the needs of the application.

How DMOs Differ from DirectShow Filters

DirectShow filters cannot function outside of a DirectShow filter graph. In DirectShow, the Filter Graph Manager mediates between the application and the filters. DirectShow filters do most of the work required to stream data, including:

-   Allocating buffers.
-   Negotiating media types and connections to other filters.
-   Pushing data through the filter graph.
-   Sending events to the Filter Graph Manager.
-   Synchronizing multiple threads.

In contrast, a DMO does none of these things. Instead, these kinds of tasks are the responsibility of the client using the DMO. The client allocates buffers, fills them with data, and delivers them to the DMO. The DMO processes the data, and the client retrieves the resulting output buffers.

## Related topics

<dl> <dt>

[About DMOs](about-dmos.md)
</dt> </dl>

 

 



