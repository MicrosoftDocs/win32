---
title: ByteAddressBuffer::Load3(uint) function
description: Gets three values. | ByteAddressBuffer::Load3(uint) function
ms.assetid: 79afeb36-e0e7-44a2-b252-8e3577f4c1a5
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

# ByteAddressBuffer::Load3(uint) function

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
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Load3 methods](byteaddressbuffer-load3.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




