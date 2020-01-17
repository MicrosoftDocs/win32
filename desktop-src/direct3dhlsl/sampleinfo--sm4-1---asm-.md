---
title: sampleinfo (sm4.1 - asm)
description: Queries the number of samples in a given shader resource view or in the rasterizer.
ms.assetid: 1F0968D7-01E9-4213-9F83-172B88374C3C
ms.topic: reference
ms.date: 05/31/2018
---

# sampleinfo (sm4.1 - asm)

Queries the number of samples in a given shader resource view or in the rasterizer.



| \[\_uint\] dest\[.mask\], srcResource\[.swizzle\] |
|---------------------------------------------------|



 



| Item                                                                                                               | Description                                                    |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the results of the operation.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] The shader resource.<br/>                         |



 

## Remarks

This instruction returns the number of samples for the given resource or the rasterizer. It is valid only for resources that can be loaded using [**ld2dms**](ld2dms--sm4-1---asm-.md) unless the rasterizer is specified as *srcResource*. *srcResource* could be a t\# register (a shader resource view) or a rasterizer register.

The instruction computes the vector (SampleCount,0,0,0).

The swizzle on *srcResource* allows the returned values to be swizzled arbitrarily before they are written to the destination. The returned value is floating point, unless the \_uint modifier is used, in which case the returned value is integer. If there is no resource bound to the specified slot, 0 is returned.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| X             | X               | x            |



 

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

 

 





