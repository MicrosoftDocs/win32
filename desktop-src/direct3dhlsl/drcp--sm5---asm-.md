---
title: drcp (sm5 - asm)
description: Computes a component-wise double-precision reciprocal.
ms.assetid: 499A14D6-36DB-4860-94D1-887D931E60D4
ms.topic: reference
ms.date: 05/31/2018
---

# drcp (sm5 - asm)

Computes a component-wise double-precision reciprocal.



| rcp\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|------------------------------------------------------------|



 



| Item                                                            | Description                                                                                                                     |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results<br/> *dest* = **1.0** / *src0*. The result value must be accurate to 1.0 ULP<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The number to take the reciprocal of.<br/>                                                                         |



 

## Remarks

The DRCP instruction is emitted by the HLSL compiler only when explicitly called via the rcp() intrinsic, when a double is used as the argument. The accuracy of this instruction is required to be 1.0 ULP.

Shaders that use this instruction will be marked with a shader flag that will cause them to fail to bind unless all the following conditions are met.

-   The system supports DirectX 11.1.
-   The system includes a WDDM 1.2 driver.
-   The driver reports support for this instruction via **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS.ExtendedDoublesShaderInstructions** set to **TRUE**.

The following table shows the results obtained when executing the instruction with various classes of numbers, assuming that neither overflow or underflow occurs.

In this table F means finite-real number.



| **src**->  | **-inf** | **-F** | **-0** | **+0** | **+F** | **+inf** | **NaN** |
|---------------|----------|--------|--------|--------|--------|----------|---------|
| **dest**-> | -0       | -F     | -inf   | +inf   | +F     | +0       | NaN     |



 

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

 

 





