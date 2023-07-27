---
description: Sharing Data Between Streams
ms.assetid: e18eecf8-9475-420a-9a60-4b1b5f8fd43a
title: Sharing Data Between Streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sharing Data Between Streams

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

Processing multimedia data typically requires a great deal of system resources; therefore, you should avoid copying data whenever possible. The streaming architecture supports shared stream samples, a mechanism that moves data from one stream to another without copying it. This buffer enables the efficient transportation of data between two streams even if the destination stream doesn't specifically support the underlying data format.

For example, assume that you have a multimedia stream with three data streams: video and audio, and URL data time-stamped to match the video content. You want to write an application that adds a copyright notice on every video frame and writes the data to another stream for storage, but your application doesn't understand any data formats except the video stream. For the video stream, you create a sample attached to the desired DirectDraw surface. You can then create an output stream by calling either the [**IDirectDrawMediaStream::CreateSample**](/previous-versions/windows/desktop/api/ddstream/nf-ddstream-idirectdrawmediastream-createsample) method with that pointer to the same surface, or [**IMediaStream::CreateSharedSample**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imediastream-createsharedsample). In both cases, the input and output streams share the DirectDraw surface. Because you understand the video format, you can access this surface as needed.

To retrieve the other source stream pointers (audio and URL), enumerate the source container stream and grab pointers to the nonvideo streams. Each of these source streams has an associated output stream in the output stream container. Retrieve these output pointers by calling the [**IMultiMediaStream::GetMediaStream**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imultimediastream-getmediastream) method on the output container with each of the source stream pointers. The following steps describe this process.

1.  Call [**IMultiMediaStream::EnumMediaStreams**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imultimediastream-enummediastreams) to retrieve a pointer to a source stream. Make sure that it's not the video stream, because your application already understands its format.
2.  Call [**IMultiMediaStream::GetMediaStream**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imultimediastream-getmediastream) on the output container stream with the pointer from step 1. This returns a pointer to the desired output stream.
3.  Call [**AllocateSample**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imediastream-allocatesample) on the source stream.
4.  Call [**CreateSharedSample**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-imediastream-createsharedsample) on the output stream.
5.  Call [**Update**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-istreamsample-update) on the source stream to read the data.
6.  Call [**Update**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-istreamsample-update) on the output stream to write the data.

Repeat these steps for each stream whose format you don't support. When both samples finish updating, the output stream has all data from the source stream and you are done.

 

 



