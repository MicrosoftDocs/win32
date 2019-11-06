---
title: RWByteAddressBuffer::Store function
description: Sets one value.
ms.assetid: edfda955-602c-44f4-adc3-77b61c9dcd05
keywords:
- Store function HLSL
topic_type:
- apiref
api_name:
- Store
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Store function

Sets one value.

## Syntax

``` syntax
void Store(
  in uint address,
  in uint value
);
```

## Parameters

<dl> <dt>

*address* \[in\]
</dt> <dd>

Type: **uint**

The input address in bytes, which must be a multiple of 4.

</dd> <dt>

*value* \[in\]
</dt> <dd>

Type: **uint**

One input value.

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

 

 




