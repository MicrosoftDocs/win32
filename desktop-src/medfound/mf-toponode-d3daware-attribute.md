---
description: Specifies whether the transform associated with a topology node supports DirectX Video Acceleration (DXVA).
ms.assetid: b9e393be-0bc0-4cf6-be44-e9e95339c434
title: MF_TOPONODE_D3DAWARE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_D3DAWARE attribute

Specifies whether the transform associated with a topology node supports DirectX Video Acceleration (DXVA).

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to transform nodes (**MF\_TOPOLOGY\_TRANSFORM\_NODE**).

Applications typically do not use this attribute directly. The Media Session sets this attribute on a transform node if the underlying Media Foundation transform has the [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md) attribute.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 




