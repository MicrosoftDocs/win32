---
title: RWByteAddressBuffer::Load2(uint,uint) function
description: Gets two values and returns status of the operation.
ms.assetid: E6BBA8A7-D53F-4718-B007-EBDE50FADB06
keywords:
- Load2 function HLSL
topic_type:
- apiref
api_name:
- Load2
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Load2(uint,uint) function

Gets two values and returns status of the operation.

## Syntax


``` syntax
uint2 Load2(
  in  uint Location,
  out uint Status
);
```



## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **uint**

The location of the buffer.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **uint2**

Two values.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load2 methods](rwbyteaddressbuffer-load2.md)
</dt> </dl>

 

 