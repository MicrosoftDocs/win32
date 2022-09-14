---
title: vs_2_0
description: Learn about vs_2_0, a programmable vertex shader, which is made up of a set of instructions that operate on vertex data.
ms.assetid: 6e38c138-5f9c-40a6-9fe2-a93471c3c573
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# vs\_2\_0

A programmable vertex shader is made up of a set of instructions that operate on vertex data. Registers transfer data in and out of the ALU. Additional control can be applied to modify the instruction, the results, or what data gets written out.

-   [Instructions - vs\_2\_0](dx9-graphics-reference-asm-vs-instructions-vs-2-0.md) contains a list of the available instructions.
-   [Registers - vs\_2\_0](dx9-graphics-reference-asm-vs-registers-vs-2-0.md) lists the different types of registers used by the vertex shader ALU.
-   [Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md) are used to modify the way an instruction works.
-   [Vertex Shader Source Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers-source.md) alter the source register data before the instruction runs.
-   [Source Register Swizzling](dx9-graphics-reference-asm-vs-registers-modifiers-source-swizzling.md) gives additional control over which register components are read, copied, or written.
-   [Destination Register Masking](dx9-graphics-reference-asm-vs-registers-modifiers-masking.md) determines what components of the destination register get written.

## Instruction Count

Each vertex shader can have up to 256 instructions stored. The number of instructions run can be much higher (because of the loop/rep support), and is capped by D3DCAPS9.MaxVShaderInstructionsExecuted, which should be at least 0xFFFF.

## Related topics

<dl> <dt>

[Vertex Shaders](dx9-graphics-reference-asm-vs.md)
</dt> </dl>

 

 




