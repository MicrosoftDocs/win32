---
title: Texture1D::Operator  function
description: Returns a read-only resource variable for a Texture1D.
ms.assetid: df54097d-4d1b-496a-a17d-6e9a10cfb996
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

# Texture1D::Operator  function

Returns a read-only resource variable for a [**Texture1D**](sm5-object-texture1d.md).

## Syntax

``` syntax
R Operator[](
  in uint pos
);
```

## Parameters

<dl> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint**

The index position. Contains the x-coordinate.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

This method always accesses the first mip level. To specify other mip levels, use the [**mip.operator\[\]\[\]**](sm5-object-texture1d-mipsoperatorindex.md) instead.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture1D](sm5-object-texture1d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




