---
title: RWByteAddressBuffer::Load(int) function
description: Gets one value. | RWByteAddressBuffer::Load(int) function
ms.assetid: C95C865E-E44D-46DC-A076-BD2903758432
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

# RWByteAddressBuffer::Load(int) function

Gets one value.

## Syntax


``` syntax
uint Load(
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

Type: **uint**

One value.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwbyteaddressbuffer-load.md)
</dt> </dl>

 

 




