---
Description: Contains the display name for a hardware-based Media Foundation transform (MFT).
ms.assetid: 8f2634e8-6bdd-463a-893a-6dc616c8333d
title: MFT\_FRIENDLY\_NAME\_Attribute attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_FRIENDLY\_NAME\_Attribute attribute

Contains the display name for a hardware-based Media Foundation transform (MFT).

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master).

To set this attribute, call [**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Remarks

This attribute is supported by hardware-based MFTs. It is also set on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers allocated by the [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master) function, when those pointers represent hardware-based MFTs.

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

 

 




