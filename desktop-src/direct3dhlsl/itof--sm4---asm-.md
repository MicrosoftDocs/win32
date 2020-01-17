---
title: itof (sm4 - asm)
description: Signed integer to floating point conversion.
ms.assetid: 60652168-25FA-4084-8CC1-73F12984ECED
ms.topic: reference
ms.date: 05/31/2018
---

# itof (sm4 - asm)

Signed integer to floating point conversion.



| itof dest\[.mask\], \[-\]src0\[.swizzle\] |
|-------------------------------------------|



 



| Item                                                            | Description                                             |
|-----------------------------------------------------------------|---------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] Contains the result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] Contains the value to convert.<br/>        |



 

## Remarks

This signed integer-to-float conversion instruction assumes that *src0* contains a signed 32-bit integer 4-tuple. After the instruction executes, *dest* will contain a floating-point 4-tuple.

The conversion is performed per-component.

When an integer input value is too large in magnitude to be represented exactly in the floating point format, rounding to nearest even mode is strongly recommended but not required.

The optional negate modifier on source operand takes 2's complement before performing arithmetic operation.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

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

 

 





