---
title: case (sm4 - asm)
description: A label in a switch instruction.
ms.assetid: 456BB918-327E-4E15-8D38-F53850CAF666
ms.topic: reference
ms.date: 05/31/2018
---

# case (sm4 - asm)

A label in a switch instruction.



| case \[32-bit immediate\] |
|---------------------------|



 

## Remarks

Because falling through **cases** is valid only if there is no code added, multiple **cases** (including [default](default--sm4---asm-.md)) can share the same code block.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

## Minimum Shader Model

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

 

 




