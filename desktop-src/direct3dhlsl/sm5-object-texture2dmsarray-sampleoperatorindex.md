---
title: Texture2DMSArray::sample.Operator    function
description: Returns a read-only resource variable. | Texture2DMSArray::sample.Operator    function
ms.assetid: 5334c1d5-dfbd-4987-875c-0b92967b0f13
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

# Texture2DMSArray::sample.Operator    function

Returns a read-only resource variable.

## Syntax

``` syntax
R sample.Operator[][](
  in uint sampleSlice,
  in uint3 pos
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

Type: **uint3**

The index position. The first and second components contain the (x, y) coordinates. The third component indicates the desired array slice.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture2DMSArray<float4, 4> alpha;

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

[Texture2DMSArray](sm5-object-texture2dmsarray.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




