---
title: RWByteAddressBuffer::Store2 function
description: Sets two values.
ms.assetid: 7b32c84c-9ea2-47ae-a0f3-df6d95249163
keywords:
- Store2 function HLSL
topic_type:
- apiref
api_name:
- Store2
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Store2 function

Sets two values.

## Syntax

``` syntax
void Store2(
  in uint address,
  in uint2 values
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

Type: **uint2**

Two input values.

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

 

 




