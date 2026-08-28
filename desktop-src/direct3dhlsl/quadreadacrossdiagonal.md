---
title: QuadReadAcrossDiagonal function
description: Returns the specified local value which is read from the diagonally opposite lane in this quad.
ms.assetid: 2914F1F9-5CE2-437A-ADDB-4955D2C1490B
keywords:
- QuadReadAcrossDiagonal function HLSL
topic_type:
- apiref
api_name:
- QuadReadAcrossDiagonal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# QuadReadAcrossDiagonal function

Returns the specified local value which is read from the diagonally opposite lane in this quad.

## Syntax


``` syntax
<type> QuadReadAcrossDiagonal(
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

The specified local value which is read from the diagonally opposite lane in this quad.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported in pixel and compute shaders starting with shader model 6.0. In compute shaders targeting shader model 6.0 through 6.5, the mapping of threads to quads is implementation-dependent. Shader model 6.6 defines the quad layout for compute shaders and adds support for this function in amplification and mesh shaders.



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




