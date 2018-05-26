---
title: Load(int,int,uint) function
description: Reads texture data and returns status of the operation.
ms.assetid: 3F562ADB-225F-462B-A7AC-40797BBB632A
keywords:
- Load function HLSL
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Load(int,int,uint) function

Reads texture data and returns status of the operation.

## Syntax


```C++
 Load(
  _In_  int  Location,
  _In_  int  Offset,
  _Out_ uint Status
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

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**Texture3D**](sm5-object-texture3d.md) object.

## See also

<dl> <dt>

[Load methods](texture3d-load.md)
</dt> <dt>

[**Texture3D**](sm5-object-texture3d.md)
</dt> </dl>

 

 




