---
title: deriv_rtx_fine (sm5 - asm)
description: Computes the rate of change of components. | deriv_rtx_fine (sm5 - asm)
ms.assetid: 5752C85B-2965-489C-BF27-968FAF5EAA52
ms.topic: reference
ms.date: 05/31/2018
---

# deriv\_rtx\_fine (sm5 - asm)

Computes the rate of change of components.



| deriv\_rtx\_fine\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], |
|--------------------------------------------------------------------------|



 



| Item                                                            | Description                                                    |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components in the operation.<br/>             |



 

## Remarks

This instruction computes the rate of change of contents of each float32 component of *src0* (post-swizzle), with regard to RenderTarget x direction (rtx) or RenderTarget y direction (see [deriv\_rty\_fine](deriv-rty-fine--sm5---asm-.md)). Each pixel in the 2x2 stamp gets a unique pair of x/y derivative calculations

The data in the current pixel shader invocation always participates in the calculation of the requested derivative. In the 2x2 pixel quad the current pixel falls within, the x derivative is the delta of the row of 2 pixels including the current pixel. The y derivative is the delta of the column of 2 pixels including the current pixel. There is no specification dictating how the 2x2 quads will be aligned or tiled over a primitive.

Derivatives are calculated at a fine level (unique calculation of the x/y derivative pair for each pixel in a 2x2 quad). This instruction and [deriv\_rty\_fine](deriv-rty-fine--sm5---asm-.md) are alternatives to [deriv\_rtx\_coarse](deriv-rtx-coarse--sm5---asm-.md) and [deriv\_rty\_coarse](deriv-rty-coarse--sm5---asm-.md). These \_coarse and \_fine derivative instructions are a replacement for **deriv\_rtx** These \_coarse and \_fine derivative instructions are a replacement for **deriv\_rtx** and **deriv\_rty** from previous shader models.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     |         |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





