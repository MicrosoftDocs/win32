---
title: StructuredBuffer::Operator  function
description: Returns a read-only resource variable of a StructuredBuffer.
ms.assetid: e2a1b0f7-f374-44a3-b567-8a2318e8b2b8
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

# StructuredBuffer::Operator  function

Returns a read-only resource variable of a [**StructuredBuffer**](sm5-object-structuredbuffer.md).

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

A read-only resource variable.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[StructuredBuffer](sm5-object-structuredbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




