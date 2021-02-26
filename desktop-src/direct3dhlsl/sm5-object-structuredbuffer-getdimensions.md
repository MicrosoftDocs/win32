---
title: StructuredBuffer::GetDimensions function
description: Gets the resource dimensions. | StructuredBuffer::GetDimensions function
ms.assetid: 423ea79c-4440-4837-b637-95180a1d5019
keywords:
- GetDimensions function HLSL
topic_type:
- apiref
api_name:
- GetDimensions
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StructuredBuffer::GetDimensions function

Gets the resource dimensions.

## Syntax

``` syntax
void GetDimensions(
  out uint numStructs,
  out uint stride
);
```

## Parameters

<dl> <dt>

*numStructs* \[out\]
</dt> <dd>

Type: **uint**

The number of structures in the resource.

</dd> <dt>

*stride* \[out\]
</dt> <dd>

Type: **uint**

The stride, in bytes, of each structure element.

</dd> </dl>

## Return value

This function does not return a value.

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

 

 




