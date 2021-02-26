---
title: Texture2D::Operator  function
description: Returns a read-only resource variable. | Texture2D::Operator  function
ms.assetid: 72ba3fc8-04c3-479a-b307-525020898bac
keywords:
- Operator function HLSL
topic_type:
- apiref
api_name:
- Operator
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2D::Operator  function

Returns a read-only resource variable.

## Syntax

``` syntax
R Operator[](
  in uint2 pos
);
```

## Parameters

<dl> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint2**

The index position. Contains the (x, y) coordinates.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

This method always accesses the first mip level. To specify other mip levels, use the [**mip.operator\[\]\[\]**](sm5-object-texture2d-mipsoperatorindex.md) method instead.

The texture samples can be used for bilinear interpolation.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture2D](sm5-object-texture2d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




