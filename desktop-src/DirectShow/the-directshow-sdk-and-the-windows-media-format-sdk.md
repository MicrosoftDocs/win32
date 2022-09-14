---
description: The DirectShow SDK and the Windows Media Format SDK
ms.assetid: d9ac89cc-0d55-4c51-ae0a-592422d97383
title: The DirectShow SDK and the Windows Media Format SDK
ms.topic: article
ms.date: 05/31/2018
---

# The DirectShow SDK and the Windows Media Format SDK

DirectShow and the Windows Media Format SDK offer complementary solutions for writing applications that create and play back Windows Media Format streams. For more information, see the "[Audio and Video](../audio-and-video.md)" section of the MSDN Library.

The ASF Writer filter accepts any number of input streams and creates an ASF file. The filter uses the Windows Media Format SDK to convert uncompressed audio or video files to Windows Media-based content. The compressed content is then stored in the ASF container format. If the content is audio only, then the file is given a .wma extension and is referred to as a Windows Media Audio file. If the content is video only or video and audio, then the file is given a .wmv extension and is referred to as a Windows Media Video file. Either type of file may also include metadata.

You can use the WM ASF Writer in various scenarios including digital video (DV) capture, audio recompression, and conversion of Audio-Video Interleaved (AVI) or MPEG multimedia files for network streaming. This filter provides the only way to create Microsoft® Windows Media™ Audio (WMA) and Windows Media Video (WMV) files in DirectShow®. The filter can also create files that are secured by Digital Rights Management (DRM), and can also create MPEG-4 content using the Microsoft MPEG-4 Encoder. This content is stored in the ASF container format.

## Related topics

<dl> <dt>

[Creating ASF Files in DirectShow](creating-asf-files-in-directshow.md)
</dt> </dl>

 

 
