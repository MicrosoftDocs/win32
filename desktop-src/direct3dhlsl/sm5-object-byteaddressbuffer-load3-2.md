---
title: ByteAddressBuffer::Load3(uint, uint) function
description: Gets three values and the status of the operation.
ms.assetid: 6AD8E957-F646-4749-A9B4-5C0C936D90E3
keywords:
- Load3 function HLSL
topic_type:
- apiref
api_name:
- Load3
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Load3(uint, uint) function

Gets three values and the status of the operation.

## Syntax

``` syntax
uint3 Load3(
  in  uint Location,
  out uint Status
);
```

## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **uint**

The input address in bytes, which must be a multiple of 4.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **uint3**

Three values.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load3 methods](byteaddressbuffer-load3.md)
</dt> <dt>

[**ByteAddressBuffer**](sm5-object-byteaddressbuffer.md)
</dt> </dl>

 

 