---
title: max (sm4 - asm)
description: Component-wise float maximum.
ms.assetid: 005468AA-577E-441F-ACD5-37A691E62CDD
ms.topic: reference
ms.date: 05/31/2018
---

# max (sm4 - asm)

Component-wise float maximum.



| max\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\], |
|---------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                               |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation. <br/> *dest* = *src0* >= *src1* ? *src0* : *src1*<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to compare to *src1*.<br/>                                                    |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to compare to *src0*.<br/>                                                    |



 

## Remarks

>= is used instead of > so that if min(x,y) = x then max(x,y) = y.

NaN has special handling. If one source operand is NaN, then the other source operand is returned and the choice is made per-component. If both are NaN, any NaN representation is returned.

Denorms are flushed with sign preserved before the comparison. However, the result written to *dest* may or may not be denorm flushed.

The following table shows the results obtained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs. F means finite real number.



| **src0 src1->** | **-inf** | **F**        | **+inf** | **NaN** |
|--------------------|----------|--------------|----------|---------|
| **-inf**           | -inf     | src1         | +inf     | -inf    |
| **F**              | src0     | src0 or src1 | +inf     | src0    |
| **+inf**           | +inf     | +inf         | +inf     | +inf    |
| **NaN**            | -inf     | src1         | +inf     | NaN     |



 

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

 

 





