---
title: About the Video Compression Manager
description: About the Video Compression Manager
ms.assetid: 2a5ebc95-3ee8-4145-b2c5-512d82e49c6d
keywords:
- Windows multimedia,video compression manager (VCM)
- multimedia,video compression manager (VCM)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Video Compression Manager

Typically, installable compressors operate with video-image data stored in audio-video interleaved (AVI) files. This overview explains the programming techniques used to access installable compressors through VCM and covers the following topics:

-   VCM and the Video for Windows architecture
-   Compressing and decompressing image data from your application
-   Using VCM renderers to draw data from your application
-   VCM functions and structures

Before you read this overview, you should be familiar with the Microsoft Win32 graphic services. In particular, bitmaps and bitmap-related structures, such as [**BITMAPINFO**](https://msdn.microsoft.com/library/windows/desktop/dd183375) and [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd318229), are used extensively by VCM. For additional information about the **BITMAPINFO** and **BITMAPINFOHEADER** structures, see [Bitmaps](http://go.microsoft.com/fwlink/p/?linkid=16916).

> [!Note]  
> The audio compression manager (ACM) provides system-level support for audio compression and decompression drivers. For a description of the audio compression services, see [Audio Compression Manager](audio-compression-manager.md).

 

## Related topics

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> </dl>

 

 




