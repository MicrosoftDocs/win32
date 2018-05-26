---
title: Load(int, uint) function
description: Gets one value and the status of the operation.
ms.assetid: 8F90671B-CEEB-4F8C-9469-D85940568872
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

# Load(int, uint) function

Gets one value and the status of the operation.

## Syntax

``` syntax
uint Load(
  in  int Location,
  out uint Status
);
```

## Parameters

<dl> <dt>

*Location* \[in\]
</dt> <dd>

Type: **int**

The input address in bytes, which must be a multiple of 4.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **uint**

One value.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load methods](byteaddressbuffer-load.md)
</dt> <dt>

[**ByteAddressBuffer**](sm5-object-byteaddressbuffer.md)
</dt> </dl>

 

 




