---
Description: 'Contains the symbolic link for a hardware-based Media Foundation transform (MFT).'
ms.assetid: '7e153051-a167-4ff7-8178-b290d8a1345e'
title: 'MFT\_ENUM\_HARDWARE\_URL\_Attribute attribute'
---

# MFT\_ENUM\_HARDWARE\_URL\_Attribute attribute

Contains the symbolic link for a hardware-based Media Foundation transform (MFT).

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Remarks

This attribute is supported by hardware-based MFTs. The value of the attribute is the symbolic link for the device driver. This attribute is also set on the [**IMFActivate**](imfactivate.md) pointers allocated by the [**MFTEnumEx**](mftenumex.md) function, when those pointers represent hardware-based MFTs.

The symbolic link should be considered an opaque string. To get the display name for a device, query the [MFT\_FRIENDLY\_NAME](mft-friendly-name-attribute.md) attribute.

Software MFTs should not have this attribute set.

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

[Hardware MFTs](hardware-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




