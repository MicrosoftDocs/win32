---
title: RWStructuredBuffer::Operator  function
description: Returns a resource variable. | RWStructuredBuffer::Operator  function
ms.assetid: e821b60e-38db-463f-b0c6-47f2a4c9ccee
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

# RWStructuredBuffer::Operator  function

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

The index position.

</dd> </dl>

## Return value

Type: **R**

A resource variable.

## Remarks

A structured resource can be further indexed based on the component names of the structures.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[RWStructuredBuffer](sm5-object-rwstructuredbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




