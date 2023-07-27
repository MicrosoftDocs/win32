---
description: Pull Model
ms.assetid: b5246dfe-e6ee-4b91-bfe3-2ec8b8723938
title: Pull Model
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pull Model

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface, the upstream filter determines what data to send, and it pushes the data to the downstream filter. For some filters, a *pull* model is more appropriate. Here, the downstream filter requests data from the upstream filter. Samples still travel downstream, from output pin to input pin, but the downstream filter initiates the data flow. This type of connection uses the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface.

The typical use for the pull model is in file playback. For example, in an AVI playback graph, the [Async File Source](file-source--async--filter.md) filter performs generic file reading operations and delivers the data as a byte stream, with no format information. The [AVI Splitter](avi-splitter-filter.md) filter reads the AVI headers and parses the stream into video and audio samples. The AVI Splitter can determine what data it needs better than the Async File Source filter, and therefore it uses **IAsyncReader** instead of **IMemInputPin**.

To request data from the output pin, the input pin calls one of the following methods:

-   [**IAsyncReader::Request**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-request)
-   [**IAsyncReader::SyncRead**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-syncread)
-   [**IAsyncReader::SyncReadAligned**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-syncreadaligned).

The first method is asynchronous, to support multiple overlapped reads. The others are synchronous.

In theory, any filter can support **IAsyncReader**, but in practice it is designed for source filters that connect to parser filters. The parser acts very much like a source filter in the push model. When it pauses, it creates a streaming thread that pulls data from the **IAsyncReader** connection and pushes it downstream. The output pins use **IMemInputPin**, and the rest of the graph uses the standard push model.

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> </dl>

 

 



