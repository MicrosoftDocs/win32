---
title: atomic_cmp_store (sm5 - asm)
description: Atomic compare and write to memory.
ms.assetid: 1B97E983-11A9-47E4-B274-E94083837C6E
ms.topic: reference
ms.date: 05/31/2018
---

# atomic\_cmp\_store (sm5 - asm)

Atomic compare and write to memory.



| atomic\_cmp\_store dst, dstAddress\[.swizzle\], src0\[.select\_component\], src1\[.select\_component\] |
|--------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                           | Description                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dst"></span><span id="DST"></span>*dst*<br/>                                                   | \[in\] The components to compare with *src0*. This value must be an unordered access view (UAV) (u\#). In the compute shader it can also be thread group shared memory (g\#). <br/> |
| <span id="dstAddress"></span><span id="dstaddress"></span><span id="DSTADDRESS"></span>*dstAddress*<br/> | \[in\] The memory address.<br/>                                                                                                                                                     |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                | \[in\] The 32-bit value to compare with *dst*.<br/>                                                                                                                                 |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>                                                | \[in\] The value to write to memory if the compared values are identical. <br/>                                                                                                     |



 

## Remarks

This instruction performs a single component 32-bit value compare of operand *src0* with *dst* at 32-bit per component address *dstAddress*.

If the compared values are identical, the single-component 32-bit value in *src1* is written to destination memory. Otherwise, the destination is not changed.

The entire compare and write operation is performed atomically.

If *dst* is a u\#, it can be declared as raw, typed or structured. If typed, it must be declared as UINT/SINT with the bound resource format being R32\_UINT/\_SINT.

If *dst* is g\#, it must be declared as raw or structured.

The number of components taken from the address is determined by the dimensionality of dst u\# or g\#.

Nothing is returned to the shader.

If the shader invocation is inactive, for example if the pixel has been discarded earlier in its execution, or a pixel/sample instruction does not alter the *dst* memory at all (silently).

Out of bounds addressing on u\# causes nothing to be written to memory, except if the u\# is structured, and byte offset into the struct (second component of the address) is causing the out of bounds access, then the entire contents of the UAV become undefined.

Out of bounds addressing on g\# (the bounds of that particular g\#, as opposed to all shared memory) causes the entire contents of all shared memory to become undefined.

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

 

 





