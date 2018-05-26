---
Description: Contains an IMFFieldOfUseMFTUnlock pointer, which can be used to unlock a Media Foundation transform (MFT). The IMFFieldOfUseMFTUnlock interface is used to unlock an MFT that has field-of-use restrictions.
ms.assetid: 7f48967e-375a-4019-b14f-2f457b616cc0
title: MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute

Contains an [**IMFFieldOfUseMFTUnlock**](/windows/win32/mfidl/nn-mfidl-imffieldofusemftunlock?branch=master) pointer, which can be used to unlock a Media Foundation transform (MFT). The **IMFFieldOfUseMFTUnlock** interface is used to unlock an MFT that has field-of-use restrictions.

## Data type

**[**IMFFieldOfUseMFTUnlock**](/windows/win32/mfidl/nn-mfidl-imffieldofusemftunlock?branch=master)\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

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

[**MFCreateTransformActivate**](/windows/win32/mftransform/nf-mftransform-mfcreatetransformactivate?branch=master)
</dt> </dl>

 

 




