---
title: Rendering Content
description: Rendering Content
ms.assetid: 9a3baa33-dac4-4742-8f80-33b05caada09
keywords:
- Windows Media Format SDK,rendering content
- Advanced Systems Format (ASF),rendering content
- ASF (Advanced Systems Format),rendering content
- Advanced Systems Format (ASF),content rendering
- ASF (Advanced Systems Format),content rendering
ms.topic: article
ms.date: 05/31/2018
---

# Rendering Content

The Windows Media Format SDK does not provide any routines for rendering content delivered by the reader object. If you write applications to play back the content in ASF files, you must implement your own rendering routines.

You must be careful when rendering content to ensure that samples are rendered in order of presentation time and that samples from different streams are synchronized when rendering. The method you employ to ensure stream synchronization will depend upon the rendering technique you use for your application. In general, if you have audio and video streams, you should synchronize to the audio stream, because inconsistency in the audio stream is more noticeable than a few dropped frames in a video stream.

## Related topics

<dl> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**To Retrieve Media Samples with the Asynchronous Reader**](to-retrieve-media-samples-with-the-asynchronous-reader.md)
</dt> <dt>

[**To Retrieve Media Samples with the Synchronous Reader**](to-retrieve-media-samples-with-the-synchronous-reader.md)
</dt> </dl>

 

 




