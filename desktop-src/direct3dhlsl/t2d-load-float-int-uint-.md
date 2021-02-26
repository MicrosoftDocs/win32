---
title: Texture2D::Load(int,int,uint) function
description: Reads texture data and returns status of the operation. | Texture2D::Load(int,int,uint) function
ms.assetid: 05A12BE2-4604-470B-9EE8-F03F51E6D254
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

# Texture2D::Load(int,int,uint) function

Reads texture data and returns status of the operation.

## Syntax


``` syntax
 Load(
  in  int  Location,
  in  int  Offset,
  out uint Status
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int**

The texture coordinates.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Type: **int**

An offset applied to the texture coordinates before sampling.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**Texture2D**](sm5-object-texture2d.md) object.

## See also

<dl> <dt>

[Load methods](texture2d-load.md)
</dt> </dl>

 

 
