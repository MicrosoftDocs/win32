---
title: RWByteAddressBuffer::Load4(uint) function
description: Gets four values. | RWByteAddressBuffer::Load4(uint) function
ms.assetid: b46cd119-75be-4c2d-82f9-5dcabd7e4400
keywords:
- Load4 function HLSL
topic_type:
- apiref
api_name:
- Load4
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWByteAddressBuffer::Load4(uint) function

Gets four values.

## Syntax

``` syntax
uint4 Load4(
  in uint address
);
```

## Parameters

<dl> <dt>

*address* \[in\]
</dt> <dd>

Type: **uint**

The input address in bytes, which must be a multiple of 4.

</dd> </dl>

## Return value

Type: **uint4**

Four values.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load4 methods](rwbyteaddressbuffer-load4.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




