---
title: dp2 (sm4 - asm)
description: 2-dimensional vector dot-product of components rg, POS-swizzle.
ms.assetid: E35F6A8B-6D8E-4660-B0F3-95B76BC19229
ms.topic: reference
ms.date: 05/31/2018
---

# dp2 (sm4 - asm)

2-dimensional vector dot-product of components rg, POS-swizzle.



| dp2\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\] |
|--------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                                                    |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation. <br/> *dest* = *src0.r* \* *src1.r* + *src0.g* \* *src1.g*<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components in the operation.<br/>                                                                             |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components in the operation.<br/>                                                                             |



 

## Remarks

Scalar result replicated to components in write mask.

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

 

 





