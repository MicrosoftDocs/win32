---
title: ftod (sm5 - asm)
description: Component-wise conversion from single-precision floating-point data to double-precision floating-point data.
ms.assetid: 95297556-41ED-4ED0-8F9A-16B7A440AF25
ms.topic: reference
ms.date: 05/31/2018
---

# ftod (sm5 - asm)

Component-wise conversion from single-precision floating-point data to double-precision floating-point data.



| ftod dest\[.mask\], \[-\]src\[.swizzle\], |
|-------------------------------------------|



 



| Item                                                            | Description                                          |
|-----------------------------------------------------------------|------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the converted data.<br/> |
| <span id="src"></span><span id="SRC"></span>*src*<br/> | \[in\] The data to be converted.<br/>          |



 

## Remarks

Each component of the source is converted from the single-precision representation to the double-precision representation.

The valid *dest* masks are .xy, .zw, and .xyzw. .xy receives the result of the first conversion, and .zw receives the result of the second conversion.

*dest* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).

*src* is a float vec2 across x and y (zw ignored) (post swizzle).

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

 

 





