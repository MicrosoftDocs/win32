---
title: DeviceMemoryBarrierWithGroupSync function
description: Blocks execution of all threads in a group until all device memory accesses have been completed and all threads in the group have reached this call.
ms.assetid: 77c54064-a996-4c51-84b5-7da60e884c4f
keywords:
- DeviceMemoryBarrierWithGroupSync function HLSL
topic_type:
- apiref
api_name:
- DeviceMemoryBarrierWithGroupSync
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DeviceMemoryBarrierWithGroupSync function

Blocks execution of all threads in a group until all device memory accesses have been completed and all threads in the group have reached this call.

## Syntax

``` syntax
void DeviceMemoryBarrierWithGroupSync(void);
```

## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          |       | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




