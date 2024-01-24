---
title: RWTexture2DArray::Load(int) function
description: Reads texture data. | RWTexture2DArray::Load(int) function
ms.assetid: BC247B2A-1744-4E37-A501-22E4A592A32D
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

# RWTexture2DArray::Load(int) function

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

The return type matches the type in the declaration for the [**RWTexture2DArray**](sm5-object-rwtexture2darray.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwtexture2darray-load.md)
</dt> </dl>

 

 




