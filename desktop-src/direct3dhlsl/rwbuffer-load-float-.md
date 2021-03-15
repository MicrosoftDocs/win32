---
title: RWBuffer::Load(int) function
description: Reads buffer data. | RWBuffer::Load(int) function
ms.assetid: 3066E244-DE56-4F0D-8443-018B9EFEC1FF
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

# RWBuffer::Load(int) function

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

The return type matches the type in the declaration for the [**RWBuffer**](sm5-object-rwbuffer.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwbuffer-load.md)
</dt> </dl>

 

 




