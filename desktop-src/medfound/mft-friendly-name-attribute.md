---
Description: 'Contains the display name for a hardware-based Media Foundation transform (MFT).'
ms.assetid: '8f2634e8-6bdd-463a-893a-6dc616c8333d'
title: 'MFT\_FRIENDLY\_NAME\_Attribute attribute'
---

# MFT\_FRIENDLY\_NAME\_Attribute attribute

Contains the display name for a hardware-based Media Foundation transform (MFT).

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Remarks

This attribute is supported by hardware-based MFTs. It is also set on the [**IMFActivate**](imfactivate.md) pointers allocated by the [**MFTEnumEx**](mftenumex.md) function, when those pointers represent hardware-based MFTs.

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

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




