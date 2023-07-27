---
description: Transports
ms.assetid: 63c5ff5b-293d-4a80-92e8-3ece41321095
title: Transports
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Transports

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In order to move media data through the filter graph, a DirectShow filter must support one of several possible protocols. These protocols are called transports. When two filters connect, they must support the same transport; otherwise they cannot exchange media data. Typically, a transport requires that one of the pins support a particular interface. When the filters connect, one pin queries the other for the interface.

Most DirectShow filters hold media data in main memory, and deliver it to other filters across pin connections. This type of transport is called local memory transport. Although local memory transport is the most common transport in DirectShow, not all filters use it. For example, some filters send media data along a hardware path, and use pins only to deliver control information. For example, see the [**IOverlay**](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface.

DirectShow defines two mechanisms for local memory transport, the push model and the pull model. In the push model, a source filter generates data and delivers it to the next filter downstream. That filter passively receives the data, processes it, and sends it further downstream. In the pull model, the source filter is connected to a parser filter. The parser filter requests data from the source filter. The source filter responds to the requests by delivering data. The push model uses the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface, and the pull model uses the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface.

The push model is more common than the pull model. Therefore, the articles that follow assume a push model. The last article in this section, [Pull Model](pull-model.md), describes how the **IAsyncReader** interface differs from **IMemInputPin**.

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> </dl>

 

 



