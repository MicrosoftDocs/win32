---
description: What's New in DirectShow
ms.assetid: 675a34d4-7a33-4125-86af-cd4ed73ad430
title: What's New in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# What's New in DirectShow

## What's New for DirectShow in Windows 7

New interfaces:

-   [**IAMAsyncReaderTimestampScaling**](/windows/desktop/api/Strmif/nn-strmif-iamasyncreadertimestampscaling)
-   [**IAMPluginControl**](/windows/desktop/api/Strmif/nn-strmif-iamplugincontrol)

New or updated filters:

-   [**Microsoft MPEG-1/DD/AAC Audio Decoder**](microsoft-mpeg-1-dd-audio-decoder.md)
-   [**Microsoft MPEG-2 Video Decoder**](microsoft-mpeg-2-video-decoder.md)

The "intelligent connect" algorithms have been modified to support preferred and blocked filters. For details, see [Intelligent Connect](intelligent-connect.md).

DVD playback: New options for the [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) method.

## What's New for DirectShow in Windows Vista

-   DirectShow is now part of the Windows SDK. The DirectShow headers, libraries, samples, and tools are no longer included in the DirectX SDK.
-   DirectX Video Acceleration (DXVA) 2.0 contains many enhancements from DXVA 1.0.

    -   The hardware video pipeline has been significantly improved.
    -   Components such as decoders can access DXVA 2.0 directly without communicating through the video renderer.
    -   The Direct3D Device Manager enables components to share the same Direct3D device.

    For more information about DXVA 2.0, see the [DirectX Video Acceleration 2.0](../medfound/directx-video-acceleration-2-0.md) documentation, which is part of the [Microsoft Media Foundation](../medfound/microsoft-media-foundation-sdk.md) documentation.

-   The [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) is a powerful new video renderer, which shares the same plug-in model as the Media Foundation version of the EVR. For more information about the EVR, see the [Microsoft Media Foundation](../medfound/microsoft-media-foundation-sdk.md) documentation.
-   Support for Windows Vista Display Driver Model (WDDM) capture. This feature enables filters to take full advantage of video cards with integrated video capture, to reduce unnecessary copies between video memory and system memory. For more information, see [Using WDDM Capture in DirectShow](using-wddm-capture-in-directshow.md).
-   The MPEG-1 Layer II audio decoder now uses floating-point arithmetic, for improved decoding quality.
-   DVD playback enhancements. For details, see [DVD Playback Enhancements in Windows Vista](dvd-playback-enhancements-in-windows-vista.md).
    -   Better trick-mode support: Smooth transitions between rates; transitions between forward and reverse playback; support for audio playback during fast-forward and reverse.
    -   Enhanced caching. Applications can set how much data the DVD Navigator reads in advance. Setting a larger cache can extend battery life and enable silent playback (after the drive spins down). For more information, see [**DVD\_OPTION\_FLAG**](/windows/win32/api/strmif/ne-strmif-dvd_option_flag).
-   Audio end-point devices: Applications can associate the [DirectSound Renderer Filter](directsound-renderer-filter.md) with a particular audio end-point device. Applications can use the Multimedia Device (MMDevice) API to enumerate and select the end-point device. For more information, see the Core Audio API documentation in the Windows SDK.
-   The following filters have been removed from Windows Vista:
    -   [BDA IP Sink Filter](/previous-versions/windows/desktop/mstv/bda-ip-sink-filter)
    -   [BDA SLIP Deframer Filter](/previous-versions/windows/desktop/mstv/bda-slip-deframer-filter)
    -   [CC Decoder Filter](cc-decoder-filter.md)
    -   [NABTS/FEC VBI Codec Filter](/previous-versions/windows/desktop/mstv/nabts-fec-vbi-codec-filter)
    -   [QT Decompressor Filter](qt-decompressor-filter.md)
    -   [QuickTime Movie Parser Filter](quicktime-movie-parser-filter.md)
    -   [WST Codec Filter](wst-codec-filter.md)
    -   [WST Decoder Filter](wst-decoder-filter.md)
-   The proxy/stub code for many of the DirectShow interfaces has been moved from quartz.dll to proppage.dll. This code was removed from quartz.dll because it was not intended for use by applications. However, it is useful for debugging, because it enables a test application to connect remotely to a DirectShow filter graph in another process. To use this feature in Windows Vista, you must first register proppage.dll. This DLL is available in the Windows SDK tools directory. (For more information, see [Loading a Graph From an External Process](loading-a-graph-from-an-external-process.md).)

 

 
