---
title: EvaluateAttributeCentroid function
description: Evaluates at the pixel centroid.
ms.assetid: 6735b3f4-765f-4cd9-9f38-326a52709021
keywords:
- EvaluateAttributeCentroid function HLSL
topic_type:
- apiref
api_name:
- EvaluateAttributeCentroid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EvaluateAttributeCentroid function

Evaluates at the pixel centroid.

## Syntax

``` syntax
numeric EvaluateAttributeCentroid(
  in attrib numeric value
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **attrib numeric**

The input value.

</dd> </dl>

## Remarks

Interpolation mode can be **linear** or **linear\_no\_perspective** on the variable. Use of **centroid** or **sample** is ignored. Attributes with constant interpolation are also allowed, in which case the sample index is ignored.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




