---
title: Texture2DMS::sample.Operator    function
description: Retrieves a value from the resource at the location and sample index provided. | Texture2DMS::sample.Operator    function
ms.assetid: 5bc24129-b690-44dd-ae85-8533b10befaa
keywords:
- sample.Operator function HLSL
topic_type:
- apiref
api_name:
- sample.Operator
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2DMS::sample.Operator    function

Retrieves a value from the resource at the location and sample index provided.

## Syntax

``` syntax
R sample.Operator[][](
  in uint sampleSlice,
  in uint2 pos
);
```

## Parameters

<dl> <dt>

*sampleSlice* \[in\]
</dt> <dd>

Type: **uint**

The sample slice index.

</dd> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint2**

The index position. The components contain the (x, y) coordinates.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture2DMS<float4, 8> tex;

float4 main( float3 tcoord : texturecoord0 ) : SV_Target
{
     return s_msTexture.sample[2][tcoord];
}
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture2DMS](sm5-object-texture2dms.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




