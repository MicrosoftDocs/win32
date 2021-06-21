---
title: vs_2_x
description: Learn about vs_2_x, a programmable vertex shader, which is made up of a set of instructions that operate on vertex data.
ms.assetid: 64b07597-1e16-4803-b991-e78eabc2c060
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# vs\_2\_x

A programmable vertex shader is made up of a set of instructions that operate on vertex data. Registers transfer data in and out of the ALU. Additional control can be applied to modify the instruction, the results, or what data gets written out.

Vertex shader version vs\_2\_x extends the feature set supported by vs\_2\_0. Each additional feature is represented by a corresponding cap in the [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9) structure within [D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps). To use any of the enhanced features represented by these caps, the vertex shader version must be specified as vs\_2\_x.

-   [Instructions - vs\_2\_x](dx9-graphics-reference-asm-vs-instructions-vs-2-x.md) contains a list of the available instructions.
-   [Registers - vs\_2\_x](dx9-graphics-reference-asm-vs-registers-vs-2-x.md) lists the different types of registers used by the vertex shader ALU.
-   [Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md) are used to modify the way an instruction works.
-   [Vertex Shader Source Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers-source.md) alter the source register data before the instruction runs.
-   [Source Register Swizzling](dx9-graphics-reference-asm-vs-registers-modifiers-source-swizzling.md) gives additional control over which register components are read, copied, or written.
-   [Destination Register Masking](dx9-graphics-reference-asm-vs-registers-modifiers-masking.md) determines what components of the destination register get written.

## New Features

New features are as follows:

### Dynamic Flow Control

If [D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps) > 0, then the following dynamic flow control instructions are supported:

-   [if\_comp - vs](if-comp---vs.md)
-   [break - vs](break---vs.md)
-   [break\_comp - vs](break-comp---vs.md)

If [D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps) is also set, the following additional flow control instructions are supported:

-   [setp\_comp - vs](setp-comp---vs.md)
-   [if pred - vs](if-pred---vs.md)
-   [callnz pred - vs](callnz-pred---vs.md)
-   [breakp - vs](breakp---vs.md)

The range of values for dynamic flow control depth is 0 to 24 and is equal to the nesting depth of the dynamic flow control instructions (see [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md) for details). If this cap is zero, the device does not support dynamic flow control instructions.

### Number of Temporary Registers

[D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps) represents the number of [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)s supported by the device. The range of values for this cap is 12 to 32.

### Static Flow Control Nesting Depth

[D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps) represents the nesting depth of two types of static flow control instructions: [loop - vs](loop---vs.md)/[rep - vs](rep---vs.md) and [call - vs](call---vs.md)/[callnz bool - vs](callnz-bool---vs.md)/[if bool - vs](if-bool---vs.md). loop - vs/rep - vs instructions can be nested up to D3DVS20CAPS deep. Independently, call - vs/callnz bool - vs instructions can be nested up to D3DVS20CAPS deep. If D3DVS20CAPS is also set, then [callnz pred - vs](callnz-pred---vs.md) is counted toward the nesting depth of call - vs/callnz bool - vs/if bool - vs (see [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md) for details).

### Predication

If [D3DVS20CAPS](/windows/desktop/direct3d9/d3dvs20caps) is set, the device supports [setp\_comp - vs](setp-comp---vs.md) and instruction predication. If D3DVS20CAPS is also greater than 0, then the following additional dynamic flow control instructions are supported:

-   [if pred - vs](if-pred---vs.md)
-   [callnz pred - vs](callnz-pred---vs.md)
-   [breakp - vs](breakp---vs.md)

### Instruction Count

Each vertex shader can have up to 256 instructions stored. The number of instructions run can be much higher (because of the loop/rep support), and is capped by [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9), which should be at least 0xFFFF.

## Related topics

<dl> <dt>

[Vertex Shaders](dx9-graphics-reference-asm-vs.md)
</dt> </dl>

 

 