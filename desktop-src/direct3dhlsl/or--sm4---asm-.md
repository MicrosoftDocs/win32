---
title: or (sm4 - asm)
description: Bitwise or.
ms.assetid: BBC06F8C-4C86-4077-A1F9-383D6A8FBED3
ms.topic: reference
ms.date: 05/31/2018
---

# or (sm4 - asm)

Bitwise or.



| or dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|------------------------------------------------------|



 



| Item                                                            | Description                                         |
|-----------------------------------------------------------------|-----------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation.<br/>      |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to OR with *src1*.<br/> |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to OR with *src0*.<br/> |



 

## Remarks

This instruction performs a component-wise logical OR of each pair of 32-bit values from *src0* and *src1*. The 32-bit results are placed in *dest*.

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

 

 





