---
title: ibfe (sm5 - asm)
description: Given a range of bits in a number, shift those bits to the LSB and sign extend the MSB of the range.
ms.assetid: 1ED39812-A89F-4325-82A0-DA2CCC55A99A
ms.topic: reference
ms.date: 05/31/2018
---

# ibfe (sm5 - asm)

Given a range of bits in a number, shift those bits to the LSB and sign extend the MSB of the range.



| ibfe dest\[.mask\], src0\[.swizzle\], src1\[.swizzle\], src2\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                            | Description                                                    |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The bitfield width.<br/>                          |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The bitfield offset.<br/>                         |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The value to shift.<br/>                          |



 

## Remarks

The LSB 5 bits of src0 provide the bitfield width (0-31).

The LSB 5 bits of src1 provide the bitfield offset (0-31).

The following example shows how to use this instruction.

``` syntax
        Given width, offset:
                if( width == 0 )
                {
                    dest = 0
                }
                else if( width + offset < 32 )
                {
                    shl dest, src2, 32-(width+offset)
                    ishr dest, dest, 32-width
                }
                else
                {
                    ishr dest, src2, offset
                }
```

Use this instruction to unpack signed integers or flags.

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

 

 





