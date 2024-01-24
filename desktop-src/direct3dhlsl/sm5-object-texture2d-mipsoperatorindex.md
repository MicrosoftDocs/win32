---
title: Texture2D::mips.Operator    function
description: Returns a read-only resource variable. | Texture2D::mips.Operator    function
ms.assetid: 201996a7-741f-4457-ab77-9cd653f3682b
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

# Texture2D::mips.Operator    function

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

The index position. Contains the (x, y) coordinates.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture2D<float4> tex;
uint mip = 2;
uint2 pos_xy = {123, 456};
float4 f = tex.mips[mip][pos_xy];
        
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture2D](sm5-object-texture2d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




