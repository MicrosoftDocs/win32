---
title: Seeking in ASF Files (Windows Media Format 11 SDK)
description: Seeking in ASF Files
ms.assetid: a1717cb4-9f41-4148-b088-a6517be7da9b
keywords:
- Windows Media Format SDK,seeking in ASF files
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),seeking
- ASF (Advanced Systems Format),seeking
- DirectShow,seeking in ASF files
ms.topic: article
ms.date: 05/31/2018
---

# Seeking in ASF Files (Windows Media Format 11 SDK)

The [WM ASF Reader](wm-asf-reader-filter.md), through its **IMediaSeeking** interface, can perform very accurate temporal seeking on Windows Media–based content that has a temporal index. (All frame-indexed content also contains a temporal index.) Guaranteed frame-accurate seeking is not directly supported in the WM ASF Reader, but there is a way to do it if you require this functionality. First, use the Windows Media Format SDK directly to create an instance of the synchronous reader object, open the file, obtain the time stamp associated with a specified frame, and then use the DirectShow **IMediaSeeking** interface to seek to that time. The DirectShow **IVideoFrameStep** interface does not support frame-accurate seeking of Windows Media–based content. The DSSeekFm sample in the Windows Media Format SDK demonstrates how to perform frame-accurate seeking using the WM ASF Reader.

## Related topics

<dl> <dt>

[**WM ASF Reader Filter**](wm-asf-reader-filter.md)
</dt> </dl>

 

 




