---
title: iadd (sm4 - asm)
description: Integer addition.
ms.assetid: EF78EA65-DC16-469A-9E45-52844FF4BD93
ms.topic: reference
ms.date: 05/31/2018
---

# iadd (sm4 - asm)

Integer addition.



| iadd dest\[.mask\], \[-\]src0\[.swizzle\], \[-\]src1\[.swizzle\] |
|------------------------------------------------------------------|



 



| Item                                                            | Description                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The number to be added to *src1*.<br/>           |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The number to be added to *src0*.<br/>           |



 

## Remarks

Component-wise add of 32-bit operands *src0* and *src1*, placing the correct 32-bit result in *dest*. No carry or borrow beyond the 32-bit values of each component is performed, so this instruction is not sensitive to the signed-ness of its operands.

Optional negate modifier on source operands takes 2's complement before performing operation.

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

 

 





