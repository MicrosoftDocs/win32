---
description: This topic provides information about the native GIF codec available through the Windows Imaging Component (WIC).
ms.assetid: CAEC8F92-8971-42B4-BED8-A6A93522D11E
title: GIF Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# GIF Format Overview

This topic provides information about the native GIF codec available through the Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



|  Component             | Description                           |
|------------------------|---------------------------------------|
| Formal Name(s)         | Graphics Interchange Format 89a (GIF) |
| File Name Extension(s) | gif                                   |
| MIME type              | image/gif                             |
| Specification Support  | GIF Specification 89a/89m             |



 

The following table lists the GUIDs used to identify the native GIF codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatGif | 1f8a5601-7d4d-4cbd-9c821bc8d4eeb9a5 |
| Decoder          | CLSID\_WICGifDecoder     | 381dda3c-9ce9-4834-a23e1f98f8fc52be |
| Encoder          | CLSID\_WICGifEncoder     | 114f5598-0b22-40a0-86a1c83ea495adbd |



 

## Encoding

The WIC encoding API are designed to be codec-independent and image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface . For more information about using the **IPropertyBag2** interface for WIC encoding , see the [Encoding Overview](-wic-creating-encoder.md).

The GIF encoder does not support any basic WIC options and does not provide custom encoder options. If an encoder option is in the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) option list, it is ignored.

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 
