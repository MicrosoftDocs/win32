---
title: ps_2_0
description: Learn about ps_2_0, a programmable pixel shader, which is made up of a set of instructions that operate on pixel data.
ms.assetid: 15f2e4a4-9c39-434b-bea7-5d2d31cae1d9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_2\_0

A programmable pixel shader is made up of a set of instructions that operate on pixel data. Registers transfer data in and out of the ALU. Additional control can be applied to modify the instruction, the results, or what data gets written out.

-   [ps\_2\_0 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-2-0.md) contains a list of the available instructions.
-   [ps\_2\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-2-0.md) lists the different types of registers used by the vertex shader ALU.
-   [Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers.md) Are used to modify the way an instruction works.
-   [Destination Register Write Mask](dx9-graphics-reference-asm-ps-registers-modifiers-write-mask.md) determines what components of the destination register get written.
-   [Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md) alter the source register data before the instruction runs.
-   [Source Register Swizzling](dx9-graphics-reference-asm-ps-registers-modifiers-source-register-swizzling.md) gives additional control over which register components are read, copied, or written.

## Instruction Count

Shaders have restrictions for maximum instruction counts. Total Instruction slots: 96 (64 arithmetic and 32 texture).

## Sampler Count

The number of texture samplers available is 16.

## Related topics

<dl> <dt>

[Pixel Shaders](dx9-graphics-reference-asm-ps.md)
</dt> </dl>

 

 




