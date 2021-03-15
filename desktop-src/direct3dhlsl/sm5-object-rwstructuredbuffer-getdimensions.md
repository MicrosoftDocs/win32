---
title: RWStructuredBuffer::GetDimensions function
description: Gets the resource dimensions. | RWStructuredBuffer::GetDimensions function
ms.assetid: 842b3d21-2e2b-4906-93ee-0252b2e8cf85
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

# RWStructuredBuffer::GetDimensions function

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

Nothing

## Remarks

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

 

 




