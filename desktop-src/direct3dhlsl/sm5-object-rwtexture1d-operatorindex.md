---
title: RWTexture1D::Operator  function
description: Returns a resource variable. | RWTexture1D::Operator  function
ms.assetid: 16e62879-8ed3-4b17-9124-9da41c41af4f
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

# RWTexture1D::Operator  function

Returns a resource variable.

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

The index position. Contains the x coordinate.

</dd> </dl>

## Return value

Type: **R**

A resource variable.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[RWTexture1D](sm5-object-rwtexture1d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




