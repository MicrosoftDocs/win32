---
title: imad (sm4 - asm)
description: Signed integer multiply and add.
ms.assetid: 1C24AF49-AA32-4D3A-8478-C9BAC4FE7D77
ms.topic: reference
ms.date: 05/31/2018
---

# imad (sm4 - asm)

Signed integer multiply and add.



| imad dest\[.mask\], \[-\]src0\[.swizzle\], \[-\]src1\[.swizzle\], \[-\]src2\[.swizzle |
|---------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                         |
|-----------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation.<br/>                      |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] Value to multiply with *src1*.<br/>                    |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] Value to multiply with *src0*.<br/>                    |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] Value to add to the product of *src0* and *src1*.<br/> |



 

## Remarks

Component-wise [imul](imul--sm4---asm-.md) of 32-bit operands *src0* and *src1* (signed), keeping low 32-bits (per component) of the result, followed by an [iadd](iadd--sm4---asm-.md) of *src2*, producing the correct low 32-bit (per component) result. The 32-bit results are placed in *dest*.

Optional negate modifier on source operands takes 2's complement before performing arithmetic operation.

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

 

 





