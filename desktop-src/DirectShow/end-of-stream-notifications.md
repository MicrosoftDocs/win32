---
description: End-of-Stream Notifications
ms.assetid: cf2b13bc-5b54-4ac7-8a33-7434126fdf31
title: End-of-Stream Notifications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# End-of-Stream Notifications

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a source filter is done sending data, it calls the [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method on the downstream input pin. The downstream filter propagates the call to the next filter, and so on. When the **EndOfStream** call reaches the renderer, the renderer sends an [**EC\_COMPLETE**](ec-complete.md) event to the Filter Graph Manager. If the renderer has multiple input pins, it delivers the EC\_COMPLETE event after every input pin has received the end-of-stream notification.

A filter must serialize [**EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) calls with other streaming calls, such as [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive). (In other words, the downstream filter must always receive the calls in the correct order.)

In some cases, a downstream filter might detect the end of the stream before the source filter does. (For example, the downstream filter might be parsing the stream.) In that case, the downstream filter can send the end-of-stream notification, in which case it should return S\_FALSE from [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) until the graph stops or flushes. The S\_FALSE return value informs the source filter to stop sending data.

### Default Handling of EC\_COMPLETE

By default, the Filter Graph Manager does not forward every EC\_COMPLETE event to the application. Instead, it waits until all streams have signaled EC\_COMPLETE and then sends a single EC\_COMPLETE event. Thus, the application receives the event after every stream has completed.

To determine the number of streams, the Filter Graph Manager counts the number of filters that support seeking (through [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) or [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition)) and have a *rendered* input pin, which is defined as an input pin with no corresponding outputs. The Filter Graph Manager determines whether a pin is rendered in one of two ways:

-   The pin's [**IPin::QueryInternalConnections**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryinternalconnections) method returns zero in the *nPin* parameter.
-   The filter exposes the [**IAMFilterMiscFlags**](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags) interface and returns the AM\_FILTER\_MISC\_FLAGS\_IS\_RENDERER flag.

### End-of-Stream Notifications in Pull Mode

In an [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) connection, the source filter does not send an end-of-stream notification. Instread, this is done by the downstream filter, which is typically a parser filter. The parser sends the [**EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) call downstream. It does not send one upstream to the source filter.

## Related topics

<dl> <dt>

[Delivering the End of Stream](delivering-the-end-of-stream.md)
</dt> </dl>

 

 



