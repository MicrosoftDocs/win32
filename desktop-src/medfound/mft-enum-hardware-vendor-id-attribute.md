---
description: Specifies the vendor ID for a hardware-based Microsoft Media Foundation.
ms.assetid: AA31639F-EF70-4454-AC61-60755CAA684A
title: MFT_ENUM_HARDWARE_VENDOR_ID_Attribute attribute
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_ENUM\_HARDWARE\_VENDOR\_ID\_Attribute attribute

Specifies the vendor ID for a hardware-based Microsoft Media Foundation transform (MFT).

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Remarks

This attribute is informational and optional.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mftransform.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Hardware MFTs](hardware-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




