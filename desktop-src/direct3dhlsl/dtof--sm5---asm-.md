---
title: dtof (sm5 - asm)
description: Component-wise conversion from double-precision floating-point data to single-precision floating-point data.
ms.assetid: 1D2EF05C-06EF-44F0-AA0F-22D3057FF43E
ms.topic: reference
ms.date: 05/31/2018
---

# dtof (sm5 - asm)

Component-wise conversion from double-precision floating-point data to single-precision floating-point data.



| dtof dest\[.mask\], \[-\]src0\[.swizzle\], |
|-------------------------------------------|



 



| Item                                                            | Description                                          |
|-----------------------------------------------------------------|------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the converted data.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The data to be converted.<br/>          |



 

## Remarks

Each component of the source is converted from the double-precision representation to the single-precision representation using round-to-nearest-even rounding.

The valid swizzles for the source parameter are .xyzw, .xyxy, .zwxy, .zwzw.

The valid *dest* masks are any one or two components. That is: .x, .y, .z, .w, .xy, .xz, .xw, .yz, .yw, .zw The result of the first conversion goes to the first component in the mask, and the result of the second component goes in the second component in the mask, if present.

*dest* components are float32.

*src0* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB) post swizzle.

For float32<->double conversions, implementations may either honor float32 denorms or may flush them.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

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

 

 





