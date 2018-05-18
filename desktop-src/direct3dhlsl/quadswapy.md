---
title: QuadReadAccrossY function
description: Returns the specified source value read from the other lane in this quad in the Y direction.
ms.assetid: '6C03D1E6-433F-4CCA-A5EA-C3F34BB2B93B'
keywords: ["QuadSwapY function HLSL"]
topic_type:
- apiref
api_name:
- QuadSwapY
api_type:
- NA
---

# QuadReadAccrossY function

Returns the specified source value read from the other lane in this quad in the Y direction.

## Syntax

``` syntax
<type> QuadSwapY(
   <type> localValue
);
```

## Parameters

<dl> <dt>

*localValue* 
</dt> <dd>

The requested type.

</dd> </dl>

## Return value

The specified source value. If the source lane is inactive, the results are undefined.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




