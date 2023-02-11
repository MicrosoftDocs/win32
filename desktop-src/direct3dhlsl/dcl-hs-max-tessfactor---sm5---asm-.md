---
title: dcl_hs_max_tessfactor (sm5 - asm)
description: Declare the maxTessFactor for the patch.
ms.assetid: 7EF0FD81-69FE-49F6-95DF-0C452A90A713
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_hs\_max\_tessfactor (sm5 - asm)

Declare the maxTessFactor for the patch.



| dcl\_hs\_max\_tessfactor N |
|----------------------------|



 



| Item                                                   | Description                          |
|--------------------------------------------------------|--------------------------------------|
| <span id="N"></span><span id="N"></span>*N*<br/> | \[in\] The maxTessFactor.<br/> |



 

## Remarks

The maxTessFactor is a float32 value in the range {1.0 ... 64.0}.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | X    |        |          |       |         |



 

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

 

 





