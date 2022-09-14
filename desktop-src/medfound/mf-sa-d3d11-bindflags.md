---
description: Specifies the binding flags to use when allocating Microsoft Direct3D 11 surfaces for media samples.
ms.assetid: C3B475B1-9A44-47EA-BCE7-D3D0FB56DDAC
title: MF_SA_D3D11_BINDFLAGS attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SA\_D3D11\_BINDFLAGS attribute

Specifies the binding flags to use when allocating Microsoft Direct3D 11 surfaces for media samples.

## Data type

**UINT32**

## Remarks

The value of this attribute is a bitwise **OR** of [**D3D11\_BIND\_FLAG**](/windows/win32/api/d3d11/ne-d3d11-d3d11_bind_flag) flags.

### Microsoft Media Foundation Transforms

In this context, the attribute applies only when the Microsoft Media Foundation transform (MFT) returns **TRUE** for the [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md) attribute.

If an MFT supports Direct3D 11, this attribute provides a hint to the MFT when allocating Microsoft Direct3D surfaces for output. Set the attribute as follows:

1.  Call [**IMFTransform::GetOutputStreamAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreamattributes) to get the MFT attribute store.
2.  Call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

The Media Foundation pipeline sets the attribute before streaming starts. The MFT should attempt to honor the setting when it allocates surfaces. If that is not possible, the MFT can ignore the attribute, rather than failing the allocation.

In addition, if the MFT requires Direct3D surfaces for input, it can expose this attribute as a hint for how the input surfaces should be allocated. Query the attribute as follows:

1.  Call [**IMFTransform::GetInputStreamAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreamattributes) to get the input stream attributes.
2.  Call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

### Sample Allocator

This attribute can be set on the video sample allocator, in the [**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](/windows/desktop/api/mfidl/nf-mfidl-imfvideosampleallocatorex-initializesampleallocatorex) method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
