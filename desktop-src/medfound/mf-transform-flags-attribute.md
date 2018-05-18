---
Description: 'Contains flags for a Media Foundation transform (MFT) activation object.'
ms.assetid: 'de377132-19b0-4c8c-882e-193c31420739'
title: 'MF\_TRANSFORM\_FLAGS\_Attribute attribute'
---

# MF\_TRANSFORM\_FLAGS\_Attribute attribute

Contains flags for a Media Foundation transform (MFT) activation object.

## Data type

**UINT32**

The value is a bitwise **OR** of flags from the [**\_MFT\_ENUM\_FLAG**](-mft-enum-flag.md) enumeration.

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute is set on the [**IMFActivate**](imfactivate.md) pointers returned by the [**MFTEnumEx**](mftenumex.md) function. The attribute contains flags that describe the MFT.

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

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




