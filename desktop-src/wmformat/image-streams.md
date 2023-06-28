---
title: Image Streams
description: Image Streams
ms.assetid: '17a945aa-463a-4aac-82cc-68b49c720c0a'
keywords:
- Windows Media Format SDK,image streams
- Advanced Systems Format (ASF),image streams
- ASF (Advanced Systems Format),image streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- image streams,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Image Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An image stream is a special type of stream that contains still images assigned to presentation times. An application can display the pictures in an image stream as desired, but the typical implementation is to display each picture until the next picture is delivered, like a slide show. Usually, an image stream is encoded in a file with an audio stream to produce a simple presentation of images synchronized with music or speech.

Image streams are like video streams in that they are created from uncompressed samples that are compressed as part of the file writing process, but they are also like arbitrary streams because you must assign a bit rate and buffer window appropriate to the content without relying on codec-assigned properties.

## Related topics

<dl> <dt>

[**Arbitrary Streams**](arbitrary-streams.md)
</dt> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Audio and Video Streams**](audio-and-video-streams.md)
</dt> <dt>

[**Writing Image Streams**](writing-image-streams.md)
</dt> </dl>

 

 




