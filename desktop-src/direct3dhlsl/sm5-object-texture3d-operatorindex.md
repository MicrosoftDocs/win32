---
title: Texture3D::Operator  function
description: Returns a read-only resource variable. | Texture3D::Operator  function
ms.assetid: d7e27778-6a96-47f8-a58a-1966452adf04
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

# Texture3D::Operator  function

Returns a read-only resource variable.

## Syntax

``` syntax
R Operator[](
  in uint3 pos
);
```

## Parameters

<dl> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint3**

The index position. Contains the (x, y, z) coordinates.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

This method always accesses the first mip level. To specify other mip levels use the [**mip.operator\[\]\[\]**](sm5-object-texture3d-mipsoperatorindex.md) instead.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture3D](sm5-object-texture3d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




