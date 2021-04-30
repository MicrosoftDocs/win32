---
description: The minimum frame rate that is supported by a video capture device, in frames per second.
ms.assetid: d3725796-f683-4ca1-a37f-22c40fff0b76
title: MF_MT_FRAME_RATE_RANGE_MIN attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_FRAME\_RATE\_RANGE\_MIN attribute

The minimum frame rate that is supported by a video capture device, in frames per second.

## Data type

**UINT64**

## Get/set

To get this attribute, call [**MFGetAttributeRatio**](/windows/desktop/api/mfapi/nf-mfapi-mfgetattributeratio).

To set this attribute, call [**MFSetAttributeRatio**](/windows/desktop/api/mfapi/nf-mfapi-mfsetattributeratio).

## Remarks

The frame rate is expressed as a ratio. The upper 32 bits of the attribute value contain the numerator, and the lower 32 bits contain the denominator. For example, if the frame rate is 30 frames per second (fps), the ratio is 30/1.

If the capture device reports a minimum frame rate, the media source sets this attribute on the media type. The maximum frame rate is given in the [MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md) attribute. The device is not guaranteed to support every increment within this range.

To set the device's frame rate, first modify the value of the [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md) attribute on the media type. Then set the media type on the media source.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[How to Set the Video Capture Frame Rate](how-to-set-the-video-capture-frame-rate.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md)
</dt> </dl>

 

 




