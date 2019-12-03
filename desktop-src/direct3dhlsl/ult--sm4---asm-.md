---
title: ult (sm4 - asm)
description: Component-wise vector unsigned integer less-than comparison.
ms.assetid: DB10F654-4A98-4ED8-A3B4-CA9FE1DFE6CD
ms.topic: reference
ms.date: 05/31/2018
---

# ult (sm4 - asm)

Component-wise vector unsigned integer less-than comparison.



| ult dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|-------------------------------------------------------|



 



| Item                                                            | Description                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The value to compare to *src1*.<br/>             |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The value to compare to *src1*.<br/>             |



 

## Remarks

Performs the unsigned integer comparison (*src0* < *src1*) for each component, and writes the result to *dest*.

If the comparison is true, this instruction returns 0xFFFFFFFF for that component. Otherwise it returns 0x0000000.

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

 

 





