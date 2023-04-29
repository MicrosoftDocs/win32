---
title: exp (sm4 - asm)
description: Component-wise 2exponent.
ms.assetid: 12EB865A-BF71-4B4B-854F-9DA056B18AE0
ms.topic: reference
ms.date: 05/31/2018
---

# exp (sm4 - asm)

Component-wise 2exponent.



| exp\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|------------------------------------------------------------|



 



| Item                                                            | Description                                                                |
|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation.<br/> *dest* = 2<sup>*src0*</sup><br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The exponent.<br/>                                            |



 

## Remarks

This instruction follows limit theory. The maximum relative error is 2-21.

The following table shows the results obtained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs. In this table F means finite-real number.



| **src**  | **-inf** | **-F** | **-denorm** | **-0** | **+0** | **+denorm** | **+F** | **+inf** | **NaN** |
|----------|----------|--------|-------------|--------|--------|-------------|--------|----------|---------|
| **dest** | 0        | +F     | 1           | 1      | 1      | 1           | +F     | +inf     | NaN     |



 

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

 

 





