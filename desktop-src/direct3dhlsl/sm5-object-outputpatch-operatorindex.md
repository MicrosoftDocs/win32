---
title: OutputPatch::Operator  function
description: Returns the nth control point in the patch. | OutputPatch::Operator  function
ms.assetid: 3ac15fe8-8bab-46a2-8826-61ade927c99e
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

# OutputPatch::Operator  function

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
|        | x    | x      |          |       |         |



 

## See also

<dl> <dt>

[OutputPatch](sm5-object-outputpatch.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




