---
title: RWByteAddressBuffer::Store3 function
description: Sets three values.
ms.assetid: eaf12b5a-c9c6-413a-9646-3d14e7825460
keywords:
- Store3 function HLSL
topic_type:
- apiref
api_name:
- Store3
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Store3 function

Sets three values.

## Syntax

``` syntax
void Store3(
  in uint address,
  in uint3 values
);
```

## Parameters

<dl> <dt>

*address* \[in\]
</dt> <dd>

Type: **uint**

The input address in bytes, which must be a multiple of 4.

</dd> <dt>

*values* \[in\]
</dt> <dd>

Type: **uint3**

Three input values.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




