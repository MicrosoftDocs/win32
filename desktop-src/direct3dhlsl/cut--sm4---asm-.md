---
title: cut (sm4 - asm)
description: Geometry Shader instruction that completes the current primitive topology (if any vertices have been emitted), and starts a new topology of the type declared by the Geometry Shader.
ms.assetid: 9B28E33D-F518-4844-BE3F-BE61B5F08B4F
ms.topic: reference
ms.date: 05/31/2018
---

# cut (sm4 - asm)

Geometry Shader instruction that completes the current primitive topology (if any vertices have been emitted), and starts a new topology of the type declared by the Geometry Shader.



| cut |
|-----|



 

## Remarks

When **cut** is executed, the first thing that happens is that any previously emitted topology by the Geometry Shader invocation is completed. If not enough vertices were emitted for the previous primitive topology, they are discarded. Because the only available output topologies for the Geometry Shader are pointlist, linestrip, and trianglestrip, there are never any leftover vertices upon **cut**.

After the previous topology, if any, is completed, **cut** causes a new topology to begin, using the topology declared as the Geometry Shader output.

## Restrictions

-   The **cut** instruction applies only to the Geometry Shader.
-   **cut** can appear any number of times in the Geometry Shader, including within flow control.
-   If the Geometry Shader ends and vertices have been emitted, the topology they are building is completed, as if a **cut** was executed as the last instruction.
-   If streams have been declared, then [cut\_stream](cut-stream---sm5---asm-.md) must be used instead of **cut**.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               | x               |              |



 

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

 

 




