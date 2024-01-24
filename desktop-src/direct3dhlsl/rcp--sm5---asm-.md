---
title: rcp (sm5 - asm)
description: Component-wise reciprocal.
ms.assetid: 499A14D6-36DB-4860-94D1-887D931E60D4
ms.topic: reference
ms.date: 05/31/2018
---

# rcp (sm5 - asm)

Component-wise reciprocal.



| rcp\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|------------------------------------------------------------|



 



| Item                                                            | Description                                                                         |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results<br/> *dest* = **1.0f** / *src0*.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The number to take the reciprocal of.<br/>                             |



 

## Remarks

Use this instruction for reduced precision reciprocal, independent of the strict requirements for divide.

Maximum relative error is 2-21. (The error tolerance just matches rsq)

The following table shows the results obtained when executing the instruction with various classes of numbers.



| *src*  | **-inf** | **-F** | **-denorm** | **-0** | **+0** | **+denorm** | **+F** | **+inf** | **NaN** |
|--------|----------|--------|-------------|--------|--------|-------------|--------|----------|---------|
| *dest* | -0       | -F     | -inf        | -inf   | +inf   | +inf        | +F     | +0       | NaN     |



 

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

 

 





