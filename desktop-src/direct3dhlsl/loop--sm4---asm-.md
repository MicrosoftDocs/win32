---
title: loop (sm4 - asm)
description: Specifies a loop which iterates until a break instruction is encountered.
ms.assetid: 0BEFADF4-036E-4FDA-9681-10965D6BA9FC
ms.topic: reference
ms.date: 05/31/2018
---

# loop (sm4 - asm)

Specifies a loop which iterates until a break instruction is encountered.



| loop |
|------|



 

## Remarks

**loop** can iterate indefinitely, although overall execution of the Shader may be forced to terminate after some number of instructions are executed.

Flow control blocks can nest up to 64 deep per subroutine and main. The HLSL compiler will not generate subroutines that exceed this limit. Behavior of control flow instructions beyond 64 levels deep per subroutine is undefined.

The token format contains the offset of the corresponding [endloop](endloop--sm4---asm-.md) instruction in the Shader as a convenience.

The following example shows how to use the loop instruction.

``` syntax
                loop
                    // example of termination condition
                    if_nz r0.x
                        break
                    endif
                    ...
                endloop
```

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

 

 




