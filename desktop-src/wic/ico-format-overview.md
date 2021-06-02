---
description: This topic provides information about the native ICO codec available through Windows Imaging Component (WIC).
ms.assetid: EF28956E-7156-4BAE-8805-C64B8C8ADE50
title: ICO Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# ICO Format Overview

This topic provides information about the native ICO codec available through Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



|                        |                   |
|------------------------|-------------------|
| Formal Name(s)         | Icon Format (ICO) |
| File Name Extension(s) | ico               |
| MIME type              | image/ico         |
| Specification Support  |                   |



 

The following table lists the GUIDs used to identify the native ICO codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatIco | a3a860c4-338f-4c17-919afba4b5628f21 |
| Decoder          | CLSID\_WICIcoDecoder     | c61bfcdf-2e0f-4aad-a8d7e06bafebcdfe |
| Encoder          | NOT AVAILABLE            | NOT AVAILABLE                       |



 

## Encoding

WIC does not provide a native ICO image encoder.

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 



