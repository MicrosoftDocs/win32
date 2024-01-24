---
title: dmul (sm5 - asm)
description: Component-wise double-precision multiply.
ms.assetid: 53AE27BE-2F4B-4C55-B496-D7122C00DC52
ms.topic: reference
ms.date: 05/31/2018
---

# dmul (sm5 - asm)

Component-wise double-precision multiply.



| dmul\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\] |
|---------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                        |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> *dest* = *src0* \* *src1*<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to multiply with *src1*.<br/>                                          |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to multiply with *src0*.<br/>                                          |



 

## Remarks

The valid swizzles for the source parameters are .xyzw, .xyxy, .zwxy, .zwzw. The valid *dest* masks are .xy, .zw, and .xyzw. The following *src* mappings are post-swizzle:

-   *dest* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src0* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src1* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).

The following table shows the results obtained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs.

F means finite-real number.



| **src0 src1->** | **-inf** | **-F** | **-1.0** | **-0** | **+0** | **+1.0** | **+F** | **+inf** | **NaN** |
|--------------------|----------|--------|----------|--------|--------|----------|--------|----------|---------|
| **-inf**           | +inf     | +inf   | +inf     | NaN    | NaN    | -inf     | -inf   | -inf     | NaN     |
| **-F**             | +inf     | +F     | -src0    | +0     | -0     | src0     | -F     | -inf     | NaN     |
| **-1.0F**          | +inf     | -src1  | +1.0     | +0     | -0     | -1.0     | -src1  | -inf     | NaN     |
| **-0**             | NaN      | +0     | +0       | +0     | -0     | -0       | -0     | NaN      | NaN     |
| **+0**             | NaN      | -0     | -0       | -0     | +0     | +0       | +0     | NaN      | NaN     |
| **+1.0**           | -inf     | src1   | -1.0     | -0     | +0     | +1       | src1   | +inf     | NaN     |
| **+F**             | -inf     | -F     | -src0    | -0     | +0     | src0     | +F     | +inf     | NaN     |
| **+inf**           | -inf     | -inf   | -inf     | NaN    | NaN    | +inf     | +inf   | +inf     | NaN     |
| **NaN**            | NaN      | NaN    | NaN      | NaN    | NaN    | NaN      | NaN    | NaN      | NaN     |



 

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

 

 





