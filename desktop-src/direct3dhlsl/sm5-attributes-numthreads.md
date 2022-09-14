---
title: numthreads
description: Defines the number of threads to be executed in a single thread group when a compute shader is dispatched (see ID3D11DeviceContext Dispatch).
ms.assetid: ec6b751c-d81c-4221-ae80-166d2a3707fe
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# numthreads

Defines the number of threads to be executed in a single thread group when a compute shader is dispatched (see [**ID3D11DeviceContext::Dispatch**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-dispatch)).


```
numthreads(X, Y, Z)    
```



The X, Y and Z values indicate the size of the thread group in a particular direction and the total of X\*Y\*Z gives the number of threads in the group. The ability to specify the size of the thread group across three dimensions allows individual threads to be accessed in a manner that logically 2D and 3D data structures.

For example, if a compute shader is doing 4x4 matrix addition then numthreads could be set to numthreads(4,4,1) and the indexing in the individual threads would automatically match the matrix entries. The compute shader could also declare a thread group with the same number of threads (16) using numthreads(16,1,1), however it would then have to calculate the current matrix entry based on the current thread number.

The allowable parameter values for **numthreads** depends on the compute shader version.



| Compute Shader | Maximum Z | Maximum Threads (X\*Y\*Z) |
|----------------|-----------|---------------------------|
| cs\_4\_x       | 1         | 768                       |
| cs\_5\_0       | 64        | 1024                      |



 

The following illustration shows the relationship between the parameters passed to [**ID3D11DeviceContext::Dispatch**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-dispatch), Dispatch(5,3,2), the values specified in the numthreads attribute, numthreads(10,8,3), and values that will passed to the compute shader for the thread related system values ([SV\_GroupIndex](sv-groupindex.md),[SV\_DispatchThreadID](sv-dispatchthreadid.md),[SV\_GroupThreadID](sv-groupthreadid.md),[SV\_GroupID](sv-groupid.md)).

![illustration of the relationship between dispatch, thread groups, and threads](images/threadgroupids.png)

This attribute is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          |       | x       |



 

## Related topics

<dl> <dt>

[Shader Model 5 Attributes](d3d11-graphics-reference-sm5-attributes.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 