---
description: Using the Media Detector
ms.assetid: 462150d5-7315-4c2b-81b0-964a788ec47d
title: Using the Media Detector
ms.topic: article
ms.date: 05/31/2018
---

# Using the Media Detector

\[This API is not supported and may be altered or unavailable in the future.\]

The media detector is a helper object that can retrieve information about a file, such as the number of streams, their type, and their duration. It also contains methods for retrieving poster frames from a video stream. It exposes the [**IMediaDet**](imediadet.md) interface.

The media detector operates in one of two modes. When you create an instance of the media detector, it is not attached to a particular source file. In this mode, you can retrieve stream information from multiple source files. However, once you use the media detector to obtain a poster frame, it switches to *bitmap grab mode*. In bitmap grab mode, the media detector is attached to a specific video stream, and the stream information methods no longer work. Moreover, there is no way to switch the media detector back to its starting mode. Therefore, obtain any stream information you need before retrieving poster frames, or else create new instances of the media detector for each stream.

To obtain stream information, do the following:

1.  Call [**IMediaDet::put\_Filename**](imediadet-put-filename.md) with the name of the source file.
2.  Call [**IMediaDet::get\_OutputStreams**](imediadet-get-outputstreams.md) to obtain the number of streams in the source.
3.  Specify a stream number with [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md). Then call one or more of the following methods:
    -   [**IMediaDet::get\_StreamType**](imediadet-get-streamtype.md): Retrieves the stream's media type.
    -   [**IMediaDet::get\_StreamLength**](imediadet-get-streamlength.md): Retrieves the duration of the stream.
    -   [**IMediaDet::get\_FrameRate**](imediadet-get-framerate.md): Retrieves a video stream's frame rate.

To obtain a poster frame, specify the stream number, as in the previous step. Then call either [**IMediaDet::GetBitmapBits**](imediadet-getbitmapbits.md), which copies a poster frame into a buffer, or [**IMediaDet::WriteBitmapBits**](imediadet-writebitmapbits.md), which saves a poster frame to a file.

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



