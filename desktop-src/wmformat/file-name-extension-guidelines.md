---
title: File Name Extension Guidelines
description: File Name Extension Guidelines
ms.assetid: 71189ed8-4140-446f-a765-d72f35dd3d88
keywords:
- Windows Media Format SDK,file name extensions
- Advanced Systems Format (ASF),file name extensions
- ASF (Advanced Systems Format),file name extensions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# File Name Extension Guidelines

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A file name extension provides an independent software vendor with information about the rendering requirements of an application that uses that particular extension.

The file name extension you must use for a file created by an application based on the Windows Media Format SDK is determined by the type of content in the file. Use the following logic to determine the file name extension you must use.

If the file contains any streams encoded with third-party codecs or any unsupported uncompressed data (including arbitrary data), the file must use the .asf extension.

If the file contains no unsupported streams and contains one or more video streams either uncompressed or encoded with any Windows Media video codec, the file must use the .wmv extension. These files may also include PCM audio streams, audio streams encoded with any Windows Media audio codec, script streams, and Web streams.

If the file contains no unsupported streams and no supported video streams, and contains one or more audio streams either uncompressed PCM or encoded with any Windows Media audio codec, the file must use the .wma extension. These files may also contain script streams, and Web streams.

If the file contains only streams that are neither audio nor video, it must use the .asf extension.

Supported uncompressed video types include RGB8, RGB565, RGB555, RGB24, RGB32, I420, IYUV, YV12, YUY2, UYVY, YVYU, and YVU9.

## Related topics

<dl> <dt>

[**Project Considerations**](project-considerations.md)
</dt> </dl>

 

 




