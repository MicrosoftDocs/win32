---
title: ret (sm4 - asm)
description: Return statement.
ms.assetid: 1B690036-99C5-441D-9DD3-E09D43E48AFF
ms.topic: reference
ms.date: 05/31/2018
---

# ret (sm4 - asm)

Return statement.



| ret |
|-----|



 

## Remarks

If within a subroutine, return to the instruction after the call. If not inside a subroutine, terminate program execution.

The following example shows how to use this instruction.

``` syntax
 
               ...
                call l3
                ...
                ret
                label l3
                    ...
                ret
```

### Restrictions

-   **ret** can appear anywhere in a program, any number of times.
-   If a [label](label--sm4---asm-.md) instruction appears in a Shader, it must be preceded by a **ret** command that is not nested in any flow control statements.
-   If there are subroutines in a Shader, the last instruction in the Shader must be a **ret**.

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

 

 




