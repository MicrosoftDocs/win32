---
title: div (sm4 - asm)
description: Component-wise divide.
ms.assetid: B086F069-8F43-4746-A6A5-8F4462212648
ms.topic: reference
ms.date: 05/31/2018
---

# div (sm4 - asm)

Component-wise divide.



| div\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] \[-\]src1\[\_abs\]\[.swizzle\] |
|-------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                    |
|-----------------------------------------------------------------|------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The dividend.<br/>                |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The divisor.<br/>                 |



 

## Remarks

The following table shows the results obtained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs.

You should note the two allowed implementations of divide: a/b and a\*(1/b).

One outcome of this is that there are exceptions to the table below for large denominator values (greater than 8.5070592e+37), where 1/denominator is a denorm. Because implementations may perform divide as a\*(1/b), instead of a/b directly, and 1/\[large value\] is a denorm that could get flushed, some cases in the table would produce different results. For example, (+/-)INF / (+/-)\[value > 8.5070592e+37\] may produce NaN on some implementations, but (+/-)INF on other implementations

In this table F means finite-real number.



| **src0 src1 ->** | **-inf** | **-F**     | **-denorm** | **-0** | **+0** | **+denorm** | **+F**     | **+inf** | **Nan** |
|---------------------|----------|------------|-------------|--------|--------|-------------|------------|----------|---------|
| **-inf**            | -inf     | -inf       | -inf        | -inf   | -inf   | -inf        | -inf       | NaN      | NaN     |
| **-F**              | -inf     | -F         | src0        | src0   | src0   | src0        | +-F or +-0 | +inf     | NaN     |
| **-denorm**         | -inf     | src1       | -0          | -0     | +0     | +0          | src1       | +inf     | NaN     |
| **-0**              | -inf     | src1       | -0          | -0     | +0     | +0          | src1       | +inf     | NaN     |
| **+0**              | -inf     | src1       | +0          | +0     | +0     | +0          | src1       | +inf     | NaN     |
| **+denorm**         | -inf     | src1       | +0          | +0     | +0     | +0          | src1       | +inf     | NaN     |
| **+F**              | -inf     | +-F or +-0 | src0        | src0   | src0   | src0        | +F         | +inf     | NaN     |
| **+inf**            | NaN      | +inf       | +inf        | +inf   | +inf   | +inf        | +inf       | +inf     | NaN     |
| **NaN**             | NaN      | NaN        | NaN         | NaN    | NaN    | NaN         | NaN        | NaN      | NaN     |



 

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

 

 





