---
title: Vertex Shader Differences
description: Vertex Shader Differences
ms.assetid: 94fe4033-94c0-4561-b0fd-1fb85d8f796b
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Vertex Shader Differences

## Instruction Slots

Each version supports a differing number of maximum instruction slots.



| Version  | Maximum number of instruction slots                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| vs\_1\_1 | 128                                                                                                                               |
| vs\_2\_0 | 256                                                                                                                               |
| vs\_2\_x | 256                                                                                                                               |
| vs\_3\_0 | 512 minimum, and up to the number of slots in D3DCAPS9.MaxVertexShader30InstructionSlots. See [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9). |



 

For information about the limitations of software shaders, see [Software Shaders](dx9-graphics-reference-asm-software-shaders.md).

## Flow Control Nesting Limits

-   See [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md).

## vs\_1\_1 Features

New instructions:

See [Instructions - vs\_1\_1](dx9-graphics-reference-asm-vs-instructions-vs-1-1.md).

New registers:

See [Registers - vs\_1\_1](dx9-graphics-reference-asm-vs-registers-vs-1-1.md).

## vs\_2\_0 Features

New features:

-   Static flow control
-   All four components of the [Address Register](dx9-graphics-reference-asm-vs-registers-address.md) (a0) are available.

New instructions:

-   Setup instructions - [defb - vs](defb---vs.md), [defi - vs](defi---vs.md)
-   Arithmetic instructions - [abs - vs](abs---vs.md), [crs - vs](crs---vs.md), [lrp - vs](lrp---vs.md), [mova - vs](mova---vs.md), [nrm - vs](nrm---vs.md), [pow - vs](pow---vs.md), [sgn - vs](sgn---vs.md), [sincos - vs](sincos---vs.md)
-   Static flow control instructions - [call - vs](call---vs.md), [callnz bool - vs](callnz-bool---vs.md), [else - vs](else---vs.md), [endif - vs](endif---vs.md), [endloop - vs](endloop---vs.md), [endrep - vs](endrep---vs.md), [if bool - vs](if-bool---vs.md), [label - vs](label---vs.md), [loop - vs](loop---vs.md), [rep - vs](rep---vs.md), [ret - vs](ret---vs.md)

New registers:

-   [Constant Boolean Register](dx9-graphics-reference-asm-vs-registers-constant-boolean.md) (b\#)
-   [Constant Integer Register](dx9-graphics-reference-asm-vs-registers-constant-integer.md) (i\#)
-   [Loop Counter Register](dx9-graphics-reference-asm-vs-registers-loop-counter.md) (aL)

## vs\_2\_x Features

New features (D3DCAPS9.VS20Caps):

-   Dynamic flow control
-   Nesting for dynamic and static flow control instructions
-   Number of [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)s (r\#) increased
-   Predication

New Instructions:

-   Dynamic flow control instructions - [break - vs](break---vs.md), [break\_comp - vs](break-comp---vs.md), [breakp - vs](breakp---vs.md), [callnz pred - vs](callnz-pred---vs.md), [if\_comp - vs](if-comp---vs.md), [if pred - vs](if-pred---vs.md), [setp\_comp - vs](setp-comp---vs.md)

New registers:

-   [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md) (p0)

## vs\_3\_0 Features

New features :

-   Texture lookup
-   Indexable [Output Registers](dx9-graphics-reference-asm-vs-registers-vs-3-0.md) (o\#)
-   Number of [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)s (r\#) increased to 32

New instructions:

-   Setup instruction - [dcl\_samplerType (sm3 - vs asm)](dcl-samplertype---vs.md)
-   Texture instruction - [texldl - vs](texldl---vs.md)

New registers:

-   [Sampler (Direct3D 9 asm-vs)](dx9-graphics-reference-asm-vs-registers-sampler.md) (s\#)

## Related topics

<dl> <dt>

[Vertex Shaders](dx9-graphics-reference-asm-vs.md)
</dt> </dl>

 

 