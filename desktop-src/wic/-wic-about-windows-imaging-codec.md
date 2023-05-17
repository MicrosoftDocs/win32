---
description: The Windows Imaging Component (WIC) provides an extensible framework for working with images and image metadata.
ms.assetid: a05b496a-bd4c-4065-8060-df0f8930cde7
title: Windows Imaging Component Overview
ms.topic: article
ms.date: 05/31/2018
---

# Windows Imaging Component Overview

The Windows Imaging Component (WIC) provides an extensible framework for working with images and image metadata. WIC makes it possible for independent software vendors (ISVs) and independent hardware vendors (IHVs) to develop their own image codecs and get the same platform support as standard image formats (for example, TIFF, JPEG, PNG, GIF, BMP, and HDPhoto). A single, consistent set of interfaces is used for all image processing, regardless of image format, so any application using the WIC gets automatic support for new image formats as soon as the codec is installed. The extensible metadata framework makes it possible for applications to read and write their own proprietary metadata directly to image files, so the metadata never gets lost or separated from the image.

This topic includes the following sections.

-   [Windows Imaging Component Features](#windows-imaging-component-features)
-   [Native Codecs](#native-codecs)
-   [Related topics](#related-topics)

## Windows Imaging Component Features

The primary features of WIC are:

-   Enables application developers to perform image processing operations on any image format through a single, consistent set of common interfaces, without requiring prior knowledge of specific image formats.
-   Provides an extensible "plug and play" architecture for image codecs, pixel formats, and metadata, with automatic run-time discovery of new formats.
-   Supports reading and writing of arbitrary metadata in image files, with the ability to preserve unrecognized metadata during editing.
-   Preserves high bit depth image data, up to 32 bits per channel, throughout the image processing pipeline.
-   Provides built-in support for most popular image formats, pixel formats, and metadata schemas.

## Native Codecs

WIC includes several built-in codecs. The following standard codecs are provided with the platform. 

| Codec                                                                                             | Mime Types                       | Decoders | Encoders |
|---------------------------------------------------------------------------------------------------|----------------------------------|----------|----------|
| BMP (Windows Bitmap Format), BMP Specification v5.                                                | image/bmp                        | Yes      | Yes      |
| GIF (Graphics Interchange Format 89a), GIF Specification 89a/89m                                  | image/gif                        | Yes      | Yes      |
| ICO (Icon Format)                                                                                 | image/ico                        | Yes      | No       |
| JPEG (Joint Photographic Experts Group), JFIF Specification 1.02                                  | image/jpeg, image/jpe, image/jpg | Yes      | Yes      |
| JPEG XR (JPEG Extended Range)                                                                     | image/jxr                        | Yes      | Yes      |
| PNG (Portable Network Graphics), PNG Specification 1.2                                            | image/png                        | Yes      | Yes      |
| TIFF (Tagged Image File Format), TIFF Specification 6.0                                           | image/tiff, image/tif            | Yes      | Yes      |
| Windows Media Photo, [HD Photo Specification 1.0](https://www.microsoft.com/whdc/xps/wmphoto.mspx) | image/vnd.ms-photo               | Yes      | Yes      |
| DDS (DirectDraw Surface)                                                                          | image/vnd.ms-dds                 | Yes      | Yes      |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[AITCodec Sample CODEC](/previous-versions/dotnet/netframework-3.0/ms771770(v=vs.85))
</dt> </dl>

 

 
