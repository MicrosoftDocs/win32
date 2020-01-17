---
title: retc (sm4 - asm)
description: Conditional return.
ms.assetid: D936099D-4A75-4AE2-9FE3-70ED213DF4D9
ms.topic: reference
ms.date: 05/31/2018
---

# retc (sm4 - asm)

Conditional return.



| retc{\_z\|\_nz} src0.select\_component |
|----------------------------------------|



 



| Item                                                            | Description                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The register to test the condition against.<br/> |



 

## Remarks

If within a subroutine, this instruction conditionally returns to the instruction after the call. If not inside a subroutine, this instruction terminates program execution.

The following example shows how to use this instruction.

``` syntax
           ...
           call l3
           ...
           ret
           label l3
               ...
               retc_nz r0.x  // If any bit in r0.x is nonzero, then return
               retc_z  r1.x  // If all bits in r0.x are zero, then return.
               ...
           ret
```

### Restrictions

-   **retc** can appear anywhere in a program, any number of times.
-   The last instruction in a main program or subroutine cannot be a **retc\_z** or **retc\_nz**. Instead, the unconditional [ret](ret--sm4---asm-.md) can be used.
-   The 32-bit register supplied by *src0* is tested at a bit level. If any bit is nonzero, **ret\_nz** will return. If all bits are zero, **retc\_z** will return.

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

 

 





