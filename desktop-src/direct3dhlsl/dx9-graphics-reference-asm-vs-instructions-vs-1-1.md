---
title: Instructions - vs_1_1
description: This section contains reference information for the vertex shader version 1\_1 instructions.
ms.assetid: db3c14ce-6e50-4931-b07f-966acc7ffb0a
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Instructions - vs\_1\_1

This section contains reference information for the vertex shader version 1\_1 instructions.

There are several types of vertex shader instructions, as shown in the table. Columns to the right mean the following:

-   Instruction slots - Number of instruction slots used by each instruction.
-   Setup - Non-arithmetic instructions. Every shader must have a version instruction and it must be the first instruction.
-   Arithmetic - These instructions provide the mathematical operations in a shader.
-   New - These instructions are new to this version.

## Instruction Set



| Name                                                                           | Description                                                                                                     | Instruction slots | Setup | Arithmetic | New |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------|-------|------------|-----|
| [add - vs](add---vs.md)                                                       | Add two vectors                                                                                                 | 1                 |       | x          | x   |
| [dcl\_usage input (sm1, sm2, sm3 - vs asm)](dcl-usage-input-register---vs.md) | Declare input vertex registers (see [Registers - vs\_1\_1](dx9-graphics-reference-asm-vs-registers-vs-1-1.md)) | 0                 | x     |            | x   |
| [def - vs](def---vs.md)                                                       | Define constants                                                                                                | 0                 | x     |            | x   |
| [dp3 - vs](dp3---vs.md)                                                       | Three-component dot product                                                                                     | 1                 |       | x          | x   |
| [dp4 - vs](dp4---vs.md)                                                       | Four-component dot product                                                                                      | 1                 |       | x          | x   |
| [dst - vs](dst---vs.md)                                                       | Calculate the distance vector                                                                                   | 1                 |       | x          | x   |
| [exp - vs](exp---vs.md)                                                       | Full precision 2<sup>x</sup>                                                                                    | 10                |       | x          | x   |
| [expp - vs](expp---vs.md)                                                       | Partial precision 2<sup>x</sup>                                                                                 | 1                 |       | x          | x   |
| [frc - vs](frc---vs.md)                                                       | Fractional component                                                                                            | 3                 |       | x          | x   |
| [lit - vs](lit---vs.md)                                                       | Partial lighting calculation                                                                                    | 1                 |       | x          | x   |
| [log - vs](log---vs.md)                                                       | Full precision log₂(x)                                                                                          | 10                |       | x          | x   |
| [logp - vs](logp---vs.md)                                                     | Partial precision log₂(x)                                                                                       | 1                 |       | x          | x   |
| [m3x2 - vs](m3x2---vs.md)                                                     | 3x2 multiply                                                                                                    | 2                 |       | x          | x   |
| [m3x3 - vs](m3x3---vs.md)                                                     | 3x3 multiply                                                                                                    | 3                 |       | x          | x   |
| [m3x4 - vs](m3x4---vs.md)                                                     | 3x4 multiply                                                                                                    | 4                 |       | x          | x   |
| [m4x3 - vs](m4x3---vs.md)                                                     | 4x3 multiply                                                                                                    | 3                 |       | x          | x   |
| [m4x4 - vs](m4x4---vs.md)                                                     | 4x4 multiply                                                                                                    | 4                 |       | x          | x   |
| [mad - vs](mad---vs.md)                                                       | Multiply and add                                                                                                | 1                 |       | x          | x   |
| [max - vs](max---vs.md)                                                       | Maximum                                                                                                         | 1                 |       | x          | x   |
| [min - vs](min---vs.md)                                                       | Minimum                                                                                                         | 1                 |       | x          | x   |
| [mov - vs](mov---vs.md)                                                       | Move                                                                                                            | 1                 |       | x          | x   |
| [mul - vs](mul---vs.md)                                                       | Multiply                                                                                                        | 1                 |       | x          | x   |
| [nop - vs](nop---vs.md)                                                       | No operation                                                                                                    | 1                 |       | x          | x   |
| [rcp - vs](rcp---vs.md)                                                       | Reciprocal                                                                                                      | 1                 |       | x          | x   |
| [rsq - vs](rsq---vs.md)                                                       | Reciprocal square root                                                                                          | 1                 |       | x          | x   |
| [sge - vs](sge---vs.md)                                                       | Greater than or equal compare                                                                                   | 1                 |       | x          | x   |
| [slt - vs](slt---vs.md)                                                       | Less than compare                                                                                               | 1                 |       | x          | x   |
| [sub - vs](sub---vs.md)                                                       | Subtract                                                                                                        | 1                 |       | x          | x   |
| [vs](vs---vs.md)                                                              | Version                                                                                                         | 0                 | x     |            | x   |



 

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




