---
title: GroupMemoryBarrierWithGroupSync function
description: Blocks execution of all threads in a group until all group shared accesses have been completed and all threads in the group have reached this call.
ms.assetid: 64dd78e1-c597-4bd0-8a9b-592123178de5
keywords:
- GroupMemoryBarrierWithGroupSync function HLSL
topic_type:
- apiref
api_name:
- GroupMemoryBarrierWithGroupSync
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GroupMemoryBarrierWithGroupSync function

Blocks execution of all threads in a group until all group shared accesses have been completed and all threads in the group have reached this call.

## Syntax

``` syntax
void GroupMemoryBarrierWithGroupSync(void);
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

 

 




