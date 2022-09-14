---
title: cut_stream (sm5 - asm)
description: The geometry shader instruction that completes the current primitive topology at the specified stream, if any vertices have been emitted to it, and starts a new topology of the type declared by the geometry shader at that stream.
ms.assetid: CEFDD13B-34FD-4E9C-94A0-CB8879A7DBDE
ms.topic: reference
ms.date: 05/31/2018
---

# cut\_stream (sm5 - asm)

The geometry shader instruction that completes the current primitive topology at the specified stream, if any vertices have been emitted to it, and starts a new topology of the type declared by the geometry shader at that stream.



| cut\_stream streamIndex |
|-------------------------|



 



| Item                                                                                                               | Description                         |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| <span id="streamIndex"></span><span id="streamindex"></span><span id="STREAMINDEX"></span>*streamIndex*<br/> | \[in\] The stream index.<br/> |



 

## Remarks

When this instruction is executed, any previously emitted topology by the geometry shader invocation is completed. If there are not enough vertices emitted for the previous primitive topology, then they are discarded. Because the only available output topologies for the geometry shader are pointlist, linestrip and trianglestrip, there are never any leftover vertices.

*streamIndex* must be an immediate value \[0..3\] for a declared stream.

After the previous topology, if any, is completed, this instruction causes a new topology to begin, using the topology declared as the output for the geometry shader.

### Restrictions

-   This instruction applies to the geometry shader only.
-   **cut\_stream** can appear any number of times in the geometry shader, including within flow control.
-   If the geometry shader ends and vertices have been emitted, the topology they are building is completed, as if a **cut\_stream** instruction was executed as the last instruction.
-   If streams have not been declared, you must use [cut](cut--sm4---asm-.md) instead of **cut\_stream**.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        | X        |       |         |



 

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

 

 





