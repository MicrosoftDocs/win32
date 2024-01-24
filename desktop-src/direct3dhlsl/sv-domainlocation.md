---
title: SV_DomainLocation
description: Defines the location on the hull of the current domain point being evaluated.
ms.assetid: 907f568c-7c45-41e5-96c4-6e6b816a4a53
keywords:
- SV_DomainLocation HLSL
topic_type:
- apiref
api_name:
- SV_DomainLocation
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SV\_DomainLocation

Defines the location on the hull of the current domain point being evaluated.

## Type



| Type       | Input topology               |
|--------|----------------|
| float2 | quad patch     |
| float3 | tri patch      |
| float2 | isoline        |



 

## Remarks

This system value is required.

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      | x      |          |       |         |



 

## See also

<dl> <dt>

[Semantics](dx-graphics-hlsl-semantics.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




