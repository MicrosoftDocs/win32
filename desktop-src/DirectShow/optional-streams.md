---
description: Optional Streams
ms.assetid: 94477a71-c267-4602-893b-1bd1256b34ef
title: Optional Streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Optional Streams

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A DMO can designate some of its output streams as optional. An optional stream produces data that the application can discard, either completely or on occasional samples. For example, an optional stream might contain additional information about a primary stream.

To query whether a stream is optional, call the [**IMediaObject::GetOutputStreamInfo**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getoutputstreaminfo) method and check the *pdwFlags* parameter. Optional streams return either the DMO\_OUTPUT\_STREAMF\_DISCARDABLE flag or the DMO\_OUTPUT\_STREAMF\_OPTIONAL flag. These flags mean almost the same thing; one minor difference between them will be explained shortly.

If a stream is optional, the client can instruct the DMO to discard data from that stream when it processes the output. To do so, call the [**IMediaObject::ProcessOutput**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-processoutput) method and set the output buffer to **NULL** for each stream that you wish to discard. (The output buffer is specified in the **pBuffer** member of the [**DMO\_OUTPUT\_DATA\_BUFFER**](/previous-versions/windows/desktop/api/Mediaobj/ns-mediaobj-dmo_output_data_buffer).) Also set the DMO\_PROCESS\_OUTPUT\_DISCARD\_WHEN\_NO\_BUFFER flag in the *dwFlags* parameter.

For each stream where the *pBuffer* pointer is **NULL**, the DMO will attempt to discard the data. If the stream is optional, the DMO is guaranteed to discard the data. If the stream is not optional, the DMO discards the data when possible, but is not guaranteed to do so. If it cannot discard the data, it sets the DMO\_OUTPUT\_DATA\_BUFFERF\_INCOMPLETE flag. If you set a *pBuffer* pointer to **NULL** but do not set the DMO\_PROCESS\_OUTPUT\_DISCARD\_WHEN\_NO\_BUFFER flag, the DMO does not discard the data. In that case, the DMO either buffers the output internally, or simply fails the **ProcessOutput** call.

The only functional difference between the DMO\_OUTPUT\_STREAMF\_OPTIONAL flag and the DMO\_OUTPUT\_STREAMF\_DISCARDABLE flag is the following:

-   The DMO\_OUTPUT\_STREAMF\_OPTIONAL flag indicates that the client does not have to set a media type on that stream. However, if the client begins processing data without setting the media type for that stream, then it must discard the data from that stream for the entire duration of streaming. If you want to discard samples selectively, then you must set the media type.
-   The DMO\_OUTPUT\_STREAMF\_DISCARDABLE flag indicates that, although the stream is optional, it always requires a media type.

## Related topics

<dl> <dt>

[Directly Hosting a DMO](directly-hosting-a-dmo.md)
</dt> </dl>

 

 



