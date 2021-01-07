---
description: Introduction (WIC Guidelines for Camera RAW Image Formats)
ms.assetid: 3c588386-1d4d-4ee0-b633-bfc94ca751ea
title: Introduction (WIC Guidelines for Camera RAW Image Formats)
ms.topic: article
ms.date: 05/31/2018
---

# Introduction (WIC Guidelines for Camera RAW Image Formats)

The Windows Imaging Component (WIC) provides an extensible framework for working with images and image metadata. WIC makes it possible for software and hardware vendors to develop codecs so that their own image formats can obtain the same platform support as native image formats such as tagged image file format (TIFF), Joint Photographic Experts Group (JPEG), or HD Photo.

WIC provides a single, consistent set of interfaces for all image processing, regardless of image format. Therefore, any application that uses WIC receives automatic support for new image formats as soon as the codec is installed. WIC also provides an extensible metadata framework that makes it possible for applications to read and write their own proprietary metadata directly to image files, so the metadata is never lost or separated from the image.

WIC is included with Windows Presentation Foundation (WPF) and is built into Windows Vista and later Windows versions. It is also available as a stand-alone redistributable component for Windows XP.

These guidelines are designed to help RAW format manufacturers in their development of WIC codecs.

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

 

 



