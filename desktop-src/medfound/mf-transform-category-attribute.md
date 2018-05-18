---
Description: 'Specifies the category for a Media Foundation transform (MFT).'
ms.assetid: 'cebd64ea-b20f-4ccc-805f-0deab3096bc3'
title: 'MF\_TRANSFORM\_CATEGORY\_Attribute attribute'
---

# MF\_TRANSFORM\_CATEGORY\_Attribute attribute

Specifies the category for a Media Foundation transform (MFT).

## Data type

**GUID**

For a list of possible values, see [**MFT\_CATEGORY**](mft-category.md).

## Get/set

To get this attribute, call [**IMFAttributes::GetGUID**](imfattributes-getguid.md).

To set this attribute, call [**IMFAttributes::SetGUID**](imfattributes-setguid.md).

## Remarks

This attribute is set on the [**IMFActivate**](imfactivate.md) pointers returned by the [**MFTEnumEx**](mftenumex.md) function.

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

 

 




