---
title: Texture3D::mips.Operator    function
description: Returns a read-only resource variable. | Texture3D::mips.Operator    function
ms.assetid: d5f6cb3b-4163-44c2-8379-ac8a412b1aa6
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

# Texture3D::mips.Operator    function

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

The index position. Contains the (x, y, z) coordinates.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

### Usage Example


```
Texture3D<float4> tex;
uint mip = 2;
uint3 pos_xyz = {123, 456, 789};
float4 f = tex.mips[mip][pos_xyz];
        
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture3D](sm5-object-texture3d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




