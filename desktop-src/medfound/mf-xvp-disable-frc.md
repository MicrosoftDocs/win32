---
description: Disables frame-rate conversion in the Video Processor MFT.
ms.assetid: 98AA7B3A-281C-427D-805E-5C4EE1EFAE21
title: MF_XVP_DISABLE_FRC attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_XVP\_DISABLE\_FRC attribute

Disables frame-rate conversion in the [**Video Processor MFT**](video-processor-mft.md).

## Data type

**BOOL** stored as **UINT32**

## Remarks

If this attribute is **TRUE**, the video processor will not perform frame-rate conversion. By default, the video processor will convert the frame rate to match the output media type.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) on the video processor.
2.  Call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

Set the attribute before streaming begins.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




