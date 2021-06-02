---
description: This topic provides information about the native DNG codec available through Windows Imaging Component (WIC).
ms.assetid: 6F87A47D-E54A-42D9-92DC-2411803278AA
title: DNG Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# DNG Format Overview

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This topic provides information about the native DNG codec available through Windows Imaging Component (WIC).

-   [Codec Identity](#codec-identity)
-   [Decoding](#decoding)

## Codec Identity

The following table provides codec identification information.



|                        |                                                      |
|------------------------|------------------------------------------------------|
| Formal Name(s)         | Digital Negative (DNG)                               |
| File Name Extension(s) | .dng                                                 |
| MIME type(s)           | image/DNG                                            |
| Specification Support  | Digital Negative (DNG) Specification Version 1.4.0.0 |



 

The following table lists the GUIDs used to identify the native DNG codec components.



| Component        | Friendly Name             | GUID                                |
|------------------|---------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatAdng | f3ff6d0d-38c0-41c4-b1fe1f3824f17b84 |
| Decoder          | CLSID\_WICAdngDecoder     | 981d9411-909e-42a7-8f5da747ff052edb |



 

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

The decoder does not support decoding raw sensor data and only supports files with a non-raw image representation embedded in an IFD with NewSubFileType equal to 1.

 

 



