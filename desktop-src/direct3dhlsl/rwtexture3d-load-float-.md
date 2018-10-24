---
title: Load(int) function
description: Reads texture data.
ms.assetid: 93C4FFFF-8695-4BAF-BAE4-A2704332E6A9
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

The return type matches the type in the declaration for the [**RWTexture3D**](sm5-object-rwtexture3d.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwtexture3d-load.md)
</dt> </dl>

 

 




