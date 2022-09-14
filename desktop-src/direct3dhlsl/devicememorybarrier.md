---
title: DeviceMemoryBarrier function
description: Blocks execution of all threads in a group until all device memory accesses have been completed.
ms.assetid: 904ab8f6-4849-4b13-8fac-3967cf66574e
keywords:
- DeviceMemoryBarrier function HLSL
topic_type:
- apiref
api_name:
- DeviceMemoryBarrier
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DeviceMemoryBarrier function

Blocks execution of all threads in a group until all device memory accesses have been completed.

## Syntax

``` syntax
void DeviceMemoryBarrier(void);
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
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




