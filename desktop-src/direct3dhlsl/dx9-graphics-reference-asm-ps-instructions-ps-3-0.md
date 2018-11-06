---
title: ps_3_0 Instructions
description: This section contains reference information for the pixel shader version 3\_0 instructions.
ms.assetid: 36972b9b-a4e7-45b4-83f5-959e75d270de
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_3\_0 Instructions

This section contains reference information for the pixel shader version 3\_0 instructions.

There are several types of pixel shader instructions, as shown in the table. Columns to the right mean the following:

-   Instruction slots - Number of instruction slots used by each instruction.
-   Setup - A pixel shader must have a version instruction and it must be the first instruction.
-   Arithmetic - These instructions provide the mathematical operations in a shader.
-   Texture - These instructions are used to load and sample texture data, and to modify texture coordinates.
-   Flow control - These instructions provide static and dynamic flow control to the execution of instructions.
-   New - These instructions are new to this version.

## Instruction Set



| Name                                                             | Description                                                                          | Instruction slots | Setup | Arithmetic | Texture | Flow control | New |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------|-------|------------|---------|--------------|-----|
| [abs - ps](abs---ps.md)                                         | Absolute value                                                                       | 1                 |       | x          |         |              |     |
| [add - ps](add---ps.md)                                         | Add two vectors                                                                      | 1                 |       | x          |         |              |     |
| [break - ps](break---ps.md)                                     | Break out of a loop...endloop or rep...endrep block                                  | 1                 |       |            |         | x            |     |
| [break\_comp - ps](break-comp---ps.md)                          | Conditionally break out of a loop...endloop or rep...endrep block, with a comparison | 3                 |       |            |         | x            |     |
| [breakp - ps](break-p---ps.md)                                  | break out of a loop...endloop or rep...endrep block, based on a predicate            | 3                 |       |            |         | x            |     |
| [call - ps](call---ps.md)                                       | Call a subroutine                                                                    | 2                 |       |            |         | x            |     |
| [callnz bool - ps](callnz-bool---ps.md)                         | Call a subroutine if a boolean register is not zero                                  | 3                 |       |            |         | x            |     |
| [callnz pred - ps](callnz-pred---ps.md)                         | Call a subroutine if a predicate register is not zero                                | 3                 |       |            |         | x            |     |
| [cmp - ps](cmp---ps.md)                                         | Compare source to 0                                                                  | 1                 |       | x          |         |              |     |
| [crs - ps](crs---ps.md)                                         | Cross product                                                                        | 2                 |       | x          |         |              |     |
| [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md) | Declare the texture dimension for a sampler                                          | 0                 | x     |            |         |              |     |
| [dcl\_semantics (sm3 - ps asm)](dcl-usage---ps.md)              | Declare input and output registers                                                   | 0                 | x     |            |         |              | x   |
| [def - ps](def---ps.md)                                         | Define constants                                                                     | 0                 | x     |            |         |              |     |
| [defb - ps](defb---ps.md)                                       | Define a Boolean constant                                                            | 0                 | x     |            |         |              |     |
| [defi - ps](defi---ps.md)                                       | Define an integer constant                                                           | 0                 | x     |            |         |              |     |
| [dp2add - ps](dp2add---ps.md)                                   | 2D dot product and add                                                               | 2                 |       | x          |         |              |     |
| [dp3 - ps](dp3---ps.md)                                         | 3D dot product                                                                       | 1                 |       | x          |         |              |     |
| [dp4 - ps](dp4---ps.md)                                         | 4D dot product                                                                       | 1                 |       | x          |         |              |     |
| [dsx - ps](dsx---ps.md)                                         | Rate of change in the x-direction                                                    | 2                 |       | x          |         |              |     |
| [dsy - ps](dsy---ps.md)                                         | Rate of change in the y direction                                                    | 2                 |       | x          |         |              |     |
| [else - ps](else---ps.md)                                       | Begin an else block                                                                  | 1                 |       |            |         | x            |     |
| [endif - ps](endif---ps.md)                                     | End an if...else block                                                               | 1                 |       |            |         | x            |     |
| [endloop - ps](endloop---ps.md)                                 | End a loop                                                                           | 2                 |       |            |         | x            | x   |
| [endrep - ps](endrep---ps.md)                                   | End of a repeat block                                                                | 2                 |       |            |         | x            |     |
| [exp - ps](exp---ps.md)                                         | Full precision 2<sup>x</sup>                                                         | 1                 |       | x          |         |              |     |
| [frc - ps](frc---ps.md)                                         | Fractional component                                                                 | 1                 |       | x          |         |              |     |
| [if bool - ps](if-bool---ps.md)                                 | Begin an if block                                                                    | 3                 |       |            |         | x            |     |
| [if\_comp - ps](if-comp---ps.md)                                | Begin an if block with a comparison                                                  | 3                 |       |            |         | x            |     |
| [if pred - ps](if-pred---ps.md)                                 | Begin an if block with predication                                                   | 3                 |       |            |         | x            |     |
| [label - ps](label---ps.md)                                     | Label                                                                                | 0                 |       |            |         | x            |     |
| [log - ps](log---ps.md)                                         | Full precision log₂(x)                                                               | 1                 |       | x          |         |              |     |
| [loop - ps](loop---ps.md)                                       | Loop                                                                                 | 3                 |       |            |         | x            | x   |
| [lrp - ps](lrp---ps.md)                                         | Linear interpolate                                                                   | 2                 |       | x          |         |              |     |
| [m3x2 - ps](m3x2---ps.md)                                       | 3x2 multiply                                                                         | 2                 |       | x          |         |              |     |
| [m3x3 - ps](m3x3---ps.md)                                       | 3x3 multiply                                                                         | 3                 |       | x          |         |              |     |
| [m3x4 - ps](m3x4---ps.md)                                       | 3x4 multiply                                                                         | 4                 |       | x          |         |              |     |
| [m4x3 - ps](m4x3---ps.md)                                       | 4x3 multiply                                                                         | 3                 |       | x          |         |              |     |
| [m4x4 - ps](m4x4---ps.md)                                       | 4x4 multiply                                                                         | 4                 |       | x          |         |              |     |
| [mad - ps](mad---ps.md)                                         | Multiply and add                                                                     | 1                 |       | x          |         |              |     |
| [max - ps](max---ps.md)                                         | Maximum                                                                              | 1                 |       | x          |         |              |     |
| [min - ps](min---ps.md)                                         | Minimum                                                                              | 1                 |       | x          |         |              |     |
| [mov - ps](mov---ps.md)                                         | Move                                                                                 | 1                 |       | x          |         |              |     |
| [mul - ps](mul---ps.md)                                         | Multiply                                                                             | 1                 |       | x          |         |              |     |
| [nop - ps](nop---ps.md)                                         | No operation                                                                         | 1                 |       | x          |         |              |     |
| [nrm - ps](nrm---ps.md)                                         | Normalize                                                                            | 3                 |       | x          |         |              |     |
| [pow - ps](pow---ps.md)                                         | x<sup>y</sup>                                                                        | 3                 |       | x          |         |              |     |
| [ps](ps---ps.md)                                                | Version                                                                              | 0                 | x     |            |         |              |     |
| [rcp - ps](rcp---ps.md)                                         | Reciprocal                                                                           | 1                 |       | x          |         |              |     |
| [rep - ps](rep---ps.md)                                         | Repeat                                                                               | 3                 |       |            |         | x            |     |
| [ret - ps](ret---ps.md)                                         | End of a subroutine                                                                  | 1                 |       |            |         | x            |     |
| [rsq - ps](rsq---ps.md)                                         | Reciprocal square root                                                               | 1                 |       | x          |         |              |     |
| [setp\_comp](setp-comp---ps.md)                                 | Set the predicate register                                                           | 1                 |       |            |         | x            |     |
| [sincos - ps](sincos---ps.md)                                   | Sine and cosine                                                                      | 8                 |       | x          |         |              |     |
| [sub - ps](sub---ps.md)                                         | Subtract                                                                             | 1                 |       | x          |         |              |     |
| [texkill - ps](texkill---ps.md)                                 | Kill pixel render                                                                    | 2                 |       |            | x       |              |     |
| [texld - ps\_2\_0 and up](texld---ps-2-0.md)                    | Sample a texture                                                                     | See note 1        |       |            | x       |              |     |
| [texldb - ps](texldb---ps.md)                                   | Texture sampling with level-of-detail bias from w-component                          | 6                 |       |            | x       |              |     |
| [texldl - ps](texldl---ps.md)                                   | Texture sampling with level-of-detail from w-component                               | See note 2        |       |            | x       |              | x   |
| [texldd - ps](texldd---ps.md)                                   | Texture sampling with user-provided gradients                                        | 3                 |       |            | x       |              |     |
| [texldp - ps](texldp---ps.md)                                   | Texture sampling with projective divide by w-component                               | See note 3        |       |            | x       |              |     |



 

Notes:

1.  If the texture is a cube map, slots = 4; otherwise slots = 1.
2.  If the texture is a cube map, slots = 5; otherwise slots = 2.
3.  If the texture is a cube map, slots = 4; otherwise slots = 3.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




