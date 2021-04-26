---
title: sincos (sm4 - asm)
description: Component-wise sin(theta) and cos(theta) for theta in radians.
ms.assetid: 81FDEC8F-2C1C-4C60-A6DA-699C798F8316
ms.topic: reference
ms.date: 05/31/2018
---

# sincos (sm4 - asm)

Component-wise sin(theta) and cos(theta) for theta in radians.



| sincos\[\_sat\] destSIN\[.mask\], destCOS\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|------------------------------------------------------------------------------------|



 



| Item                                                                                               | Description                                                           |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="destSIN"></span><span id="destsin"></span><span id="DESTSIN"></span>*destSIN*<br/> | \[in\] The address of sin(*src0*), computed per component.<br/> |
| <span id="destCOS"></span><span id="destcos"></span><span id="DESTCOS"></span>*destCOS*<br/> | \[in\] The address of cos(*src0*), computed per component.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                    | \[in\] The components for which to compute sin and cos.<br/>    |



 

## Remarks

If the result is not needed, you can specify *destSIN* and *destCOS* as NULL instead of specifying a register.

Theta values can be any IEEE 32-bit floating point values.

The maximum absolute error is 0.0008 in the interval from -100\*Pi to +100\*Pi.

The following table shows the results obtained when executing the instruction with various classes of numbers.

F means finite-real number.



| **src**     | **-inf** | **-F**       | **-denorm** | **-0** | **+0** | **+denorm** | **+F**       | **+inf** | **NaN** |
|-------------|----------|--------------|-------------|--------|--------|-------------|--------------|----------|---------|
| **destSIN** | NaN      | \[-1 to +1\] | -0          | -0     | +0     | +0          | \[-1 to +1\] | NaN      | NaN     |
| **destCOS** | NaN      | \[-1 to +1\] | +1          | +1     | +1     | +1          | \[-1 to +1\] | NaN      | NaN     |



 

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

 

 





