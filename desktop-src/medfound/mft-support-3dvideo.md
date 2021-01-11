---
description: Specifies whether a Media Foundation transform (MFT) supports 3D stereoscopic video.
ms.assetid: DE96FD14-5C7E-4560-99AC-B1EBDA1EBB2B
title: MFT_SUPPORT_3DVIDEO attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_SUPPORT\_3DVIDEO attribute

Specifies whether a Media Foundation transform (MFT) supports 3D stereoscopic video.

## Data type

**BOOL** stored as **UINT32**

## Remarks

To query this attribute, call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) to get the global attribute store of the MFT. If **GetAttributes** succeeds, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

The default value of this attribute is **FALSE**. Treat this attribute as read-only. Do not change the value; the MFT will ignore any changes to the value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




