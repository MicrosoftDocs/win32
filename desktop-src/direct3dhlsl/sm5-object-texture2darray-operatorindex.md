---
title: Operator  function
description: Returns a read-only resource variable.
ms.assetid: eb6ff496-c46f-405f-a172-ab747415a2f9
keywords:
- Operator function HLSL
topic_type:
- apiref
api_name:
- Operator
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# Operator\[\] function

Returns a read-only resource variable.

## Syntax

``` syntax
R Operator[](
  in uint3 pos
);
```

## Parameters

<dl> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint3**

The index position. The first and second components contain the (x, y) coordinates. The third component indicates the desired array slice.

</dd> </dl>

## Return value

Type: **R**

A read-only resource variable.

## Remarks

This method always accesses the first mip level. To specify other mip levels, use the [**mip.operator\[\]\[\]**](sm5-object-texture2darray-mipsoperatorindex.md) method instead.

The texture samples can be used for bilinear interpolation.

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

 

 




