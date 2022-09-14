---
title: GroupMemoryBarrier function
description: Blocks execution of all threads in a group until all group shared accesses have been completed.
ms.assetid: cebd4277-47a0-401a-bfbe-8d956412f254
keywords:
- GroupMemoryBarrier function HLSL
topic_type:
- apiref
api_name:
- GroupMemoryBarrier
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GroupMemoryBarrier function

Blocks execution of all threads in a group until all group shared accesses have been completed.

## Syntax

``` syntax
void GroupMemoryBarrier(void);
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

 

 




