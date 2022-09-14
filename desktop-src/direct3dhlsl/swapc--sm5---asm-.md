---
title: swapc (sm5 - asm)
description: Performs a component-wise conditional swap of the values between two input registers.
ms.assetid: 3DFCEB82-076E-4AFA-915F-47390A355B7C
ms.topic: reference
ms.date: 05/31/2018
---

# swapc (sm5 - asm)

Performs a component-wise conditional swap of the values between two input registers.



| swapc dest0\[.mask\], dest1\[.mask\], src0\[.swizzle\], src1\[.swizzle\], src2\[.swizzle\] |
|--------------------------------------------------------------------------------------------|



 



| Item                                                               | Description                                                                                     |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="dest0"></span><span id="DEST0"></span>*dest0*<br/> | \[in\] Register with arbitrary nonempty write masks. Must be different than *dest1*.<br/> |
| <span id="dest1"></span><span id="DEST1"></span>*dest1*<br/> | \[in\] Register with arbitrary nonempty write masks. Must be different than *dest0*.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>    | \[in\] Provides 4 conditions. A nonzero integer value means **true**. <br/>               |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/>    | \[in\] One of the values to be swapped.<br/>                                              |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/>    | \[in\] One of the values to be swapped.<br/>                                              |



 

## Remarks

The encoding of this instruction attempts to compactly express multiple parallel conditional swaps of scalars across two 4-component registers, with minor flexibility in the arrangement of the pairs of numbers involved in swapping.

The choice of register and value for *src0*, *src1*, and *src2* are unconstrained in any way, like [movc](movc--sm4---asm-.md).

The semantics of this instruction can be described by the equivalent operations with the **movc** instruction. The worst case is shown in the following example, making sure destination registers are not updated until the end.

``` syntax
                swapc dest0[.mask], 
                      dest1[.mask],
                      src0[.swizzle],
                      src1[.swizzle],
                      src2[.swizzle]

                expands to:

                movc temp[dest0 s mask], 
                     src0[.swizzle], 
                     src2[.swizzle], src1[.swizzle]

                movc dest1[.mask], 
                     src0[.swizzle], 
                     src1[.swizzle], src2[.swizzle]

                mov  dest0.mask, temp
```

You can choose how to tackle the task, if not directly. For example, the same effect can be achieved by a sequence of up to 4 simple scalar conditional swaps, or as above, two vector **movc** instructions, plus any overhead to make sure the source values are not clobbered by earlier operations in the midst of the expansion.

Use this instruction for sorting.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





