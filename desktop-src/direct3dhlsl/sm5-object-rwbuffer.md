---
title: RWBuffer
description: A read/write buffer.
ms.assetid: e9b60e63-5b2b-4f45-834b-269e692ba84c
keywords:
- RWBuffer HLSL
topic_type:
- apiref
api_name:
- RWBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWBuffer

A read/write buffer.



| Method                                                     | Description                            |
|------------------------------------------------------------|----------------------------------------|
| [**GetDimensions**](sm5-object-rwbuffer-getdimensions.md) | Gets the resource dimensions.          |
| [**Load**](rwbuffer-load.md)                              | Gets one value in a read-write buffer. |
| [**Operator\[\]**](sm5-object-rwbuffer-operatorindex.md)  | Returns a resource variable.           |



 

A resource variable can also be passed into any unordered or interlocked operation.

**RWBuffer** objects can be prefixed with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will flush a UAV only within the current group.

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

 




