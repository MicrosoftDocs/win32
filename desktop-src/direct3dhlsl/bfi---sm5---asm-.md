---
title: bfi (sm5 - asm)
description: Given a bit range from the LSB of a number, place that number of bits in another number at any offset.
ms.assetid: BA84C882-A141-4AD2-8FD9-C60F1483FC65
ms.topic: reference
ms.date: 05/31/2018
---

# bfi (sm5 - asm)

Given a bit range from the LSB of a number, place that number of bits in another number at any offset.



| bfi dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\], src2\[.swizzle\], src3\[.swizzle\] |
|-------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                         |
|-----------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results.<br/>                       |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The bitfield width to take from *src2*.<br/>           |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The bitfield offset for replacing bits in *src3*.<br/> |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The number the bits are taken from. <br/>              |
| <span id="src3"></span><span id="SRC3"></span>*src3*<br/> | \[in\] The number with bits to be replaced.<br/>              |



 

## Remarks

The LSB 5 bits of *src0* provide the bitfield width (0-31) to take from *src2*.

The LSB 5 bits of *src1* provide the bitfield offset (0-31) to start replacing bits in the number read from *src3*.

``` syntax
Given width, offset:
                bitmask = (((1 << width)-1) << offset) & 0xffffffff
                dest = ((src2 << offset) & bitmask) | (src3 & ~bitmask)
```

This instruction is used for packing integers or flags.

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

 

 





