---
title: Texture2D::GatherGreen(S,float,int) function
description: For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value. | Texture2D::GatherGreen(S,float,int) function
ms.assetid: 97e1fb52-75f4-4e73-93f1-98b7a5925efc
keywords:
- GatherGreen function HLSL
topic_type:
- apiref
api_name:
- GatherGreen
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2D::GatherGreen(S,float,int) function

For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value.

## Syntax

``` syntax
TemplateType GatherGreen(
  in sampler s,
  in float2 location,
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

Type: **float2**

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

[GatherGreen methods](texture2d-gathergreen.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




