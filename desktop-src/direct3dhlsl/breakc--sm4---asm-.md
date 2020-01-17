---
title: breakc (sm4 - asm)
description: Conditionally moves the point of execution to the instruction after the next endloop or endswitch.
ms.assetid: 5735EF88-1E8C-4142-8442-9328D78999A7
ms.topic: reference
ms.date: 05/31/2018
---

# breakc (sm4 - asm)

Conditionally moves the point of execution to the instruction after the next [endloop](endloop--sm4---asm-.md) or [endswitch](endswitch--sm4---asm-.md).



| breakc{\_z\|\_nz} src0.select\_component |
|------------------------------------------|



 



| Item                                                            | Description                                                     |
|-----------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The component on which to test the condition.<br/> |



 

## Remarks

The token format contains the offset of the corresponding **endloop** instruction in the Shader as a convenience.

The following example shows the**breakc** instruction.


```
                loop
                    // example of termination condition
                    breakc_z  r0.x // break if all bits in r0.x are 0
                    breakc_nz r1.x // break if any bit in r1.x is nonzero
                    ...
                endloop

```



This instruction must appear within a **loop**/**endloop** or **switch**/**endswitch**.

The 32-bit register supplied by *src0* is tested at a bit level. If any bit is nonzero, **breakc\_nz** will perform the break. If all bits are zero, **breakc\_z** will perform the break.

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

 

 





