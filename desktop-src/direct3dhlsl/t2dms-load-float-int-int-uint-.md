---
title: Texture2DMS::Load(int,int,int,uint) function
description: Reads texture data and returns status of the operation. | Texture2DMS::Load(int,int,int,uint) function
ms.assetid: 4230962C-2968-4030-9770-8318F1760AEB
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

# Texture2DMS::Load(int,int,int,uint) function

Reads texture data and returns status of the operation.

## Syntax


``` syntax
 Load(
  in  int2 Location,
  in  int  sampleindex,
  in  int2 Offset,
  out uint Status
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int2**

The texture coordinates.

</dd> <dt>

*sampleindex* \[in\]
</dt> <dd>

Type: **[**int**](/windows/desktop/WinProg/windows-data-types)**

The sample index.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Type: **int2**

An offset applied to the texture coordinates before loading.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**Texture2DMS**](sm5-object-texture2dms.md) object.

## See also

<dl> <dt>

[Load methods](texture2dms-load.md)
</dt> <dt>

[**Texture2DMS**](sm5-object-texture2dms.md)
</dt> </dl>

 

 
