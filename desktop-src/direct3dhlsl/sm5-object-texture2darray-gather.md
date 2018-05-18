---
title: Gather(S,float,int) function
description: Samples a texture and returns all four components.
ms.assetid: 'b0355158-01c8-45a1-bb5d-29a8c43b1685'
keywords: ["Gather function HLSL"]
topic_type:
- apiref
api_name:
- Gather
api_type:
- NA
---

# Gather(S,float,int) function

Samples a texture and returns all four components.

## Syntax

``` syntax
TemplateType Gather(
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

The offset applied to the texture coordinates before sampling.

</dd> </dl>

## Return value

Type: **TemplateType**

A four-component value whose type is the same as the template type.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Gather methods](texture2darray-gather.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




