---
title: Texture1DArray::mips.Operator    function
description: Returns a read-only resource variable. | Texture1DArray::mips.Operator    function
ms.assetid: b8f2ef78-4b50-4051-a00f-5b81cd77d1e0
keywords:
- mips.Operator function HLSL
topic_type:
- apiref
api_name:
- mips.Operator
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture1DArray::mips.Operator    function

Returns a read-only resource variable.

## Syntax

``` syntax
R mips.Operator[][](
  in uint mipSlice,
  in uint2 pos
);
```

## Parameters

<dl> <dt>

*mipSlice* \[in\]
</dt> <dd>

Type: **uint**

The mip slice index.

</dd> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint2**

The index position. The first component contains the x-coordinate. The second component indicates the desired array slice.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture1DArray<float4> tex;
uint mip = 2;
uint2 pos_x_and_array = {1234, 3};
float4 f = tex.mips[mip][pos_x_and_array];        
        
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture1DArray](sm5-object-texture1darray.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




