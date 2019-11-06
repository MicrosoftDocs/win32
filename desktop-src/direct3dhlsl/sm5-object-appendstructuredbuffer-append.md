---
title: AppendStructuredBuffer::Append function
description: Appends a value to the end of the buffer.
ms.assetid: 667bc6dc-c0d0-419a-9227-99ce30b9cc73
keywords:
- Append function HLSL
topic_type:
- apiref
api_name:
- Append
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Append function

Appends a value to the end of the buffer.

## Syntax

``` syntax
void Append(
  in T value
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **T**

The input value.

</dd> </dl>

## Return value

None

## Remarks

T can be any data type including structures.

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

 

 




