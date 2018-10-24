---
title: Load(int) function
description: Reads texture data.
ms.assetid: AA5E324E-A2C0-45C5-92A8-E4DBC4EB684C
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

Reads texture data.

## Syntax


```C++
 Load(
  _In_ int Location
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int**

The location of the texture.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**RWTexture1D**](sm5-object-rwtexture1d.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwtexture1d-load.md)
</dt> </dl>

 

 




