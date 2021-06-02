---
description: Specifies whether a deinterlaced video frame was derived from the upper field or the lower field.
ms.assetid: 3710ab94-afb3-44d3-a680-b4a716810ec1
title: MFSampleExtension_DerivedFromTopField attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_DerivedFromTopField attribute

Specifies whether a deinterlaced video frame was derived from the upper field or the lower field. This attribute applies to media samples.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

This attribute is valid for deinterlaced samples only. Set this attribute if the frame was deinterlaced by interpolating one of the fields.

If the value is **TRUE**, the lower field was interpolated from the upper field. If the value is **FALSE**, the upper field was interpolated from the lower field.

If the attribute is not set, the frame has not been deinterlaced. The frame is either a true progressive frame, or it is an interlaced frame.

This attribute is informational. A software deinterlacer could set this attribute. If this attribute is set, it provides a hint that you can recover the original field by dropping the interpolated scan lines. For example, if the attribute is **TRUE**, you can recover the original upper field by dropping the interpolated lower field.

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

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[Video Interlacing](video-interlacing.md)
</dt> </dl>

 

 




