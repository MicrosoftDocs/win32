---
title: RWByteAddressBuffer::Load3(uint) function
description: Gets three values. | RWByteAddressBuffer::Load3(uint) function
ms.assetid: cf8c4c5d-4748-43d7-896e-33ed07c94b9e
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

# RWByteAddressBuffer::Load3(uint) function

Gets three values.

## Syntax

``` syntax
uint3 Load3(
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

Type: **uint3**

Three values.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Load3 methods](rwbyteaddressbuffer-load3.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




