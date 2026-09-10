---
title: QuadReadAcrossY function
description: Returns the specified source value read from the other lane in this quad in the Y direction.
ms.assetid: 6C03D1E6-433F-4CCA-A5EA-C3F34BB2B93B
keywords:
- QuadReadAcrossY function HLSL
topic_type:
- apiref
api_name:
- QuadReadAcrossY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# QuadReadAcrossY function

Returns the specified source value read from the other lane in this quad in the Y direction.

## Syntax

``` syntax
<type> QuadReadAcrossY(
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

This function is supported in pixel and compute shaders starting with shader model 6.0. In compute shaders targeting shader model 6.0 through 6.5, the mapping of threads to quads is implementation-dependent. Shader model 6.6 defines the quad layout for compute shaders and adds support for this function in amplification and mesh shaders.



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




