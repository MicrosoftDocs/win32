---
title: ps_2_0 Instructions
description: This section contains reference information for the pixel shader version 2\_0 instructions.
ms.assetid: 70492436-4d0d-48e6-b3d2-8934931fb5c2
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_2\_0 Instructions

This section contains reference information for the pixel shader version 2\_0 instructions.

There are several types of pixel shader instructions, as shown in the table. Columns to the right mean the following:

-   Instruction slots - Number of instruction slots used by each instruction.
-   Setup - A pixel shader must have a version instruction and it must be the first instruction.
-   Arithmetic - These instructions provide the mathematical operations in a shader.
-   Texture - These instructions are used to load and sample texture data, and to modify texture coordinates.
-   New - These instructions are new to this version.

## Instruction Set



| Name                                                             | Description                                                                                      | Instruction slots | Setup | Arithmetic | Texture | New |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------|-------|------------|---------|-----|
| [abs - ps](abs---ps.md)                                         | Absolute value                                                                                   | 1                 |       | x          |         | x   |
| [add - ps](add---ps.md)                                         | Add two vectors                                                                                  | 1                 |       | x          |         |     |
| [cmp - ps](cmp---ps.md)                                         | Compare source to 0                                                                              | 1                 |       | x          |         |     |
| [crs - ps](crs---ps.md)                                         | Cross product                                                                                    | 2                 |       | x          |         | x   |
| [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md) | Declare the texture dimension for a sampler                                                      | 0                 | x     |            |         | x   |
| [dcl - (sm2, sm3 - ps asm)](dcl---ps.md)                        | Declare the association between vertex shader output registers and pixel shader input registers. | 0                 | x     |            |         | x   |
| [def - ps](def---ps.md)                                         | Define constants                                                                                 | 0                 | x     |            |         |     |
| [dp2add - ps](dp2add---ps.md)                                   | 2D dot product and add                                                                           | 2                 |       | x          |         | x   |
| [dp3 - ps](dp3---ps.md)                                         | 3D dot product                                                                                   | 1                 |       | x          |         |     |
| [dp4 - ps](dp4---ps.md)                                         | 4D dot product                                                                                   | 1                 |       | x          |         |     |
| [exp - ps](exp---ps.md)                                         | Full precision 2<sup>x</sup>                                                                     | 1                 |       | x          |         | x   |
| [frc - ps](frc---ps.md)                                         | Fractional component                                                                             | 1                 |       | x          |         | x   |
| [log - ps](log---ps.md)                                         | Full precision log₂(x)                                                                           | 1                 |       | x          |         | x   |
| [lrp - ps](lrp---ps.md)                                         | Linear interpolate                                                                               | 2                 |       | x          |         |     |
| [m3x2 - ps](m3x2---ps.md)                                       | 3x2 multiply                                                                                     | 2                 |       | x          |         | x   |
| [m3x3 - ps](m3x3---ps.md)                                       | 3x3 multiply                                                                                     | 3                 |       | x          |         | x   |
| [m3x4 - ps](m3x4---ps.md)                                       | 3x4 multiply                                                                                     | 4                 |       | x          |         | x   |
| [m4x3 - ps](m4x3---ps.md)                                       | 4x3 multiply                                                                                     | 3                 |       | x          |         | x   |
| [m4x4 - ps](m4x4---ps.md)                                       | 4x4 multiply                                                                                     | 4                 |       | x          |         | x   |
| [mad - ps](mad---ps.md)                                         | Multiply and add                                                                                 | 1                 |       | x          |         |     |
| [max - ps](max---ps.md)                                         | Maximum                                                                                          | 1                 |       | x          |         | x   |
| [min - ps](min---ps.md)                                         | Minimum                                                                                          | 1                 |       | x          |         | x   |
| [mov - ps](mov---ps.md)                                         | Move                                                                                             | 1                 |       | x          |         |     |
| [mul - ps](mul---ps.md)                                         | Multiply                                                                                         | 1                 |       | x          |         |     |
| [nop - ps](nop---ps.md)                                         | No operation                                                                                     | 1                 |       | x          |         |     |
| [nrm - ps](nrm---ps.md)                                         | Normalize                                                                                        | 3                 |       | x          |         | x   |
| [pow - ps](pow---ps.md)                                         | x<sup>y</sup>                                                                                    | 3                 |       | x          |         | x   |
| [ps](ps---ps.md)                                                | Version                                                                                          | 0                 | x     |            |         |     |
| [rcp - ps](rcp---ps.md)                                         | Reciprocal                                                                                       | 1                 |       | x          |         | x   |
| [rsq - ps](rsq---ps.md)                                         | Reciprocal square root                                                                           | 1                 |       | x          |         | x   |
| [sincos - ps](sincos---ps.md)                                   | Sine and cosine                                                                                  | 8                 |       | x          |         | x   |
| [sub - ps](sub---ps.md)                                         | Subtract                                                                                         | 1                 |       | x          |         |     |
| [texkill - ps](texkill---ps.md)                                 | Kill pixel render                                                                                | 1                 |       |            | x       |     |
| [texld - ps\_2\_0 and up](texld---ps-2-0.md)                    | Sample a texture                                                                                 | 1                 |       |            | x       | x   |
| [texldb - ps](texldb---ps.md)                                   | Texture sampling with level-of-detail bias from w-component                                      | 1                 |       |            | x       | x   |
| [texldp - ps](texldp---ps.md)                                   | Texture sampling with projective divide by w-component                                           | 1                 |       |            | x       | x   |



 

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




