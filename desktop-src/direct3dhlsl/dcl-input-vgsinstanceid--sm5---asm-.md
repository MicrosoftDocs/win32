---
title: dcl_input vGSInstanceID (sm5 - asm)
description: Enable geometry shader instancing.
ms.assetid: 47B9BAD5-0FFF-4DB7-B34A-7811B8A4F792
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_input vGSInstanceID (sm5 - asm)

Enable geometry shader instancing.



| dcl\_input vGSInstanceID, instanceCount |
|-----------------------------------------|



 



| Item                                                                                                                       | Description                           |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="vGSInstanceID"></span><span id="vgsinstanceid"></span><span id="VGSINSTANCEID"></span>*vGSInstanceID*<br/> | \[in\] The instance ID.<br/>    |
| <span id="instanceCount"></span><span id="instancecount"></span><span id="INSTANCECOUNT"></span>*instanceCount*<br/> | \[in\] The instance count.<br/> |



 

## Remarks

The *instanceCount* parameter of the declaration specifies how many instances the geometry shader should execute for each input primitive. The maximum value for *instanceCount* is 32.

The maximum number of vertices declared for output, via [**dcl\_maxOutputVertexCount**](dcl-maxoutputvertexcount.md), applies individually to each instance.

The instance count in this declaration, multiplied by the maximum vertex count per instance via [**dcl\_maxOutputVertexCount**](dcl-maxoutputvertexcount.md), must be <= 1024.

The amount of data that a given geometry shader instance can emit is 1024 scalars maximum, validated by counting up all scalars declared for input and multiplying by the declared output vertex count.

Use of geometry shader instancing effectively increases the total amount of data that can be emitted per input primitive. 1024 scalars for a single instance yields up to 1024\*32 scalars of output data across all geometry shader instances for a single input primitive. However the more instances, the fewer vertices each instance can emit. A single instance (no instancing) can emit 1024 vertices. If you declare \*32 instances it means each instance can only output 1024/32 = 32 vertices.

The geometry shader instancing declaration makes available to the program a standalone 32-bit integer input register, *vGSInstanceID*. Each geometry shader instance is identified by the value contained in *vGSInstanceID* \[0,1,2...\].

*vGSInstanceID* is not part of the geometry shader input vertex array (e.g. 3 vertices when inputting a triangle). The *vGSInstanceID* register stands on its own, like vPrimitiveID.

When each geometry shader instance ends, there is an implicit cut in the output topology, so consecutive instances do not depend on each other.

Although hardware may execute each geometry shader instance in parallel, the output of all instances at the end is serialized as if all the instanced geometry shader invocations ran sequentially in a loop iterating *vGSInstanceID* from 0 to *instanceCount*-1, with implicit output topology cuts at the end of each instance.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        | X        |       |         |



 

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

 

 





