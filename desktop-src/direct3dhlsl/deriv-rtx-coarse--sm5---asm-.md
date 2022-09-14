---
title: deriv_rtx_coarse (sm5 - asm)
description: Computes the rate of change of components. | deriv_rtx_coarse (sm5 - asm)
ms.assetid: 57743BB2-251C-4EA7-BDA9-70B2ECEE3B3F
ms.topic: reference
ms.date: 05/31/2018
---

# deriv\_rtx\_coarse (sm5 - asm)

Computes the rate of change of components.



| deriv\_rtx\_coarse\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], |
|----------------------------------------------------------------------------|



 



| Item                                                            | Description                                                    |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components in the operation.<br/>             |



 

## Remarks

This instruction computes the rate of change of contents of each float32 component of *src0* (post-swizzle), with regard to RenderTarget x direction (rtx) or RenderTarget y direction (see [deriv\_rty\_coarse](deriv-rty-coarse--sm5---asm-.md)). Only a single x,y derivative pair is computed for each 2x2 stamp of pixels.

The data in the current pixel shader invocation may or may not participate in the calculation of the requested derivative, because the derivative will be calculated only once per 2x2 quad. For example, the x derivative could be a delta from the top row of pixels, and the y direction ([deriv\_rty\_coarse](deriv-rty-coarse--sm5---asm-.md)) could be a delta from the left column of pixels. The exact calculation is up to the hardware vendor. There is also no specification dictating how the 2x2 quads will be aligned or tiled over a primitive.

Derivatives are calculated at a coarse level, once per 2x2 pixel quad. This instruction and [deriv\_rty\_coarse](deriv-rty-coarse--sm5---asm-.md) are alternatives to [deriv\_rtx\_fine](deriv-rtx-fine--sm5---asm-.md) and [deriv\_rty\_fine](deriv-rty-fine--sm5---asm-.md). These \_coarse and \_fine derivative instructions are a replacement for **deriv\_rtxderiv\_rty** from previous shader models .

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

 

 





