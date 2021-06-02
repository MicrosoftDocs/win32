---
description: Default surface stride, for an uncompressed video media type. Stride is the number of bytes needed to go from one row of pixels to the next.
ms.assetid: 71fda231-3497-49db-b82e-2fd79f6ade66
title: MF_MT_DEFAULT_STRIDE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_DEFAULT\_STRIDE attribute

Default surface stride, for an uncompressed video media type. Stride is the number of bytes needed to go from one row of pixels to the next.

## Data type

**UINT32**

Treat as a **INT32** value.

## Remarks

The attribute value is stored as a **UINT32**, but should be cast to a 32-bit signed integer value. Stride can be negative.

Stride is positive for top-down images, and negative for bottom-up images.

This attribute gives the stride for a *contiguous* representation of the image in memory; that is, a representation with no additional padding bytes after each row. If a media buffer supports the [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer) interface, use the [**IMF2DBuffer::Lock2D**](/windows/desktop/api/mfobjects/nf-mfobjects-imf2dbuffer-lock2d) method to get the actual stride of the surface, which might include extra padding bytes.

For more information about surface stride, see [Image Stride](image-stride.md).

For an example of how to calculate the default stride, see [Uncompressed Video Buffers](uncompressed-video-buffers.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Image Stride](image-stride.md)
</dt> </dl>

 

 




