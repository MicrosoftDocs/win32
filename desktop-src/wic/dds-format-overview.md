---
description: Provides information about the native DDS codec available through the Windows Imaging Component (WIC).
ms.assetid: 6CFDD674-C8AE-4F29-B2E5-C9C9431CB85A
title: DDS Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# DDS Format Overview

This topic provides information about the native DDS codec available through the Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



| Component              | Description        |
|------------------------|--------------------|
| Formal Name(s)         | DirectDraw Surface |
| File Name Extension(s) | dds                |
| MIME type              | image/vnd-ms.dds   |



 

The following table lists the GUIDs used to identify the native DDS codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatDds | 9967cb95-2e85-4ac8-8ca283d7ccd425c9 |
| Decoder          | CLSID\_WICDdsDecoder     | 9053699f-a341-429d-9e90ee437cf80c73 |
| Encoder          | CLSID\_WICDdsEncoder     | a61dde94-66ce-4ac1-881b71680588895e |



 

## Pixel Format Support

Note that the DDS format supports any valid [**DXGI\_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) value. However, the WIC DDS codec only supports decoding and encoding files containing the following formats:

-   DXGI\_FORMAT\_BC1\_UNORM
-   DXGI\_FORMAT\_BC2\_UNORM
-   DXGI\_FORMAT\_BC3\_UNORM

## Encoding

The WIC encoding APIs are designed to be codec-independent and therefore image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

The DDS file format has unique requirements that arise from its support for concepts such as mipmaps and texture arrays. To fully exercise control over DDS image encoding, you should use the [**IWICDdsEncoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicddsencoder) interface to set DDS-specific encoding parameters.

## Decoding

The WIC decoding APIs are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

## Block compressed data access

In addition to supporting the standard WIC codec interfaces, the DDS decoder provides direct access to the native block compressed data using the DDS-specific interfaces, [**IWICDdsDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicddsdecoder) and [**IWICDdsFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicddsframedecode). To use these interfaces, call QueryInterface off of [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) and [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode), respectively.

 

 
