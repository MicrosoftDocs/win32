---
title: usubb (sm5 - asm)
description: Unsigned integer subtract with borrow.
ms.assetid: 6D42E3CA-5A37-4194-AB42-7A2337C5AB9D
ms.topic: reference
ms.date: 05/31/2018
---

# usubb (sm5 - asm)

Unsigned integer subtract with borrow.



| usubb dst0\[.mask\], dst1\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                               | Description                                                                                       |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="dst0"></span><span id="dst0"></span>*dst0*<br/> | \[in\] Contains the LSAB results of the instruction.<br/>                                   |
| <span id="dst1"></span><span id="dst1"></span>*dst1*<br/> | \[in\] The corresponding component of *dst0* that specifies if a borrow was produced.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>    | \[in\] The value from which to subtract.<br/>                                               |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>    | \[in\] The amount to subtract from *src0*.<br/>                                             |



 

## Remarks

This instruction performs a component-wise unsigned subtract of 32-bit operands *src1* from *src0*, placing the LSB part of the 32-bit result in *dst0*.

The corresponding component in *dst1* is written with 1 if a borrow is produced, 0 otherwise.

*dst1* can be NULL if the borrow is not needed.

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

 

 





