---
Description: 'Contains an IMFFieldOfUseMFTUnlock pointer, which can be used to unlock a Media Foundation transform (MFT). The IMFFieldOfUseMFTUnlock interface is used to unlock an MFT that has field-of-use restrictions.'
ms.assetid: '7f48967e-375a-4019-b14f-2f457b616cc0'
title: 'MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute'
---

# MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute

Contains an [**IMFFieldOfUseMFTUnlock**](imffieldofusemftunlock.md) pointer, which can be used to unlock a Media Foundation transform (MFT). The **IMFFieldOfUseMFTUnlock** interface is used to unlock an MFT that has field-of-use restrictions.

## Data type

**[**IMFFieldOfUseMFTUnlock**](imffieldofusemftunlock.md)\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

For more information about this attribute, see [Field of Use Restrictions](field-of-use-restrictions.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Field of Use Restrictions](field-of-use-restrictions.md)
</dt> <dt>

[**MFCreateTransformActivate**](mfcreatetransformactivate.md)
</dt> </dl>

 

 




