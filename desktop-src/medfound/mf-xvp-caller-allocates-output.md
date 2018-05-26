---
Description: Specifies whether that the caller will allocate the textures used for output.
ms.assetid: CAB41B22-AD96-4932-9686-66474CB26C38
title: MF\_XVP\_CALLER\_ALLOCATES\_OUTPUT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_XVP\_CALLER\_ALLOCATES\_OUTPUT attribute

Specifies whether that the caller will allocate the textures used for output.

## Data type

**BOOL** stored as **UINT32**

## Remarks

If this attribute is **TRUE**, the video processor expect output textures to be allocated by the caller, even when operating in DirectX Video Acceleration (DXVA) mode. If this attribute is **FALSE**, the video processor will allocate the output textures when operating in DXVA mode, and will fail if caller provided output textures are provided.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getattributes?branch=master) on the video processor.
2.  Call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

Set the attribute before streaming begins.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




