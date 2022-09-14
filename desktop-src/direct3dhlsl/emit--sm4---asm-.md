---
title: emit (sm4 - asm)
description: Emit a vertex.
ms.assetid: FDD18CCD-8088-46BD-897C-434B77FF81E6
ms.topic: reference
ms.date: 05/31/2018
---

# emit (sm4 - asm)

Emit a vertex.



| emit |
|------|



 

## Remarks

**emit** causes all declared o\# registers to be read out of the Geometry Shader to generate a vertex.

As multiple **emit** calls are issued, primitives are generated.

**emit** can appear any number of times in a Geometry Shader, including within flow control.

If streams have been declared, you must use [emit\_stream](emit-stream--sm5---asm-.md).

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               | x               |              |



 

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 




