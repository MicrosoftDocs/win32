---
title: lod (sm4.1 - asm)
description: Returns the level of detail (LOD) that would be used for texture filtering.
ms.assetid: A5931203-8CD7-4FC9-A4A4-CA981F38C7A3
ms.topic: reference
ms.date: 05/31/2018
---

# lod (sm4.1 - asm)

Returns the level of detail (LOD) that would be used for texture filtering.



| lod dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], srcSampler |
|--------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                     |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the results.<br/>   |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] A set of texture coordinates.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register.<br/>           |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>     | \[in\] A sampler register.<br/>           |



 

## Remarks

This behaves like the [sample](sample--sm4---asm-.md) instruction, but a filtered sample is not generated. The instruction computes the following vector (ClampedLOD, NonClampedLOD, 0, 0). NonClampedLOD is a computed LOD value that ignores any clamping from either the sampler or the texture (ie: it can return negative values.) ClampedLOD is a computed LOD value that would be used by the actual **sample** instruction. The swizzle on *srcResource* allows the returned values to be swizzled arbitrarily before they are written to the destination.

If there is no resource bound to the specified slot, 0 is returned.

If the sampler is using anisotropic filtering the LOD should correspond to the fractional mip level based on the smaller axis of the elliptical footprint.

This is valid for the following texture types: Texture1D, Texture2D, Texture3D and TextureCube.

The **lod** instruction is not defined when used with a sampler that specifies point mip filtering, specifically, any D3D10\_FILTER enum that ends in MIP\_POINT. (An example of this would be D3D10\_FILTER\_MIN\_MAG\_MIP\_POINT.)

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               |                 | x            |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





