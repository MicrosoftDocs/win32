---
description: Specifies whether a Media Foundation transform (MFT) supports DirectX Video Acceleration (DXVA). This attribute applies only to video MFTs.
ms.assetid: db6a8b20-fda0-4ffe-b1b5-a77b7604d290
title: MF_SA_D3D_AWARE attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SA\_D3D\_AWARE attribute

Specifies whether a Media Foundation transform (MFT) supports DirectX Video Acceleration (DXVA). This attribute applies only to video MFTs.

## Data type

**BOOL** stored as **UINT32**

## Remarks

To query this attribute, call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) to get the global attribute store of the MFT. If **GetAttributes** succeeds, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

This attribute tells the client whether the MFT can use Direct3D 9 video:

-   If the attribute is nonzero, the client can give the MFT a pointer to the [**IDirect3DDeviceManager9**](/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9) interface before streaming starts. To do so, the client sends the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message to the MFT. The client is not required to send this message.
-   If this attribute is zero (**FALSE**), the MFT does not support Direct3D 9 video, and the client should not send the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message to the MFT.

The default value of this attribute is **FALSE**. Treat this attribute as read-only. Do not change the value; the MFT will ignore any changes to the value.

For more information about implementing this attribute in a custom MFT, see [Direct3D-Aware MFTs](direct3d-aware-mfts.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples

The following code tests whether an MFT supports DXVA.


```C++
// Returns TRUE is an MFT supports DirectX Video Acceleration.

BOOL IsTransformD3DAware(IMFTransform *pMFT)
{
    BOOL bD3DAware = FALSE;
    
    IMFAttributes *pAttributes = NULL;

    HRESULT hr = pMFT->GetAttributes(&pAttributes);
    if (SUCCEEDED(hr))
    {
        bD3DAware = MFGetAttributeUINT32(pAttributes, MF_SA_D3D_AWARE, FALSE);
        pAttributes->Release();
    }
    return bD3DAware;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Direct3D-Aware MFTs](direct3d-aware-mfts.md)
</dt> <dt>

[Supporting DXVA 2.0 in Media Foundation](supporting-dxva-2-0-in-media-foundation.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[MF\_TOPOLOGY\_DXVA\_MODE](mf-topology-dxva-mode.md)
</dt> </dl>

 

 




