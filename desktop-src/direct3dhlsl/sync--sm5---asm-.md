---
title: sync (sm5 - asm)
description: Thread group sync or memory barrier.
ms.assetid: DCA637FE-8F5C-41D0-8B5E-F913463BA387
ms.topic: reference
ms.date: 05/31/2018
---

# sync (sm5 - asm)

Thread group sync or memory barrier.



| sync\[\_uglobal\|\_ugroup\]\[\_g\]\[\_t\] |
|-------------------------------------------|



 

## Remarks

**Sync** has options \_uglobal, \_ugroup, \_g and \_t.

In the pixel shader, only **sync\_uglobal** is allowed.

In the compute shader, (\_uglobal or \_ugroup\*) and/or \_g must be specified. \_t is optional in addition.

### \_uglobal

Global u\# (UAV) memory fence.

All prior u\# memory reads/writes by this thread in program order are made visible to all threads on the entire GPU before any subsequent u\# memory accesses by this thread. The entire GPU part of the definition is replaced by a less-than-global scope in one case, described below.

This applies to all UAV memory bound at the current shader stage.

\_uglobal is available in the compute shader or pixel shader.

For any bound UAV that has not been declared by the shader as Globally Coherent, the \_uglobal u\# memory fence only has visibility within the current compute shader thread-group for that UAV, as if it is \_ugroup instead of \_uglobal. This issue only applies to the compute shader, since the pixel shader must declare all UAVs as Globally Coherent.

### \_ugroup

Thread group scope u\# (UAV) memory fence.

All prior u\# memory reads or writes by this thread in program order are made visible to all threads in the thread group before any subsequent u\# memory accesses by this thread.

This applies to all UAV memory bound at the current shader stage.

\_ugroup is available in the compute shader only.

If \_ugroup is exposed, for some implementations. The advantage of specifying \_ugroup instead of \_uglobal is that the **sync** operation can complete more quickly.

Other implementations do not distinguish \_ugroup from \_uglobal, so both operations are equivalent and behave like \_uglobal. Applications can specify their intent by requesting the narrowest scope of **sync** necessary.

Even if a particular UAV is declared as Globally Coherent, a \_ugroup **sync** operation will function more efficiently on that UAV if a global barrier is not required.

### \_g

g\# (thread group shared memory) fence.

All prior g\# memory reads or writes by this thread in program order are made visible to all threads in the thread group before any subsequent g\# memory accesses by this thread.

This applies to all of the current thread group's g\# shared memory.

\_g is available in the compute shader only.

### \_t

Thread group sync. All threads within a single thread group (those that can share access to a common set of shared register space) will be executed up to the point where they reach this instruction before any thread can continue.

\_t cannot be placed in dynamic flow control, (branches which could vary within a thread group), but can be present in uniform flow control, where all threads in the group pick the same path.

\_t is available in the compute shader only.

The following is a listing of compute shader ‘sync’ variants.

-   sync\_g
-   sync\_ugroup\*
-   sync\_uglobal
-   sync\_g\_t
-   sync\_ugroup\_t\*
-   sync\_uglobal\_t
-   sync\_ugroup\_g\*
-   sync\_uglobal\_g
-   sync\_ugroup\_g\_t\*
-   sync\_uglobal\_g\_t

\*Variants with \_ugroup may not be targeted by the HLSL compiler, per the earlier discussion in the \_ugroup section above.

Listing of pixel shader sync variants include sync\_uglobal only.

Memory fences prevent affected instructions from being reordered by compilers or hardware across the fence.

Multiple reads from the same address by a shader invocation that are not separated by memory barriers or writes to the address can be collapsed together. The same applies to writes. Accesses separated by a barrier cannot be merged or moved across the barrier.

Memory fences are not necessary for atomic operations to a given address by different threads to function correctly. Fences are needed when atomics and/or load/store operations need to be synchronized with respect to each other as they appear in individual threads from the point of view of other threads.

In the pixel shader, [discard](discard--sm4---asm-.md) instructions imply a sync\_uglobal fence, in that instructions cannot be reordered across the **discard**. sync\_uglobal in helper pixels (which run only to support derivatives) or discarded pixels may or may not have any affect. It is not allowed for helper or discarded pixels to write to UAVs if, in the case of discard, the writes are issued after the discard. Returned values from UAVs are not allowed to contribute to derivative calculations. Therefore whether or not sync\_u is honored for helper pixels or when issued after a discard is moot.

cs\_4\_0 and cs\_4\_1 support this instruction.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, the **sync\_uglobal** variant of this instruction applies to all shader stages for the Direct3D 11.1 runtime, which is available starting with Windows 8.



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 




