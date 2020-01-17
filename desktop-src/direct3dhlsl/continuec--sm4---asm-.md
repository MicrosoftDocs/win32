---
title: continuec (sm4 - asm)
description: Conditionally continues execution at the beginning of the current loop.
ms.assetid: 1A5B1951-CE1E-479C-AE0F-FC5FB93E0DE9
ms.topic: reference
ms.date: 05/31/2018
---

# continuec (sm4 - asm)

Conditionally continues execution at the beginning of the current loop.



| continuec{\_z\|\_nz} src0.select\_component |
|---------------------------------------------|



 



| Term                                                            | Description                                                          |
|-----------------------------------------------------------------|----------------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The component against which to test the condition.<br/> |



 

## Remarks

**continuec** can be used only inside a [loop](loop--sm4---asm-.md) or [endloop](endloop--sm4---asm-.md).

The following example shows how to use the **continuec** instruction.


```
                loop
                    if_na r0.x
                        break
                    endif
                    continuec_z r1.x  // if all bits of r1.x are zero then
                                      // continue at beginning of loop.
                    ...
                    continuec_nz r3.y // if any bit in r3.y is set then
                                      // continue at beginning of loop.

                    ...
                endloop

```



The token format contains the offset of the corresponding loop instruction in the Shader as a convenience.

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

 

 





