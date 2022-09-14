---
description: Specifies whether the audio streams in a presentation have a variable bit rate.
ms.assetid: 2bd7eee1-5a93-4bde-8b58-80b6395a094e
title: MF_PD_AUDIO_ISVARIABLEBITRATE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_AUDIO\_ISVARIABLEBITRATE attribute

Specifies whether the audio streams in a presentation have a variable bit rate.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies To

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)

## Remarks

This is an optional attribute for presentation descriptors. If the attribute is **TRUE** (nonzero), the presentation contains at least one variable-bit-rate (VBR) audio stream. If the attribute is **FALSE**, all of the audio streams have a constant bit rate.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




