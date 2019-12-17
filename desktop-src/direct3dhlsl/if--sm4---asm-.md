---
title: if (sm4 - asm)
description: Branch based on logical OR result.
ms.assetid: 9F4CF9E0-4D9D-4300-B432-432C560F34BB
ms.topic: reference
ms.date: 05/31/2018
---

# if (sm4 - asm)

Branch based on logical OR result.



| if{\_z\|\_nz} src0.select\_component |
|--------------------------------------|



 



| Item                                                            | Description                                                              |
|-----------------------------------------------------------------|--------------------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] Contains the component on which to test the condition.<br/> |



 

## Remarks

The token format contains the offset of the corresponding endif instruction in the Shader as a convenience.

The following example shows how to use this instruction.

``` syntax
                if_z r0.x // if all bits in r0.x are zero
                   ...
                else // (optional)
                   ...
                endif
                if_nz r1.x // if any bit in r0.x is nonzero
                   ...
                else // (optional)
                   ...
                endif
```

### Restrictions

-   The source operands (if 4 component vectors) must use a single component selector.
-   The 32-bit register supplied by *src0* is tested at a bit level. If any bit is nonzero, **if\_z** will be true. If all bits are zero, **if\_nz** will be true.
-   Flow control blocks can nest up to 64 deep per subroutine (and main). The HLSL compiler will not generate subroutines that exceed this limit. Behavior of control flow instructions beyond 64 levels deep (per subroutine) is undefined.

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

 

 





