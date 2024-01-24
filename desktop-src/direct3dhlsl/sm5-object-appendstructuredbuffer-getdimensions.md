---
title: AppendStructuredBuffer::GetDimensions function
description: Gets the resource dimensions. | AppendStructuredBuffer::GetDimensions function
ms.assetid: 41ed86d5-25c0-48bd-add9-792eb89605c3
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

# AppendStructuredBuffer::GetDimensions function

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

The number of structures.

</dd> <dt>

*stride* \[out\]
</dt> <dd>

Type: **uint**

The number of bytes in each element.

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

[AppendStructuredBuffer](sm5-object-appendstructuredbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




