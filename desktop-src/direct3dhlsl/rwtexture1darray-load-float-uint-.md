---
title: Load(int,uint) function
description: Reads texture data and returns status about the operation.
ms.assetid: 'EF1D51CC-E037-4E04-9DD6-6A9C5950E5B5'
keywords: ["Load function HLSL"]
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
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

The return type matches the type in the declaration for the [**RWTexture1DArray**](sm5-object-rwtexture1darray.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwtexture1darray-load.md)
</dt> </dl>

 

 




