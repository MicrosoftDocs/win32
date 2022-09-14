---
title: ddy_coarse function
description: Computes a low precision partial derivative with respect to the screen-space y-coordinate.
ms.assetid: f6103cd3-f7ee-41c2-b3cf-9e72ca84b25e
keywords:
- ddy_coarse function HLSL
topic_type:
- apiref
api_name:
- ddy_coarse
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ddy\_coarse function

Computes a low precision partial derivative with respect to the screen-space y-coordinate.

## Syntax

``` syntax
float ddy_coarse(
  in float value
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **float**

The input value.

</dd> </dl>

## Return value

Type: **float**

The low precision partial derivative of *value*.

## Remarks

The following overloaded versions are also available:

``` syntax
float2 ddy_coarse(float2 value);
float3 ddy_coarse(float3 value);
float4 ddy_coarse(float4 value);
```

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




