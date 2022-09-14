---
title: RWTexture3D::Load(int,uint) function
description: Reads texture data and returns status about the operation. | RWTexture3D::Load(int,uint) function
ms.assetid: 7BC334D3-217A-454F-B205-A9D7D66B5E99
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

# RWTexture3D::Load(int,uint) function

Reads texture data and returns status about the operation.

## Syntax


``` syntax
 Load(
  in  int  Location,
  out uint Status
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int**

The location of the texture.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

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

 

 
