---
description: Specifies whether the IMFTransform is using hardware DRM.
title: MFT_USING_HARDWARE_DRM (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_USING\_HARDWARE\_DRM attribute

Specifies whether the IMFTransform is using hardware DRM.

## Data type

**UINT32** (treated as **BOOL**)

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMTransfrom**](/windows/win32/api/mftransform/nn-mftransform-imftransform)

## Remarks

If an MFT decrypter specifies this attribute set to 1, then it is using hardware DRM. If an MFT decrypter specifies this attribute set to 0, then it is not using hardware DRM. If an MFT decrypter does not specify this attribute or specifies it with a different value, then it does not (or is unable to) indicate whether it is using hardware DRM.


The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update   <br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt>  <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




