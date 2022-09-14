---
title: Getting the Best Video Seeking Performance
description: Getting the Best Video Seeking Performance
ms.assetid: 21269f0c-fc3a-46fc-88b4-f71828b5d5a7
keywords:
- Windows Media Format SDK,best video seeking performance
- Advanced Systems Format (ASF),best video seeking performance
- ASF (Advanced Systems Format),best video seeking performance
- Advanced Systems Format (ASF),video seeking performance
- ASF (Advanced Systems Format),video seeking performance
- Advanced Systems Format (ASF),performance
- ASF (Advanced Systems Format),performance
- video seeking
- performance,video seeking
ms.topic: article
ms.date: 05/31/2018
---

# Getting the Best Video Seeking Performance

Seeking to content in a file is a very common operation that is potentially a performance issue. Video encoded with the Windows Media Video 9 codec is made up primarily of delta frames, which only record the changes in relation to the previous frame. Reconstructing delta frames takes time, particularly if the key frames are far apart. For more information about configuring key frames for efficient seeking, see [Configuring Video Streams for Seeking Performance](configuring-video-streams-for-seeking-performance.md).

In addition to proper configuration, you can improve seeking performance by using frame indexing for the video stream. Seeking to a frame number is typically faster than seeking to a presentation time.

If seeking in a file with multiple streams, you should select only the streams that are needed. Each stream configured for reading will affect the performance of seeking, because all selected streams are synchronized when you seek to a point in a file.

## Related topics

<dl> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**To Seek By Frame Number Using the Asynchronous Reader**](to-seek-by-frame-number-using-the-asynchronous-reader.md)
</dt> <dt>

[**To Seek By Frame Number Using the Synchronous Reader**](to-seek-by-frame-number-using-the-synchronous-reader.md)
</dt> <dt>

[**To Seek By Time Using the Asynchronous Reader**](to-seek-by-time-using-the-asynchronous-reader.md)
</dt> <dt>

[**To Seek By Time Using the Synchronous Reader**](to-seek-by-time-using-the-synchronous-reader.md)
</dt> </dl>

 

 




