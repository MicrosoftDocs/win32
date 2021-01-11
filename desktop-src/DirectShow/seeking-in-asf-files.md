---
description: Seeking in ASF Files
ms.assetid: da0d687b-f571-4623-9705-e697ba8bc04e
title: Seeking in ASF Files (DirectShow)
ms.topic: article
ms.date: 05/31/2018
---

# Seeking in ASF Files (DirectShow)

The [WM ASF Reader](wm-asf-reader-filter.md), through its [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface, can perform very accurate temporal seeking on Windows Media–based content that has a temporal index. (All frame-indexed content also contains a temporal index.) Guaranteed frame-accurate seeking is not directly supported in the WM ASF Reader, but there is a way to do it if you require this functionality. First, use the Windows Media Format SDK directly to create an instance of the synchronous reader object, open the file, obtain the time stamp associated with a specified frame, and then use the DirectShow **IMediaSeeking** interface to seek to that time. The [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep) interface does not support frame-accurate seeking of Windows Media–based content.

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



