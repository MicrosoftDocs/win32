---
title: udiv (sm4 - asm)
description: Unsigned integer divide.
ms.assetid: 87C81418-0F74-4C67-9D4A-DA952EFD008E
ms.topic: reference
ms.date: 05/31/2018
---

# udiv (sm4 - asm)

Unsigned integer divide.



| udiv destQUOT\[.mask\], destREM\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|------------------------------------------------------------------------------|



 



| Item                                                                                                   | Description                                                |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="destQUOT"></span><span id="destquot"></span><span id="DESTQUOT"></span>*destQUOT*<br/> | \[in\] The address of the resulting quotient.<br/>   |
| <span id="destREM"></span><span id="destrem"></span><span id="DESTREM"></span>*destREM*<br/>     | \[in\] The address of the resulting remainder.<br/>  |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                        | \[in\] The components to be divided by *src1*.<br/>  |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>                                        | \[in\] The components by whch to divide *src0*.<br/> |



 

## Remarks

This instruction performs a component-wise unsigned divide of the 32-bit operand *src0* by the 32-bit operand *src1*. The results of the divides are the 32-bit quotients placed in *destQUOT* and 32-bit remainders placed in *destREM*.

Divide by zero returns 0xffffffff for both quotient and remainder.

You can specifiy either *destQUOT* or *destREM* as NULL instead of specifying a register, if the quotient or remainder are not needed.

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

 

 





