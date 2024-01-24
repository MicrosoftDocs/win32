---
title: ByteAddressBuffer::Load(int) function
description: Gets one value. | ByteAddressBuffer::Load(int) function
ms.assetid: a63f4099-2c3b-4d37-9135-b8c63df30824
keywords:
- Load function HLSL
topic_type:
- apiref
api_name:
- Load
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ByteAddressBuffer::Load(int) function

Gets one value.

## Syntax

``` syntax
uint Load(
  in int address
);
```

## Parameters

<dl> <dt>

*address* \[in\]
</dt> <dd>

Type: **int**

The input address in bytes, which must be a multiple of 4.

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

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




