---
title: Load(int,uint) function
description: Reads buffer data and returns status about the operation.
ms.assetid: 19FAA031-F31E-4B73-BC69-489CDF0CF184
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

Reads buffer data and returns status about the operation.

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

The location of the buffer.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://docs.microsoft.com/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type:

The return type matches the type in the declaration for the [**RWStructuredBuffer**](sm5-object-rwstructuredbuffer.md) object.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load methods](rwstructuredbuffer-load.md)
</dt> </dl>

 

 




