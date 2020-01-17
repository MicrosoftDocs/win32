---
title: ddx_coarse function
description: Computes a low precision partial derivative with respect to the screen-space x-coordinate.
ms.assetid: 5719f45d-b2ae-4916-8f31-c2797b661814
keywords:
- ddx_coarse function HLSL
topic_type:
- apiref
api_name:
- ddx_coarse
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ddx\_coarse function

Computes a low precision partial derivative with respect to the screen-space x-coordinate.

## Syntax

``` syntax
float ddx_coarse(
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
float2 ddx_coarse(float2 value);
float3 ddx_coarse(float3 value);
float4 ddx_coarse(float4 value);
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

 

 




