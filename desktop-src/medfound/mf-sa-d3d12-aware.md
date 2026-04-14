---
description: Specifies whether a Media Foundation transform (MFT) supports Microsoft Direct3D 12.
title: MF_SA_D3D12_AWARE attribute (Mfd3d12.h)
ms.topic: reference
ms.date: 04/14/2026
---

# MF\_SA\_D3D12\_AWARE attribute

Specifies whether a Media Foundation transform (MFT) supports Microsoft Direct3D 12.

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute applies only to video MFTs. To query this attribute, call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) to get the MFT attribute store. If **GetAttributes** succeeds, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

-   If the attribute is nonzero, the MFT supports Direct3D 12 resources.
-   If this attribute is zero (**FALSE**), the MFT does not support Direct3D 12.

The default value of this attribute is **FALSE**. Treat this attribute as read-only. Do not change the value; the MFT will ignore any changes to the value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps \| UWP apps\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfd3d12.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md)
</dt> </dl>

 

 




