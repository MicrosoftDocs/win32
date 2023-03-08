---
title: samplepos (sm4.1 - asm)
description: Queries the position of a sample in a given shader resource view or in the rasterizer.
ms.assetid: 5A53B342-3A1D-4016-ABF2-CA6236D562C9
ms.topic: reference
ms.date: 05/31/2018
---

# samplepos (sm4.1 - asm)

Queries the position of a sample in a given shader resource view or in the rasterizer.



| samplepos dest\[.mask\], srcResource\[.swizzle\], sampleIndex |
|--------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                    |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the results of the operation.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] The shader resource.<br/>                         |
| <span id="sampleIndex"></span><span id="sampleindex"></span><span id="SAMPLEINDEX"></span>*sampleIndex*<br/> | \[in\] The index of the sample (scalar operand).<br/>                     |



 

## Remarks

This instruction returns the 2D sample position of sample *sampleIndex* for the given resource. It is valid only for resources that can be loaded using [**ld2dms**](ld2dms--sm4-1---asm-.md) unless the rasterizer is specified as *srcResource*.

*srcResource* can be a t\# register (a shader resource view) or a rasterizer register.

The instruction computes the floating point vector (Xposition, Yposition, 0, 0).

The swizzle on *srcResource* allows the returned values to be swizzled arbitrarily before they are written to the destination. The sample position is relative to the pixel's center, based on the Pixel Coordinate System.

If *sampleIndex* is out of bounds a zero vector is returned. If there is no resource bound to the specified slot, 0 is returned.

**samplepos** can be used for things like custom resolves in shader code.

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

 

 





