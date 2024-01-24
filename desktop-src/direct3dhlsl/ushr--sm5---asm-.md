---
title: ushr (sm5 - asm)
description: Shift right. | ushr (sm5 - asm)
ms.assetid: C695CB6C-A6C9-4DC8-8EBE-70A0CFFC4981
ms.topic: reference
ms.date: 05/31/2018
---

# ushr (sm5 - asm)

Shift right.



| ushr dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|--------------------------------------------------------|



 



| Item                                                            | Description                                                                  |
|-----------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] Contains the results of the instruction.<br/>                   |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The 32-bit values to shift.<br/>                                |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The LSB 5 bits provide the number of bits to shift (0-31).<br/> |



 

This instruction performs a component-wise shift of each 32-bit value in *src0* right by an unsigned integer bit count provided by the LSB 5 bits (0-31 range) in *src1*, inserting 0. The 32-bit per component results is placed in *dest*.

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

 

 





