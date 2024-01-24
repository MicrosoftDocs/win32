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

The lane ID; this will be a value from 0 to 3.

</dd> </dl>

## Return value

The specified source value. The result of this function is uniform across the quad. If the source lane is inactive, the results are undefined.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported from shader model 6.0 only in pixel and compute shaders.



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




