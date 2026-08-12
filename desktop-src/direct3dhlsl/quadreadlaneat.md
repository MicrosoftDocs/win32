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

The lane ID, in the range 0 through 3. The value must be uniform across the quad.

</dd> </dl>

## Return value

The value of *sourceValue* from the selected lane. The result is uniform across the quad. If *quadLaneID* is not uniform across the quad, or if the selected source lane is inactive, the result is undefined.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported in pixel shaders starting with shader model 6.0. It is supported in compute, amplification, and mesh shaders starting with shader model 6.6.



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




