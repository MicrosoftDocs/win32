---
title: dcl_tessellator_partitioning (sm5 - asm)
description: Declare the tessellator partitioning in a hull shader declaration section.
ms.assetid: 6EA00C6B-A0DE-4CE4-8B52-1337CA92CA5E
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_tessellator\_partitioning (sm5 - asm)

Declare the tessellator partitioning in a hull shader declaration section.



| dcl\_tessellator\_partitioning mode |
|---------------------------------------------------------------------------------------------------------------------------------------------|



 



| Item | Description                                     |
|------|-------------------------------------------------|
| <span id="partitioning_integer__________________________________partitioning_pow2_partitioning_fractional_odd__________________________________partitioning_fractional_even"></span><span id="PARTITIONING_INTEGER__________________________________PARTITIONING_POW2_PARTITIONING_FRACTIONAL_ODD__________________________________PARTITIONING_FRACTIONAL_EVEN"></span>*mode*<br/> | \[in\] The tessellator partitioning mode. One of:<br/><ul><li>partitioning\_integer</li><li>partitioning\_pow2</li><li>partitioning\_fractional\_odd</li><li>partitioning\_fractional\_even</li></ul> |



 

## Remarks

From the hardware point of view, \_pow2 behaves just like \_integer. It is up to the HLSL shader author and/or compilercode to round TessFactors to powers of 2.

This instruction applies to the following shader stages:



| Vertex | Hull                 | Domain | Geometry | Pixel | Compute |
|--------|----------------------|--------|----------|-------|---------|
|        | Declarations Section |        |          |       |         |



 

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

 

 





