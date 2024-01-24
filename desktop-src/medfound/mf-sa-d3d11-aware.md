---
description: Specifies whether a Media Foundation transform (MFT) supports Microsoft Direct3D 11.
ms.assetid: 23482B8A-58F3-4B39-9C6D-54EC27D36C01
title: MF_SA_D3D11_AWARE attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SA\_D3D11\_AWARE attribute

Specifies whether a Media Foundation transform (MFT) supports Microsoft Direct3D 11.

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute applies only to video MFTs. To query this attribute, call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) to get the MFT attribute store. If **GetAttributes** succeeds, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

-   If the attribute is nonzero, the client can give the MFT a pointer to the [**IMFDXGIDeviceManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgidevicemanager) interface before streaming starts. To do so, the client sends the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message to the MFT. The client is not required to send this message.
-   If this attribute is zero (**FALSE**), the MFT does not support Direct3D 11, and the client should not send the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message to the MFT.

The default value of this attribute is **FALSE**. Treat this attribute as read-only. Do not change the value; the MFT will ignore any changes to the value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Supporting Direct3D 11 Video Decoding in Media Foundation](supporting-direct3d-11-video-decoding-in-media-foundation.md)
</dt> </dl>

 

 




