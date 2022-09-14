---
title: umul (sm4 - asm)
description: Unsigned integer multiply.
ms.assetid: C84AF349-32E6-40C4-9973-BCFA73EFBF0B
ms.topic: reference
ms.date: 05/31/2018
---

# umul (sm4 - asm)

Unsigned integer multiply.



| umul destHI\[.mask\], destLO\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|---------------------------------------------------------------------------|



 



| Item                                                                                           | Description                                                      |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="destHI"></span><span id="desthi"></span><span id="DESTHI"></span>*destHI*<br/> | \[in\] The high 32 bits of the result, per component.<br/> |
| <span id="destLO"></span><span id="destlo"></span><span id="DESTLO"></span>*destLO*<br/> | \[in\] The low 32 bits of the result, per component.<br/>  |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                | \[in\] The components by which to multiply *src1*.<br/>    |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>                                | \[in\] The components by which to multiply *src0*.<br/>    |



 

## Remarks

This instruction performs a component-wise multiply of unsigned 32-bit operands *src0* and *src1*, producing the correct full 64-bit result per component. The low 32 bits per component are placed in *destLO*. The high 32 bits per component are placed in *destHI*.

You can specify either *destHI* or *destLO* as NULL instead of specifying a register if the high or low 32 bits of the 64-bit result are not needed.

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

 

 





