---
title: frc (sm4 - asm)
description: Component-wise, extract fractional component.
ms.assetid: 17C88BCE-7F2F-446C-9BB4-860098B5E42A
ms.topic: reference
ms.date: 05/31/2018
---

# frc (sm4 - asm)

Component-wise, extract fractional component.



| frc\[\_sat\] dest\[.mask\], \[-\] src0\[\_abs\]\[.swizzle\] |
|-------------------------------------------------------------|



 



| Item                                                            | Description                                                                                                                              |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the result of the operation.<br/> *dest* = *src0* - [round\_ni](round-ni--sm4---asm-.md)(*src0*)<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The component in the operation.<br/>                                                                                        |



 

## Remarks

The following table shows the results obtained when executing the instruction with various classes of numbers.



| **src**  | **-inf** | **-F**     | **-denorm** | **-0** | **+0** | **+denorm** | **+F**     | **+inf** | **NaN** |
|----------|----------|------------|-------------|--------|--------|-------------|------------|----------|---------|
| **dest** | NaN      | \[+0 to 1) | +0          | +0     | +0     | +0          | \[+0 to 1) | NaN      | NaN     |



 

F means finite-real number.

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

 

 





