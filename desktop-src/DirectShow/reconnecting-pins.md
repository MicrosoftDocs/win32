---
description: Reconnecting Pins
ms.assetid: 34b3e4de-e4eb-48c5-aaef-fc99b63e8691
title: Reconnecting Pins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reconnecting Pins

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

During a pin connection, a filter can disconnect and reconnect one of its other pins, as follows:

1.  The filter calls [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) on the other filter's pin, and specifies the new media type.
2.  If **QueryAccept** returns S\_OK, the filter calls [**IFilterGraph2::ReconnectEx**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph2-reconnectex) to reconnect the pins.

The following are some examples of when a filter might need to reconnect pins:

-   **Tee filters.** A *tee filter* splits an input stream into multiple outputs without changing the data in the stream. A tee filter can accept a range of media types, but the types must match across all pin connections. Therefore, when the input pin connects, the filter might need to renegotiate any existing connections on the output pins, and vice versa. For an example, see the [InfTee Filter Sample](inftee-filter-sample.md).
-   **Trans-in-place filters.** A *trans-in-place* filter modifies the input data in the original buffer instead of copying the data to a separate output buffer. A trans-in-place filter must use the same allocator for both the upstream and the downstream connections. The first pin to connect (input or output) negotiates an allocator in the usual way. When the other pin connects, however, the first allocator might not be acceptable. In that case, the second pin chooses a different allocator, and the first pin reconnects using the new allocator. For an example implementation, see the [**CTransInPlaceFilter**](ctransinplacefilter.md) class.

In the **ReconnectEx** method, the Filter Graph Manager asynchronously disconnects and reconnects the pins. The filter must not attempt the reconnection unless **QueryAccept** returns S\_OK. Otherwise, the pin will be left disconnected, causing graph errors. Also, the filter should request the reconnection from inside the [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) method, on the same thread. If the **Connect** method returns on one thread, while another thread makes the reconnection request, the Filter Graph Manager might run the graph before it makes the reconnection, causing graph errors.

 

 



