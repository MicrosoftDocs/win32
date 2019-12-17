---
title: firstbit (sm5 - asm)
description: Finds the first bit set in a number, either from LSB or MSB.
ms.assetid: E3066676-5218-470A-944A-7B221E1BF64D
ms.topic: reference
ms.date: 05/31/2018
---

# firstbit (sm5 - asm)

Finds the first bit set in a number, either from LSB or MSB.



| firstbit{\_hi\|\_lo\|\_shi} dest\[.mask\], src0\[.swizzle\] |
|-------------------------------------------------------------|



 



| Item                                                            | Description                                                                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The integer position of the first bit set in *src0* starting from the LSB for firstbit\_lo or MSB for firstbit\_hi.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The input integer.<br/>                                                                                                  |



 

## Remarks

This operation returns the integer position of the first bit set in the 32-bit input starting from the LSB for firstbit\_lo or MSB for firstbit\_hi. For example firstbit\_lo on 0x00000001 returns 0. firstbit\_hi on 0x10000000 returns 3.

firstbit\_shi (s for signed) returns the first 0 from the MSB if the number is negative; otherwise it returns the first 1 from the MSB.

All variants of the instruction return ~0 (0xffffffff in 32-bit register) if no match is found.

Use this instruction to quickly enumerate set bits in a bitfield, or find the largest power of 2 in a number.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Mimimum Shader Model

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

 

 





