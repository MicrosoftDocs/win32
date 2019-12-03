---
title: dcl_thread_group (sm5 - asm)
description: Declare thread group size.
ms.assetid: CB8192C4-100D-49B6-94E7-6CD3AEC28149
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_thread\_group (sm5 - asm)

Declare thread group size.



| dcl\_thread\_group x, y, z |
|----------------------------|



 



| Item                                                   | Description                                                        |
|--------------------------------------------------------|--------------------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] An usigned 32-bit integer. 1 <= x <= 1024 <br/> |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] An usigned 32-bit integer. 1 <= y <= 1024<br/>  |
| <span id="z"></span><span id="Z"></span>*z*<br/> | \[in\] An usigned 32-bit integer. 1 <= z <= 64<br/>    |



 

## Remarks

x\*y\*z <= 1024

This thread group declaration must appear once in a compute shader.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          |       | X       |



 

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

 

 





