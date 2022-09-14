---
title: SV_GroupThreadID
description: Indices for which an individual thread within a thread group a compute shader is executing in.
ms.assetid: be944592-c4ea-43c9-88bc-98a9a190a437
keywords:
- SV_GroupThreadID HLSL
topic_type:
- apiref
api_name:
- SV_GroupThreadID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SV\_GroupThreadID

Indices for which an individual thread within a thread group a compute shader is executing in. SV\_GroupThreadID varies across the range specified for the compute shader in the [numthreads](sm5-attributes-numthreads.md) attribute. For example if numthreads(3,2,1) was specified possible values for the SV\_GroupThreadID input value have this range of values (0-2,0-1,0).

## Type



| Type      |
|-------|
| uint3 |



 

## Remarks

This system value is optional, and is always within the bounds of the values passed into the [numthreads](sm5-attributes-numthreads.md) attribute.

The following illustration shows the relationship between the parameters passed to [**Dispatch**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-dispatch), Dispatch(5,3,2), the values specified in the [numthreads](sm5-attributes-numthreads.md) attribute, numthreads(10,8,3), and values that will passed to the compute shader for the thread-related system values ([SV\_GroupIndex](sv-groupindex.md),[SV\_DispatchThreadID](sv-dispatchthreadid.md),SV\_GroupThreadID,[SV\_GroupID](sv-groupid.md)).

![illustration of the relationship between dispatch, thread groups, and threads](images/threadgroupids.png)

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          |       | x       |



 

## See also

<dl> <dt>

[Semantics](dx-graphics-hlsl-semantics.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 
