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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rendering Content

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




