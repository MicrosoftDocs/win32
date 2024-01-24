---
title: StructuredBuffer::Load(int) function
description: Reads buffer data. | StructuredBuffer::Load(int) function
ms.assetid: 'ef08d360-0494-49f7-9481-cb802e14aeee'
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

# StructuredBuffer::Load(int) function

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

The return type matches the type in the declaration for the [**StructuredBuffer**](sm5-object-structuredbuffer.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](structuredbuffer-load.md)
</dt> </dl>

 

 




