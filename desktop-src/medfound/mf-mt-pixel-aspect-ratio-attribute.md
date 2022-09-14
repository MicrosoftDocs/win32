---
description: Pixel aspect ratio for a video media type.
ms.assetid: e82cdd22-7d3f-4858-befd-43fa6f9f915e
title: MF_MT_PIXEL_ASPECT_RATIO attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_PIXEL\_ASPECT\_RATIO attribute

Pixel aspect ratio for a video media type.

## Data type

**UINT64**

## Remarks

The upper 32 bits contain the numerator of the pixel aspect ratio and the lower 32 bits contain the denominator. The numerator is the horizontal component of the aspect ratio; the denominator is the vertical component.

To set this attribute, use the [**MFSetAttributeRatio**](/windows/desktop/api/mfapi/nf-mfapi-mfsetattributeratio) function. To get this attribute, use the [**MFGetAttributeRatio**](/windows/desktop/api/mfapi/nf-mfapi-mfgetattributeratio) function.

The pixel aspect ratio describes the shape of the pixels in the displayed video image. Set this attribute if the image has non-square pixels. To display correctly on a display device with square pixels, the image must be scaled by the inverse of the image's pixel aspect ratio.

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

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Picture Aspect Ratio](picture-aspect-ratio.md)
</dt> </dl>

 

 




