---
title: ddiv (sm5 - asm)
description: Computes a component-wise double-precision division.
ms.assetid: 0A67FC35-7F2F-4258-83CE-1CA398E57952
ms.topic: reference
ms.date: 05/31/2018
---

# ddiv (sm5 - asm)

Computes a component-wise double-precision division.



| ddiv\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] \[-\]src1\[\_abs\]\[.swizzle\] |
|--------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                   |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The result of the operation. The result value must be accurate to 0.5 ULP. <br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The dividend.<br/>                                                               |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The divisor.<br/>                                                                |



 

## Remarks

The DDIV instruction will be emitted by the HLSL compiler whenever the division operator is used with doubles. The accuracy of this instruction will be required to be 0.5 ULP.

Shaders that use this instruction will be marked with a shader flag that will cause them to fail to bind unless all the following conditions are met.

-   The system supports DirectX 11.1.
-   The system includes a WDDM 1.2 driver.
-   The driver reports support for this instruction via **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS.ExtendedDoublesShaderInstructions** set to **TRUE**.

The following table shows the results btained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs.

In this table F means finite-real number.



| **src0 src1 ->** | **-inf** | **-F** | **-1.0** | **-0** | **+0** | **+1.0** | **+F** | **+inf** | **NaN** |
|---------------------|----------|--------|----------|--------|--------|----------|--------|----------|---------|
| **-inf**            | NaN      | +inf   | +inf     | +inf   | -inf   | -inf     | -inf   | NaN      | NaN     |
| **-F**              | +0       | +F     | -src0    | +inf   | -inf   | src0     | -F     | -0       | NaN     |
| **-0**              | +0       | +0     | +0       | NaN    | NaN    | -0       | -0     | -0       | NaN     |
| **+0**              | -0       | -0     | -0       | NaN    | NaN    | +0       | +0     | +0       | NaN     |
| **+F**              | -0       | -F     | -src0    | -inf   | +inf   | src0     | +F     | +0       | NaN     |
| **+inf**            | NaN      | -inf   | -inf     | -inf   | +inf   | +inf     | +inf   | NaN      | NaN     |
| **NaN**             | NaN      | NaN    | NaN      | NaN    | NaN    | NaN      | NaN    | NaN      | NaN     |



 

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

 

 





