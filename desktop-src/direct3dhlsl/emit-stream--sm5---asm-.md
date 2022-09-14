---
title: emit_stream (sm5 - asm)
description: Emit a vertex to a given stream.
ms.assetid: 5DBB0BEC-6EA4-4C04-A3D2-853E48260226
ms.topic: reference
ms.date: 05/31/2018
---

# emit\_stream (sm5 - asm)

Emit a vertex to a given stream.



| emit\_stream streamIndex |
|--------------------------|



 



| Item                                                                                                               | Description                         |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| <span id="streamIndex"></span><span id="streamindex"></span><span id="STREAMINDEX"></span>*streamIndex*<br/> | \[in\] The stream index.<br/> |



 

## Remarks

This instruction causes all declared o\# registers for the given stream to be read out of the geometry shader to generate a vertex. Afer the emit, all data in all output registers for all streams become uninitialized, not just the stream emitted to.

*streamIndex* must be an immediate value \[0..3\] for a declared stream.

As multiple **emit\_stream** calls are issued, primitives are generated.

### Restrictions

-   **emit\_stream** can appear any number of times in a geometry shader, including within flow control.
-   If streams have not been declared, then you must use [emit](emit--sm4---asm-.md) instead of **emit\_stream**.

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

 

 





