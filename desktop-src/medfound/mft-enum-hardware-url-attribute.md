---
Description: Contains the symbolic link for a hardware-based Media Foundation transform (MFT).
ms.assetid: 7e153051-a167-4ff7-8178-b290d8a1345e
title: MFT\_ENUM\_HARDWARE\_URL\_Attribute attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_ENUM\_HARDWARE\_URL\_Attribute attribute

Contains the symbolic link for a hardware-based Media Foundation transform (MFT).

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master).

To set this attribute, call [**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Remarks

This attribute is supported by hardware-based MFTs. The value of the attribute is the symbolic link for the device driver. This attribute is also set on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers allocated by the [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master) function, when those pointers represent hardware-based MFTs.

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

 

 




