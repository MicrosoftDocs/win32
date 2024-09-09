---
title: Video Input Formats
description: Video Input Formats
ms.assetid: 0f1ec15d-328e-4c07-bf58-fd4ecb483549
keywords:
- Windows Media Format SDK,video input formats
- Advanced Systems Format (ASF),video input formats
- ASF (Advanced Systems Format),video input formats
- video input formats
- Windows Media Format SDK,video formats
- Advanced Systems Format (ASF),video formats
- ASF (Advanced Systems Format),video formats
- video formats
- Windows Media Video 9 codec,video input formats
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Input Formats

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer accepts the following video formats as input to be compressed using the Windows Media Video 9 codec:

-   WMMEDIASUBTYPE\_IYUV
-   WMMEDIASUBTYPE\_I420
-   WMMEDIASUBTYPE\_YV12
-   WMMEDIASUBTYPE\_YUY2
-   WMMEDIASUBTYPE\_UYVY
-   WMMEDIASUBTYPE\_YVYU
-   WMMEDIASUBTYPE\_YVU9
-   WMMEDIASUBTYPE\_RGB32
-   WMMEDIASUBTYPE\_RGB24
-   WMMEDIASUBTYPE\_RGB565
-   WMMEDIASUBTYPE\_RGB555
-   WMMEDIASUBTYPE\_RGB8

You should always use [**IWMWriter::GetInputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-getinputformatcount) and [**IWMWriter::GetInputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputformat) to enumerate the available input formats and to obtain the input media properties object for the desired format. Video input media properties objects must be changed to reflect the frame size and frame rate of your input media.

## Related topics

<dl> <dt>

[**Media Type Identifiers**](media-type-identifiers.md)
</dt> <dt>

[**Media Types**](media-types.md)
</dt> </dl>

 

 




