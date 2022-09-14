---
title: switch (sm4 - asm)
description: Transfers control to a different statement block within the switch body depending on the value of a selector.
ms.assetid: ECAEECFD-B955-4356-B5C9-1D6A04C71D8F
ms.topic: reference
ms.date: 05/31/2018
---

# switch (sm4 - asm)

Transfers control to a different statement block within the switch body depending on the value of a selector.



| switch src0.selected\_component |
|---------------------------------|



 



| Item                                                            | Description                                              |
|-----------------------------------------------------------------|----------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The selector for the switch statement.<br/> |



 

## Remarks

A **switch**/[endswitch](endswitch--sm4---asm-.md) construct behaves exactly as a **switch** construct in the C language, with the following exception: for D3D11 [case](case--sm4---asm-.md)/[default](default--sm4---asm-.md) statements that fall through to the next **case**/**default** without a [break](break--sm4---asm-.md) cannot have any code in them. It is permitted for multiple **case** statements, including **default**, to appear sequentially, sharing the same code block.

The condition must be a 32-bit register component or immediate quantity. The equality comparison is bitwise (integer).

As with any Shader instruction in the D3D11, hardware may or may not implement the **switch** construct directly.

**Switch** statements can be nested. Each **switch** block counts as 1 level against the flow control nesting depth limit of 64 per subroutine and main, independent of the number of **case** statements. The HLSL compiler will not generate subroutines that exceed this limit. Behavior of control flow instructions beyond 64 levels deep per subroutine is undefined.

The following example shows how to use this instruction.

``` syntax
                ...
                switch r0.x
                default: // falling through
                case 3
                    switch r1.x
                    case 4
                        ...
                        break
                    case 5
                        ...
                        break
                    endswitch
                    break
                case 0
                    break
                endswitch
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

 

 





