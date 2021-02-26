---
title: RWTexture2D::Load(int) function
description: Reads texture data. | RWTexture2D::Load(int) function
ms.assetid: AEBB9C78-BE4B-4121-93CC-EE03B9925CF0
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

# RWTexture2D::Load(int) function

Reads texture data.

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

The location of the texture.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**RWTexture2D**](sm5-object-rwtexture2d.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwtexture2d-load.md)
</dt> </dl>

 

 




