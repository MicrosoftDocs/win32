---
title: uge (sm4 - asm)
description: Component-wise vector unsigned integer greater-than-or-equal comparison.
ms.assetid: CA8E19EC-619F-4C19-B6FD-91650B5DAF9F
ms.topic: reference
ms.date: 05/31/2018
---

# uge (sm4 - asm)

Component-wise vector unsigned integer greater-than-or-equal comparison.



| uge dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\] |
|-------------------------------------------------------|



 



| Item                                                            | Description                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to compare to *src1*.<br/>        |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to compare to *src0*.<br/>        |



 

## Remarks

This instruction performs the unsigned integer comparison (*src0* >= *src1*) for each component, and writes the result to *dest*.

If the comparison is true, then 0xFFFFFFFF is returned for that component. Otherwise 0x0000000 is returned.

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

 

 





