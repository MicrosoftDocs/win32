---
title: SV_InsideTessFactor
description: Defines the tessellation amount within a patch surface.
ms.assetid: f0762aca-d84d-44c0-a163-9737ef92c1e5
keywords:
- SV_InsideTessFactor HLSL
topic_type:
- apiref
api_name:
- SV_InsideTessFactor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SV\_InsideTessFactor

Defines the tessellation amount within a patch surface.

## Type



|            |                |
|------------|----------------|
| Type       | Input Topology |
| float\[2\] | quad patch     |
| float      | tri patch      |
| unused     | isoline        |



 

Tessellation factors must be declared as array; they cannot be packed into a single vector.

## Remarks

This value must be defined during the patch constant function of the hull shader.

Required output value for the hull shader if using quad or tri patches. This value is a required input for the domain shader in order for hardware to match the signatures through the tessellator.

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    | x      |          |       |         |



 

## See also

<dl> <dt>

[Semantics](dx-graphics-hlsl-semantics.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




