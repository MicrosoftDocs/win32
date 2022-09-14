---
title: deriv_rty (sm4 - asm)
description: Render-target y equivalent of deriv\_rtx.
ms.assetid: F78F2DBD-9428-4F34-85AD-276DF54C52D1
ms.topic: reference
ms.date: 05/31/2018
---

# deriv\_rty (sm4 - asm)

Render-target y equivalent of [deriv\_rtx](deriv-rtx--sm4---asm-.md).



| deriv\_rty\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], |
|--------------------------------------------------------------------|



 



| Item                                                            | Description                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The component in the operation.<br/>             |



 

## Remarks

Only a single x,y derivative pair is computed for each 2x2 stamp of pixels.

This operation is hardware dependent.

Reference rasterizer implementation for triangles:

-   Pixel Shader always runs Shader over 2x2 quad of pixels in lockstep (even through flow control, masking disabled pixels).
-   Quads always have even numbered pixel coordinates (both x and y) for top-left pixel.
-   Dummy pixels run off primitive if primitive is too small to fill a 2x2 quad.
-   [deriv\_rtx](deriv-rtx--sm4---asm-.md) is computed by first choosing 2 pixels: the current pixel and the other pixel with the same y coordinate from the quad. Then, the result is calculated as: *src0*(odd x pixel) - *src0*(even x pixel) \[per-component\]
-   **deriv\_rty** is computed by first choosing 2 pixels: the current pixel and the other pixel with the same x coordinate from the quad. Then, the result is calculated as: *src0*(odd y pixel) - *src0*(even y pixel) \[per-component\]

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
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





