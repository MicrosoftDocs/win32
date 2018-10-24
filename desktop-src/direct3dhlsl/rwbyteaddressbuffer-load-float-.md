---
title: Load(int) function
description: Gets one value.
ms.assetid: C95C865E-E44D-46DC-A076-BD2903758432
keywords:
- Load function HLSL
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# Load(int) function

Gets one value.

## Syntax


```C++
uint Load(
  _In_ int Location
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

 

 




