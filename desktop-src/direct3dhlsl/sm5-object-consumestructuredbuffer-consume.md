---
title: ConsumeStructuredBuffer::Consume function
description: Removes a value from the end of the buffer.
ms.assetid: b4f7b472-9274-463d-99b0-f05b74f54fc1
keywords:
- Consume function HLSL
topic_type:
- apiref
api_name:
- Consume
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Consume function

Removes a value from the end of the buffer.

## Syntax

``` syntax
T Consume(void);
```

## Parameters

This function has no parameters.

## Return value

Type: **T**

The value removed (can be a structure).

## Remarks

T can be any data type including a structure.

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

 

 




