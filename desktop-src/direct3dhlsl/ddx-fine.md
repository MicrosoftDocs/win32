---
title: ddx_fine function
description: Computes a high precision partial derivative with respect to the screen-space x-coordinate. | ddx_fine function
ms.assetid: 41062d6f-2b7f-4594-a6de-da37ded5d444
keywords:
- ddx_fine function HLSL
topic_type:
- apiref
api_name:
- ddx_fine
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ddx\_fine function

Computes a high precision partial derivative with respect to the screen-space x-coordinate.

## Syntax

``` syntax
float ddx_fine(
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

The high precision partial derivative of *value*.

## Remarks

The following overloaded versions are also available:

``` syntax
float2 ddx_fine(float2 value);
float3 ddx_fine(float3 value);
float4 ddx_fine(float4 value);
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

 

 




