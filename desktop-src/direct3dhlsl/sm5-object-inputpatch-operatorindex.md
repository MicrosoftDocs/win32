---
title: InputPatch::Operator  function
description: Returns the nth control point in the patch. | InputPatch::Operator  function
ms.assetid: 2c1eda6b-a9c1-40d3-be91-7a2e8f1da9fc
keywords:
- Operator function HLSL
topic_type:
- apiref
api_name:
- Operator
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InputPatch::Operator  function

Returns the *n*<sup>th</sup> control point in the patch.

## Syntax

``` syntax
T Operator[](
  in uint n
);
```

## Parameters

<dl> <dt>

*n* \[in\]
</dt> <dd>

Type: **uint**

The input index.

</dd> </dl>

## Return value

Type: **T**

The *n*<sup>th</sup> control point.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    |        |          |       |         |



 

## See also

<dl> <dt>

[InputPatch](sm5-object-inputpatch.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




