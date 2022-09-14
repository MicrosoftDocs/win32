---
title: ubfe (sm5 - asm)
description: Given a range of bits in a number, shift those bits to the LSB and set remaining bits to 0.
ms.assetid: CC6BE378-2726-47A2-8E23-B8151521F72D
ms.topic: reference
ms.date: 05/31/2018
---

# ubfe (sm5 - asm)

Given a range of bits in a number, shift those bits to the LSB and set remaining bits to 0.



| ubfe dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\], src2\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                    |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] Contains the results of the instruction.<br/>                     |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The LSB 5 bits provide the bitfield width (0-31).<br/>            |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The LSB 5 bits of *src1* provide the bitfield offset (0-31).<br/> |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The number to shift.<br/>                                         |



 

## Remarks

``` syntax
 
        Given width, offset:
                if( width == 0 )
                {
                    dest = 0
                }
                else if( width + offset < 32 )
                {
                    shl dest, src2, 32-(width+offset)
                    ushr dest, dest, 32-width
                }
                else
                {
                    ushr dest, src2, offset
                }
```

Use this instruction to unpack unsigned integers or flags.

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

 

 





