---
description: When a media source requests a new playback rate, this attribute specifies whether the source also requests thinning. For a definition of thinning, see About Rate Control.
ms.assetid: 42b6d0b3-e5af-4a48-969c-53628d1b7c31
title: MF_EVENT_DO_THINNING attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_DO\_THINNING attribute

When a media source requests a new playback rate, this attribute specifies whether the source also requests thinning. For a definition of thinning, see [About Rate Control](about-rate-control.md).

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute is used with the [MESourceRateChangeRequested](mesourceratechangerequested.md) event. If the value is **TRUE**, the media source is requesting a switch to thinned playback.

The default value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Event Attributes](event-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> </dl>

 

 




