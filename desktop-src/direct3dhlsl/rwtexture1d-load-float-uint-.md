---
title: Load(int,uint) function
description: Reads texture data and returns status about the operation.
ms.assetid: 3BF2397D-400C-48EE-8D45-872BA61F007B
keywords:
- Load function HLSL
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# Load(int,uint) function

Reads texture data and returns status about the operation.

## Syntax


```C++
 Load(
  _In_  int  Location,
  _Out_ uint Status
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

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

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

 

 




