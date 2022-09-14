---
title: dcl_input vThread (sm5 - asm)
description: Declare compute shader input IDs.
ms.assetid: C041863A-32B0-4588-A1A9-E416AF9B723C
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_input vThread (sm5 - asm)

Declare compute shader input IDs.



| dcl\_input {vThreadID.xyz\|vThreadGroupID.xyz\| vThreadIDInGroup.xyz\|vThreadIDInGroupFlattened} |
|--------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                                                                                                                                                                                                                                                                          | Description                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="vThreadID___vThreadGroupID___vThreadIDInGroup___vThreadIDInGroupFlattened"></span><span id="vthreadid___vthreadgroupid___vthreadidingroup___vthreadidingroupflattened"></span><span id="VTHREADID___VTHREADGROUPID___VTHREADIDINGROUP___VTHREADIDINGROUPFLATTENED"></span>*vThreadID \| vThreadGroupID \| vThreadIDInGroup \| vThreadIDInGroupFlattened*<br/> | \[in\] The 3-component unsigned 32-bit integer ID value.<br/> |



 

**dcl\_input** is an existing declaration in other shader stages. It is used in the compute shader to declare the various 3-component unsigned 32-bit integer ID values unique to the compute shader. They are:

-   vThreadID.xyz
-   vGroupID.xyz
-   vThreadIDInGroup.xyz
-   vThreadIDInGroupFlattened (single component)

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

 

 





