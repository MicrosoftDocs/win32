---
description: Specifies whether topologies have a global start and stop time.
ms.assetid: 6810a22c-f091-423c-97dd-c04fdabdb9bb
title: MF_SESSION_GLOBAL_TIME attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SESSION\_GLOBAL\_TIME attribute

Specifies whether topologies have a global start and stop time.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

You can set this attribute when you create the media sesison by using the *pConfiguration* parameter of the [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) or [**MFCreatePMPMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepmpmediasession) function.

If this attribute is present and nonzero, then all topologies passed to the Media Session must have the [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md) and [**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md) attributes. These attributes specify the start and stop times for the topology relative to the entire presentation.

If this attribute is absent or **FALSE**, the topologies must not have the [**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md) or [**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md) attribute.

Use this attribute to create editing sequences. For more information, see [Sequence Presentation Times](sequence-presentation-times.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> <dt>

[Sequence Presentation Times](sequence-presentation-times.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**MF\_TOPOLOGY\_PROJECTSTART**](mf-topology-projectstart-attribute.md)
</dt> <dt>

[**MF\_TOPOLOGY\_PROJECTSTOP**](mf-topology-projectstop-attribute.md)
</dt> </dl>

 

 




