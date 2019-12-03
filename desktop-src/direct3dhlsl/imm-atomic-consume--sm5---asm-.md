---
title: imm_atomic_consume (sm5 - asm)
description: Atomically decrement the hidden 32-bit counter stored with a Count or Append unordered access view (UAV), returning the new value.
ms.assetid: 1115C318-2F86-4161-AC5C-2A61A262DC28
ms.topic: reference
ms.date: 05/31/2018
---

# imm\_atomic\_consume (sm5 - asm)

Atomically decrement the hidden 32-bit counter stored with a Count or Append unordered access view (UAV), returning the new value.



| imm\_atomic\_consume dst0\[.single\_component\_mask\], dstUAV |
|---------------------------------------------------------------|



 



| Item                                                                                           | Description                                                               |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <span id="dst0"></span><span id="DST0"></span>*dst0*<br/>                                | \[in\] Contains the returned original counter value.<br/>           |
| <span id="dstUAV"></span><span id="dstuav"></span><span id="DSTUAV"></span>*dstUAV*<br/> | \[in\] A structured buffer UAV with the Count or Append flag. <br/> |



 

## Remarks

See [imm\_atomic\_alloc](imm-atomic-alloc--sm5---asm-.md) for a discussion about the validity of the returned count value depending on whether the UAV is Count or Append. The same applies for **imm\_atomic\_consume**.

**imm\_atomic\_consume** does an atomic decrement of the counter value, returning the new value to *dst0*.

There is no clamping of the count, so it wraps on underflow.

The same shader cannot attempt both **imm\_atomic\_alloc** and **imm\_atomic\_consume** on the same UAV. Further, the GPU cannot allow multiple shader invocations to mix **imm\_atomic\_alloc** and **imm\_atomic\_consume** on the same UAV.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, this instruction applies to all shader stages for the Direct3D 11.1 runtime, which is available starting with Windows 8.



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

 

 





