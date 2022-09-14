---
title: AllMemoryBarrierWithGroupSync function
description: Blocks execution of all threads in a group until all memory accesses have been completed and all threads in the group have reached this call.
ms.assetid: 831830e7-19ce-41d0-b555-44a083b67cdc
keywords:
- AllMemoryBarrierWithGroupSync function HLSL
topic_type:
- apiref
api_name:
- AllMemoryBarrierWithGroupSync
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# AllMemoryBarrierWithGroupSync function

Blocks execution of all threads in a group until all memory accesses have been completed and all threads in the group have reached this call.

## Syntax

``` syntax
void AllMemoryBarrierWithGroupSync(void);
```

## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

A memory barrier guarantees that outstanding memory operations have completed. Threads are synchronized at GroupSync barriers. This may stall a thread or threads if memory operations are in progress.

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

 

 




