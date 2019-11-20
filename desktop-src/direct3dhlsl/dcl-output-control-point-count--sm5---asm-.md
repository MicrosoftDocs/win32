---
title: dcl_output_control_point_count (sm5 - asm)
description: Declares the hull shader output control point count.
ms.assetid: 51E8117F-1802-413B-9820-04D5CEBE2DB6
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_output\_control\_point\_count (sm5 - asm)

Declares the hull shader output control point count.



| dcl\_output\_control\_point\_count N |
|--------------------------------------|



 



| Item                                                   | Description                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="N"></span><span id="n"></span>*N*<br/> | \[in\] An integer value from 0 to 32 that specifies the output control point count.<br/> |



 

## Remarks

The hull shader can output 0 control points if they are not needed.

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

 

 





