---
title: Texture2DArray::mips.Operator    function
description: Returns a read-only resource variable. | Texture2DArray::mips.Operator    function
ms.assetid: 66639bf6-74dd-4c69-9cc1-74cc9314de57
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

# Texture2DArray::mips.Operator    function

Returns a read-only resource variable.

## Syntax

``` syntax
R mips.Operator[][](
  in uint mipSlice,
  in uint3 pos
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

Type: **uint3**

The index position. The first and second components contain the (x, y) coordinates. The third component indicates the desired array slice.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture2DArray<float4> tex;
uint mip = 2;
uint2 pos_xy_and_array = {123, 456, 3};
float4 f = tex.mips[mip][pos_xy_and_array];
        
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture2DArray](sm5-object-texture2darray.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




