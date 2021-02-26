---
title: RWByteAddressBuffer::GetDimensions function
description: Gets the length of the buffer. | RWByteAddressBuffer::GetDimensions function
ms.assetid: 7d78aa0d-75b8-43d5-85d9-0a6fb04ae64f
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

# RWByteAddressBuffer::GetDimensions function

Gets the length of the buffer.

## Syntax

``` syntax
void GetDimensions(
  out uint dim
);
```

## Parameters

<dl> <dt>

*dim* \[out\]
</dt> <dd>

Type: **uint**

The length, in bytes, of the buffer.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




