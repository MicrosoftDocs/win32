---
description: Specifies the maximum video bit rate for the Digital Living Network Alliance (DLNA) media sink.
ms.assetid: 5805f930-6cbd-4089-a052-522b4d152cc1
title: MF_MP2DLNA_VIDEO_BIT_RATE attribute (Mfmp2dlna.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MP2DLNA\_VIDEO\_BIT\_RATE attribute

Specifies the maximum video bit rate for the Digital Living Network Alliance (DLNA) media sink.

## Data type

**UINT32**

The value is the target maximum bit rate for the encoded video stream, in bits per second. The maximum value is 9800000 (9.8 Mbps), which is also the default value.

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

To set this attribute on the DLNA media sink, query the media sink for the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface. Set the attribute before streaming begins.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmp2dlna.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




