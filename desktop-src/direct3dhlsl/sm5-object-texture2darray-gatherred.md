---
title: GatherRed(S,float,int) function
description: Samples a texture and returns the red component.
ms.assetid: cb9c21ef-87f4-4c32-b41a-9fc7478713a6
keywords:
- GatherRed function HLSL
topic_type:
- apiref
api_name:
- GatherRed
api_type:
- NA
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GatherRed(S,float,int) function

Samples a texture and returns the red component.

## Syntax

``` syntax
TemplateType GatherRed(
  in sampler s,
  in float3 location,
  in int2 offset
);
```

## Parameters

<dl> <dt>

*s* \[in\]
</dt> <dd>

Type: **sampler**

The zero-based sampler index.

</dd> <dt>

*location* \[in\]
</dt> <dd>

Type: **float3**

The sample coordinates (u,v).

</dd> <dt>

*offset* \[in\]
</dt> <dd>

Type: **int2**

An offset that is applied to the texture coordinate before sampling.

</dd> </dl>

## Return value

Type: **TemplateType**

A four-component value whose type is the same as the template type.

## Remarks

The texture samples can be used for bilinear interpolation.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[GatherRed methods](texture2darray-gatherred.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




