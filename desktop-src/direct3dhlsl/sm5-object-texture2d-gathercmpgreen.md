---
title: Texture2D::GatherCmpGreen(S,float,float,int) function
description: For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value. | Texture2D::GatherCmpGreen(S,float,float,int) function
ms.assetid: 5a11ce0c-56b2-460a-95d7-15688dd158ff
keywords:
- GatherCmpGreen function HLSL
topic_type:
- apiref
api_name:
- GatherCmpGreen
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2D::GatherCmpGreen(S,float,float,int) function

For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value.

## Syntax

``` syntax
float4 GatherCmpGreen(
  in SamplerComparisonState s,
  in float2 location,
  in float compare_value,
  in int2 offset
);
```

## Parameters

<dl> <dt>

*s* \[in\]
</dt> <dd>

Type: **SamplerComparisonState**

The zero-based sampler index.

</dd> <dt>

*location* \[in\]
</dt> <dd>

Type: **float2**

The sample coordinates (u,v).

</dd> <dt>

*compare\_value* \[in\]
</dt> <dd>

Type: **float**

A value to compare each against each sampled value.

</dd> <dt>

*offset* \[in\]
</dt> <dd>

Type: **int2**

An offset that is applied to the texture coordinate before sampling.

</dd> </dl>

## Return value

Type: **float4**

A four-component value, each component is the result of a per-component comparison.

## Remarks

The texture samples can be used for bilinear interpolation.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[GatherCmpGreen methods](texture2d-gathercmpgreen.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




