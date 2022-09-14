---
description: Microsoft Media Foundation is the next generation multimedia platform for Windows that enables developers, consumers, and content providers to embrace the new wave of premium content with enhanced robustness, unparalleled quality, and seamless interoperability.
ms.assetid: 3f933e39-8f9b-4c62-b528-4f1bba4b45d1
title: About Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# About Media Foundation

Microsoft Media Foundation is the next generation multimedia platform for Windows that enables developers, consumers, and content providers to embrace the new wave of premium content with enhanced robustness, unparalleled quality, and seamless interoperability.

Media Foundation requires Windows Vista or later. It uses the component object model (COM) and requires C/C++. Microsoft does not provide a managed API for Media Foundation.

The Media Foundation APIs are part of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx). To develop a Media Foundation application, install the latest version of the Windows SDK.

## Audio and Video Quality

Media Foundation has been designed to meet the challenges posed by high-definition content. Audio and video quality enhancements made throughout the platform now make it possible to deliver a great experience for next generation high-definition content.

-   DirectX Video Acceleration (DXVA) 2.0 offers more efficient video acceleration, compared with DXVA 1.0, with more robust and streamlined video decoding and extended use of hardware in video processing. With DXVA 2.0, Windows can handle some of the most demanding high-definition content with high quality and improved glitch-resilience.

-   Color-space information is preserved throughout the video pipeline. Users can enjoy video content with full fidelity. Color information and interlaced images are now passed to hardware for single-pass compositions. Preserving color-space information also reduces unnecessary color space conversions, which frees more cycles to process demanding HD content.
-   The enhanced video renderer (EVR) offers better timing support, enhanced video processing, and improved glitch-resilience. Full-screen playback support has been enhanced, and video tearing in windowed mode has been minimized.
-   Media Foundation uses the Multimedia Class Scheduler Service (MMCSS), a new system service in Windows Vista. MMCSS enables multimedia applications to ensure that their time-sensitive processing receives prioritized access to CPU resources.

## Content Access

As digital entertainment moves into the high-definition era and content becomes more portable and ubiquitous, content protection will become an integral part of digital media products. The extensibility of Media Foundation ensures that it can support these trends.

In addition, Media Foundation extensibility enables different content protection systems to operate together.

## About Media Foundation

This section contains general information about the Media Foundation APIs. Detailed programming information can be found in the [Media Foundation Programming Guide](media-foundation-programming-guide.md).



| Section                                                                              | Description                                                               |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [What's New for Media Foundation](whats-new-for-media-foundation.md)                | Describes new features in Media Foundation.                               |
| [Media Foundation Headers and Libraries](media-foundation-headers-and-libraries.md) | Lists the header and library files that define the Media Foundation APIs. |
| [Media Foundation Tools](media-foundation-tools.md)                                 | Describes the development tools that are available for Media Foundation.  |



 

Media Foundation is not included with the N and KN editions of Windows 8. For more information, see [Microsoft Windows Media Feature Pack for N and KN Versions of all Windows 8 Editions](https://support.microsoft.com/kb/2703761).

## Related topics

<dl> <dt>

[Microsoft Media Foundation](microsoft-media-foundation-sdk.md)
</dt> </dl>

 

 



