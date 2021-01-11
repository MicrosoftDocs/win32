---
description: Specifies the rate-control mode for an H.264 video stream.
ms.assetid: EA8EFEFA-9292-4D7B-BF5D-DE5239BB1D2C
title: MF_MT_H264_RATE_CONTROL_MODES attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_H264\_RATE\_CONTROL\_MODES attribute

Specifies the rate-control mode for an H.264 video stream.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)

## Remarks

This attribute applies to media types for H.264 streams transmitted over USB. The value corresponds to the **bmRateControlModes** field in the UVC 1.2 H.264 probe/commit control.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




