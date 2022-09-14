---
title: ConsumeStructuredBuffer::GetDimensions function
description: Gets the resource dimensions. | ConsumeStructuredBuffer::GetDimensions function
ms.assetid: 0710a4fb-23b0-4b19-b9ed-21bbb9874d33
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

# ConsumeStructuredBuffer::GetDimensions function

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

The stride, in bytes, of each element.

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

[ConsumeStructuredBuffer](sm5-object-consumestructuredbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




