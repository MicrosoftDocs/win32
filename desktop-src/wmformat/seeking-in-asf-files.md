---
title: Seeking in ASF Files (Windows Media Format 11 SDK)
description: Learn how the WM ASF Reader can perform very accurate temporal seeking on Windows Media–based content that has a temporal index in Windows Media Format 11 SDK.
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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Seeking in ASF Files (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [WM ASF Reader](wm-asf-reader-filter.md), through its **IMediaSeeking** interface, can perform very accurate temporal seeking on Windows Media–based content that has a temporal index. (All frame-indexed content also contains a temporal index.) Guaranteed frame-accurate seeking is not directly supported in the WM ASF Reader, but there is a way to do it if you require this functionality. First, use the Windows Media Format SDK directly to create an instance of the synchronous reader object, open the file, obtain the time stamp associated with a specified frame, and then use the DirectShow **IMediaSeeking** interface to seek to that time. The DirectShow **IVideoFrameStep** interface does not support frame-accurate seeking of Windows Media–based content. The DSSeekFm sample in the Windows Media Format SDK demonstrates how to perform frame-accurate seeking using the WM ASF Reader.

## Related topics

<dl> <dt>

[**WM ASF Reader Filter**](wm-asf-reader-filter.md)
</dt> </dl>

 

 




