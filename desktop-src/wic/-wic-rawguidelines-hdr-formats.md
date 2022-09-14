---
description: High Dynamic Range Pixel Formats
ms.assetid: 037b6bde-a3e0-401d-9be7-b58c5f74c30a
title: High Dynamic Range Pixel Formats
ms.topic: article
ms.date: 05/31/2018
---

# High Dynamic Range Pixel Formats

Codecs should use Windows Imaging Component (WIC) pixel formats that preserve all of the dynamic range of the underlying sensor data. GUID\_WICPixelFormat48bppRGB is a typical fixed-point 16-bit-per-channel format that can be used. Other higher precision formats can be used also. To enable full support for the Windows Presentation Foundation graphics processing unit (GPU)-accelerated rendering pipeline, Microsoft strongly encourages support for a 32-bit floating point pixel format.

High Color Pixel Formats: With Windows 7, two new WIC pixel formats have been added to support the new High Color display formats. These are: GUID\_WICPixelFormat32bppRGBA1010102 and GUID\_WICPixelFormat32bppRGBA1010102XR.

The 16 bit per channel (bpc) float High Color format is supported by the existing GUID\_WICPixelFormat64bppRGBAHalf pixel format.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



