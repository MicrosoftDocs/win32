---
title: QuadReadLaneAt function
description: Returns the specified source value from the lane identified by the lane ID within the current quad.
ms.assetid: 5CD7EE4C-E64E-46A3-ABDC-1BF65D0F96BE
keywords:
- QuadReadLaneAt function HLSL
topic_type:
- apiref
api_name:
- QuadReadLaneAt
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# QuadReadLaneAt function

Returns the specified source value from the lane identified by the lane ID within the current quad.

## Syntax


``` syntax
<type> QuadReadLaneAt(
   <type> sourceValue,
   uint   quadLaneID  
);
```



## Parameters

<dl> <dt>

*sourceValue* 
</dt> <dd>

The requested type.

</dd> <dt>

*quadLaneID* 
</dt> <dd>

The lane ID, in the range 0 through 3.

</dd> </dl>

## Return value

The value of *sourceValue* from the selected lane. If the selected source lane is inactive, the result is undefined.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported in pixel and compute shaders starting with shader model 6.0. In compute shaders targeting shader model 6.0 through 6.5, the mapping of threads to quads is implementation-dependent. Shader model 6.6 defines the quad layout for compute shaders and adds support for this function in amplification and mesh shaders.



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




