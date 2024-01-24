---
title: Buffer::GetDimensions function
description: Gets the length of the buffer. | Buffer::GetDimensions function
ms.assetid: 704890e8-43e4-4e72-b7e2-eeef331bef1c
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

# Buffer::GetDimensions function

The length, in elements, of the Buffer as set in the Shader Resource View.

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
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Buffer](sm5-object-buffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




