---
title: Audio and Video Streams
description: Audio and Video Streams
ms.assetid: 809e5bb6-2bc4-4022-9117-a2be5418d7d1
keywords:
- Windows Media Format SDK,audio streams
- Advanced Systems Format (ASF),audio streams
- ASF (Advanced Systems Format),audio streams
- Windows Media Format SDK,video streams
- Advanced Systems Format (ASF),video streams
- ASF (Advanced Systems Format),video streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- audio streams,about
- video streams,about
ms.topic: article
ms.date: 05/31/2018
---

# Audio and Video Streams

The most common types of streams used in files created by using the Windows Media Format SDK are audio and video streams. Digital representations of audio and video data are complex and take up large amounts of memory. Under most circumstances, both audio and video are compressed before being added to an ASF file. Compression is accomplished using a compressor/decompressor (codec).

Several Windows Media codecs are included with this SDK, and they provide excellent quality compression for digital media. For more information about the Windows Media codecs, see [Codec Features](codec-features.md). Many other codecs are available from various sources. You can use whatever codecs you like when creating ASF files, but only the Windows Media codecs are directly supported by the objects of this SDK. To use other codecs, you must compress samples and pass them to the writer object as arbitrary data.

The most important distinction between audio or video streams and arbitrary streams is that streams containing Windows Media audio or video data are validated by the objects of the Windows Media Format SDK. Arbitrary data streams are not validated automatically, and should be checked for integrity by your application.

The properties of an audio or video stream are described in the profile used to create the file.

## Related topics

<dl> <dt>

[**Arbitrary Streams**](arbitrary-streams.md)
</dt> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




