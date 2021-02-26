---
title: RWStructuredBuffer::Load(int) function
description: Reads buffer data. | RWStructuredBuffer::Load(int) function
ms.assetid: 9CB40579-6BF8-468C-81B8-936D9940458E
keywords:
- Load function HLSL
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWStructuredBuffer::Load(int) function

Reads buffer data.

## Syntax


``` syntax
 Load(
  in int Location
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int**

The location of the buffer.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**RWStructuredBuffer**](sm5-object-rwstructuredbuffer.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwstructuredbuffer-load.md)
</dt> </dl>

 

 




