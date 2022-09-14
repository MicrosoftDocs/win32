---
title: uaddc (sm5 - asm)
description: Unsigned integer add with carry.
ms.assetid: 1007253C-F920-4003-B266-D124A255F731
ms.topic: reference
ms.date: 05/31/2018
---

# uaddc (sm5 - asm)

Unsigned integer add with carry.



| uaddc dest0\[.mask\], dest1\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                               | Description                                            |
|--------------------------------------------------------------------|--------------------------------------------------------|
| <span id="dest0"></span><span id="DEST0"></span>*dest0*<br/> | \[in\] Address of the result.<br/>               |
| <span id="dest1"></span><span id="DEST1"></span>*dest1*<br/> | \[in\] 1 if carry is produced. Otherwise 0.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>    | \[in\] 32-bit operand to be added.<br/>          |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>    | \[in\] 32-bit operand to be added.<br/>          |



 

## Remarks

*dest1* can be NULL if the carry is not needed.

Use this instruction for high precision arithmetic.

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

 

 





