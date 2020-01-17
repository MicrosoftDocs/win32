---
title: mad (sm4 - asm)
description: Component-wise multiply add.
ms.assetid: 1C24AF49-AA32-4D3A-8478-C9BAC4FE7D77
ms.topic: reference
ms.date: 05/31/2018
---

# mad (sm4 - asm)

Component-wise multiply & add.



| :mad\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\], \[-\]src2\[\_abs\]\[.swizzle\] |
|-----------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                  |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation.<br/> *dest* = *src0* \* *src1* + *src2*<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The multiplicand.<br/>                                                          |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The multiplier.<br/>                                                            |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The addend.<br/>                                                                |



 

## Remarks

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

 

 





