---
title: umad (sm4 - asm)
description: Unsigned integer multiply and add.
ms.assetid: C0BE31CA-E01D-42C0-A660-E63727CE344F
ms.topic: reference
ms.date: 05/31/2018
---

# umad (sm4 - asm)

Unsigned integer multiply and add.



| umad dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\], src2\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                            | Description                                                             |
|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/>           |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The value to multiply with *src1*.<br/>                    |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The value to multiply with*src1*.<br/>                     |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The value to add to the product of *src0* and *src1*.<br/> |



 

## Remarks

Component-wise [umul](umul--sm4---asm-.md) of 32-bit operands *src0* and *src1* unsigned, keeping the low 32-bits, per component, of the result. This instruction then performs an [iadd](iadd--sm4---asm-.md) of *src2*, producing the correct low 32-bit (per component) result. The 32-bit results are placed in *dest*.

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

 

 





