---
title: ps_1_1, ps_1_2, ps_1_3, ps_1_4
description: The pixel shader assembler is made up of a set of instructions that operate on pixel data contained in registers.
ms.assetid: 51b59f98-2fa8-4280-bc36-f4328a646168
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4

The pixel shader assembler is made up of a set of instructions that operate on pixel data contained in registers. Operations are expressed as instructions comprised of an operator and one or more operands. Instructions use registers to transfer data in and out of the pixel shader ALU. Registers can also be used by some instructions to hold temporary results.

> [!Note]  
> HLSL support for pixel shader 1.x is deprecated.

 

## Instructions

There are two main categories of pixel shader instructions: arithmetic instructions and texture addressing instructions. Arithmetic instructions modify color data. Texture addressing operations process texture coordinate data and in most cases, sample a texture. Pixel shader instructions are run on a per-pixel basis; that is, they have no knowledge of other pixels in the pipeline.

Texture addressing instructions each consume one slot, but arithmetic instructions can be paired to enable both color components (RGB) and an alpha component instruction in a single slot.

[ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-1-x.md) contains a list of the available instructions.

When multisampling is enabled, pixel shaders only get run once per pixel, not once for every subpixel. Multisampling only increases the resolution of polygon edges, as well as depth and stencil tests. For example, if 3x3 multisampling is enabled, and a triangle being rasterized is found to cover five of the nine subpixels for a particular pixel, the pixel shader gets run once and the same color result is applied to all five subpixels.

## Registers

[ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md) lists the different registers used by the shader ALU.

## Modifiers

[Modifiers for ps\_1\_X](dx9-graphics-reference-asm-ps-instructions-modifiers-ps-1-x.md) can be used to change the functionality of an instruction, or the data read from or written to a register.

Direct3D 9 requires intermediate computations to maintain at least 8-bit precision for all surface formats. Both higher precision (12-bit) for in-stage math, and saturation to 8-bits between texture stages are recommended. No modifiable rounding modes or exceptions are supported. Multiplication should be supported with a round-to-nearest precision to keep precision loss to a minimum.

## Sampler Count

The number of texture samplers available is:

-   For ps\_1\_0 - ps\_1\_3, the maximum is 4.
-   For ps\_1\_4, the maximum is 6.

## Related topics

<dl> <dt>

[Pixel Shaders](dx9-graphics-reference-asm-ps.md)
</dt> </dl>

 

 




