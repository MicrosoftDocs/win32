---
title: ftou (sm4 - asm)
description: Floating point to unsigned integer conversion.
ms.assetid: 0E3E090B-72C0-4CED-AFA5-2DDCF67D7263
ms.topic: reference
ms.date: 05/31/2018
---

# ftou (sm4 - asm)

Floating point to unsigned integer conversion.



| ftou dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|----------------------------------------------------|



 



| ftoi dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|----------------------------------------------------|



 



| Item                                                            | Description                                                    |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation. <br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The value to convert.<br/>                        |



 

## Remarks

The conversion is performed per-component. Rounding is always performed towards zero, following the C convention for casts from float to int.

Applications that require different rounding semantics can invoke the **round** instructions before casting to integer.

Inputs are clamped to the range \[0.0f ... 4294967295.999f\] prior to conversion, and input NaN values produce a zero result.

Optional negate and absolute value modifiers are applied to the source values before conversion.

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

 

 





