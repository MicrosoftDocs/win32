---
title: Instructions - vs_2_x
description: This section contains reference information for the vertex shader version 2\_x instructions.
ms.assetid: fac85f96-0f4b-49a8-9c00-9e68000d1c76
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Instructions - vs\_2\_x

This section contains reference information for the vertex shader version 2\_x instructions.

There are several types of vertex shader instructions, as shown in the table. Columns to the right mean the following:

-   Instruction slots - Number of instruction slots used by each instruction.
-   Setup - Non-arithmetic instructions. Every shader must have a version instruction and it must be the first instruction.
-   Arithmetic - These instructions provide the mathematical operations in a shader.
-   Flow control - These instructions add flow control capabilities such as [loop - vs](loop---vs.md)...[endloop - vs](endloop---vs.md), [if bool - vs](if-bool---vs.md)...[else](else---vs.md)...[endif](endif---vs.md), and subroutine calls.
-   New - These instructions are new to this version.

## Instruction Set



| Name                                                                           | Description                                                                                                                                                            | Instruction slots | Setup | Arithmetic | Flow control | New |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------|------------|--------------|-----|
| [abs - vs](abs---vs.md)                                                       | Absolute value                                                                                                                                                         | 1                 |       | x          |              |     |
| [add - vs](add---vs.md)                                                       | Add two vectors                                                                                                                                                        | 1                 |       | x          |              |     |
| [break - vs](break---vs.md)                                                   | Break out of a [loop - vs](loop---vs.md)...[endloop - vs](endloop---vs.md) or [rep](rep---vs.md)...[endrep](endrep---vs.md) block                                  | 1                 |       |            | x            | x   |
| [break\_comp - vs](break-comp---vs.md)                                        | Conditionally break out of a [loop - vs](loop---vs.md)...[endloop - vs](endloop---vs.md) or [rep](rep---vs.md)...[endrep](endrep---vs.md) block, with a comparison | 3                 |       |            | x            | x   |
| [breakp - vs](breakp---vs.md)                                                 | Break out of a [loop - vs](loop---vs.md)...[endloop - vs](endloop---vs.md) or [rep](rep---vs.md)...[endrep](endrep---vs.md) block, based on a predicate            | 3                 |       |            | x            | x   |
| [call - vs](call---vs.md)                                                     | Call a subroutine                                                                                                                                                      | 2                 |       |            | x            |     |
| [callnz bool - vs](callnz-bool---vs.md)                                       | Call a subroutine if a Boolean register is not zero                                                                                                                    | 3                 |       |            | x            |     |
| [callnz pred - vs](callnz-pred---vs.md)                                       | Call a subroutine if a predicate register is not zero                                                                                                                  | 3                 |       |            | x            | x   |
| [crs - vs](crs---vs.md)                                                       | Cross product                                                                                                                                                          | 2                 |       | x          |              |     |
| [dcl\_usage input (sm1, sm2, sm3 - vs asm)](dcl-usage-input-register---vs.md) | Declare input vertex registers (see [Registers - vs\_2\_x](dx9-graphics-reference-asm-vs-registers-vs-2-x.md))                                                        | 0                 | x     |            |              |     |
| [def - vs](def---vs.md)                                                       | Define constants                                                                                                                                                       | 0                 | x     |            |              |     |
| [defb - vs](defb---vs.md)                                                     | Define a Boolean constant                                                                                                                                              | 0                 | x     |            |              |     |
| [defi - vs](defi---vs.md)                                                     | Define an integer constant                                                                                                                                             | 0                 | x     |            |              |     |
| [dp3 - vs](dp3---vs.md)                                                       | Three-component dot product                                                                                                                                            | 1                 |       | x          |              |     |
| [dp4 - vs](dp4---vs.md)                                                       | Four-component dot product                                                                                                                                             | 1                 |       | x          |              |     |
| [dst - vs](dst---vs.md)                                                       | Calculate the distance vector                                                                                                                                          | 1                 |       | x          |              |     |
| [else - vs](else---vs.md)                                                     | Begin an [else - vs](else---vs.md) block                                                                                                                              | 1                 |       |            | x            |     |
| [endif - vs](endif---vs.md)                                                   | End an [if bool - vs](if-bool---vs.md)...[else - vs](else---vs.md) block                                                                                             | 1                 |       |            | x            |     |
| [endloop - vs](endloop---vs.md)                                               | End of a [loop - vs](loop---vs.md) block                                                                                                                              | 2                 |       |            | x            |     |
| [endrep - vs](endrep---vs.md)                                                 | End of a repeat block                                                                                                                                                  | 2                 |       |            | x            |     |
| [exp - vs](exp---vs.md)                                                       | Full precision 2<sup>x</sup>                                                                                                                                           | 1                 |       | x          |              |     |
| [expp - vs](expp---vs.md)                                                       | Partial precision 2<sup>x</sup>                                                                                                                                        | 1                 |       | x          |              |     |
| [frc - vs](frc---vs.md)                                                       | Fractional component                                                                                                                                                   | 1                 |       | x          |              |     |
| [if bool - vs](if-bool---vs.md)                                               | Begin an [if bool - vs](if-bool---vs.md) block (using a Boolean condition)                                                                                            | 3                 |       |            | x            |     |
| [if\_comp - vs](if-comp---vs.md)                                              | Begin an [if bool - vs](if-bool---vs.md) block, with a comparison                                                                                                     | 3                 |       |            | x            | x   |
| [if pred - vs](if-pred---vs.md)                                               | Begin an [if bool - vs](if-bool---vs.md) block with a predicate condition                                                                                             | 3                 |       |            | x            | x   |
| [label - vs](label---vs.md)                                                   | Label                                                                                                                                                                  | 0                 |       |            | x            |     |
| [lit - vs](lit---vs.md)                                                       | Partial lighting calculation                                                                                                                                           | 3                 |       | x          |              |     |
| [log - vs](log---vs.md)                                                       | Full precision log₂(x)                                                                                                                                                 | 1                 |       | x          |              |     |
| [logp - vs](logp---vs.md)                                                     | Partial precision log₂(x)                                                                                                                                              | 1                 |       | x          |              |     |
| [loop - vs](loop---vs.md)                                                     | Loop                                                                                                                                                                   | 3                 |       |            | x            |     |
| [lrp - vs](lrp---vs.md)                                                       | Linear interpolation                                                                                                                                                   | 2                 |       | x          |              |     |
| [m3x2 - vs](m3x2---vs.md)                                                     | 3x2 multiply                                                                                                                                                           | 2                 |       | x          |              |     |
| [m3x3 - vs](m3x3---vs.md)                                                     | 3x3 multiply                                                                                                                                                           | 3                 |       | x          |              |     |
| [m3x4 - vs](m3x4---vs.md)                                                     | 3x4 multiply                                                                                                                                                           | 4                 |       | x          |              |     |
| [m4x3 - vs](m4x3---vs.md)                                                     | 4x3 multiply                                                                                                                                                           | 3                 |       | x          |              |     |
| [m4x4 - vs](m4x4---vs.md)                                                     | 4x4 multiply                                                                                                                                                           | 4                 |       | x          |              |     |
| [mad - vs](mad---vs.md)                                                       | Multiply and add                                                                                                                                                       | 1                 |       | x          |              |     |
| [max - vs](max---vs.md)                                                       | Maximum                                                                                                                                                                | 1                 |       | x          |              |     |
| [min - vs](min---vs.md)                                                       | Minimum                                                                                                                                                                | 1                 |       | x          |              |     |
| [mov - vs](mov---vs.md)                                                       | Move                                                                                                                                                                   | 1                 |       | x          |              |     |
| [mova - vs](mova---vs.md)                                                     | Move data from a floating-point register to the address register (a0)                                                                                                  | 1                 |       | x          |              |     |
| [mul - vs](mul---vs.md)                                                       | Multiply                                                                                                                                                               | 1                 |       | x          |              |     |
| [nop - vs](nop---vs.md)                                                       | No operation                                                                                                                                                           | 1                 |       | x          |              |     |
| [nrm - vs](nrm---vs.md)                                                       | Normalize a 4D vector                                                                                                                                                  | 3                 |       | x          |              |     |
| [pow - vs](pow---vs.md)                                                       | x<sup>y</sup>                                                                                                                                                          | 3                 |       | x          |              |     |
| [rcp - vs](rcp---vs.md)                                                       | Reciprocal                                                                                                                                                             | 1                 |       | x          |              |     |
| [rep - vs](rep---vs.md)                                                       | Repeat                                                                                                                                                                 | 3                 |       |            | x            |     |
| [ret - vs](ret---vs.md)                                                       | End of either a subroutine or main                                                                                                                                     | 1                 |       |            | x            |     |
| [rsq - vs](rsq---vs.md)                                                       | Reciprocal square root                                                                                                                                                 | 1                 |       | x          |              |     |
| [setp\_comp - vs](setp-comp---vs.md)                                          | Set the predicate register                                                                                                                                             | 1                 |       |            | x            | x   |
| [sge - vs](sge---vs.md)                                                       | Greater than or equal compare                                                                                                                                          | 1                 |       | x          |              |     |
| [sgn - vs](sgn---vs.md)                                                       | Sign                                                                                                                                                                   | 3                 |       | x          |              |     |
| [sincos - vs](sincos---vs.md)                                                 | Sine and cosine                                                                                                                                                        | 8                 |       | x          |              |     |
| [slt - vs](slt---vs.md)                                                       | Less than compare                                                                                                                                                      | 1                 |       | x          |              |     |
| [sub - vs](sub---vs.md)                                                       | Subtract                                                                                                                                                               | 1                 |       | x          |              |     |
| [vs](vs---vs.md)                                                              | Version                                                                                                                                                                | 0                 | x     |            |              |     |



 

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




