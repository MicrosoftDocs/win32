---
title: dmax (sm5 - asm)
description: Component-wise double-precision maximum.
ms.assetid: 34ED8B34-2592-4BBB-BCF0-F2222E4D51D9
ms.topic: reference
ms.date: 05/31/2018
---

# dmax (sm5 - asm)

Component-wise double-precision maximum.



| dmax\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\] |
|---------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                                                                                                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results of the operation.<br/> *dest* = *src0* >= *src1* ? *src0* : *src1*<br/> >= is used instead of > so that if min(x,y) = x then max(x,y) = y. <br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The value to compare with *src1*.<br/>                                                                                                                                                           |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The value to compare with *src0*.<br/>                                                                                                                                                           |



 

## Remarks

NaN has special handling. If one source operand is NaN, then the other source operand is returned. The choice is made per-component. If both are NaN, any NaN representation is returned.

The valid swizzles for the source parameters are .xyzw, .xyxy, .zwxy, .zwzw. The valid *dest* masks are .xy, .zw, and .xyzw. The following *src* mappings are post-swizzle:

-   *dest* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src0* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src1* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).

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

 

 





