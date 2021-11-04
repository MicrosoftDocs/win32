---
title: ps_1_1, ps_1_2, ps_1_3, ps_1_4 Instructions
description: This section contains reference information for pixel shader version 1\_X instructions.
ms.assetid: cb496887-6755-4f29-b465-a36548b88722
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4 Instructions

This section contains reference information for the pixel shader version 1\_X instructions.

There are several types of pixel shader instructions, as shown in the following table.

## Instruction Set



| Version                                    | Description                                                                   | Instruction slots | 1\_1 | 1\_2 | 1\_3 | 1\_4 |
|--------------------------------------------|-------------------------------------------------------------------------------|-------------------|------|------|------|------|
| [ps](ps---ps.md)                          | Version number                                                                | 0                 | x    | x    | x    | x    |
| Constant instructions                      |                                                                               |                   | 1\_1 | 1\_2 | 1\_3 | 1\_4 |
| [def - ps](def---ps.md)                   | Define constants                                                              | 0                 | x    | x    | x    | x    |
| Phase instructions                         |                                                                               |                   | 1\_1 | 1\_2 | 1\_3 | 1\_4 |
| [phase - ps](phase---ps.md)               | Transition between phase 1 and phase 2                                        | 0                 |      |      |      | x    |
| Arithmetic instructions                    |                                                                               |                   | 1\_1 | 1\_2 | 1\_3 | 1\_4 |
| [add - ps](add---ps.md)                   | Add two vectors                                                               | 1                 | x    | x    | x    | x    |
| [bem - ps](bem---ps.md)                   | Apply a fake bump environment-map transform                                   | 2                 |      |      |      | x    |
| [cmp - ps](cmp---ps.md)                   | Compare source to 0                                                           | 1¹                |      | x    | x    | x    |
| [cnd - ps](cnd---ps.md)                   | Compare source to 0.5                                                         | 1                 | x    | x    | x    | x    |
| [dp3 - ps](dp3---ps.md)                   | Three-component dot product                                                   | 1                 | x    | x    | x    | x    |
| [dp4 - ps](dp4---ps.md)                   | Four-component dot product                                                    | 1¹                |      | x    | x    | x    |
| [lrp - ps](lrp---ps.md)                   | Linear interpolate                                                            | 1                 | x    | x    | x    | x    |
| [mad - ps](mad---ps.md)                   | Multiply and add                                                              | 1                 | x    | x    | x    | x    |
| [mov - ps](mov---ps.md)                   | Move                                                                          | 1                 | x    | x    | x    | x    |
| [mul - ps](mul---ps.md)                   | Multiply                                                                      | 1                 | x    | x    | x    | x    |
| [nop - ps](nop---ps.md)                   | No operation                                                                  | 0                 | x    | x    | x    | x    |
| [sub - ps](sub---ps.md)                   | Subtract                                                                      | 1                 | x    | x    | x    | x    |
| Texture instructions                       |                                                                               |                   | 1\_1 | 1\_2 | 1\_3 | 1\_4 |
| [tex - ps](tex---ps.md)                   | Sample a texture                                                              | 1                 | x    | x    | x    |      |
| [texbem - ps](texbem---ps.md)             | Apply a fake bump environment-map transform                                   | 1                 | x    | x    | x    |      |
| [texbeml - ps](texbeml---ps.md)           | Apply a fake bump environment-map transform with luminance correction         | 1+1²              | x    | x    | x    |      |
| [texcoord - ps](texcoord---ps.md)         | Interpret texture coordinate data as color data                               | 1                 | x    | x    | x    |      |
| [texcrd - ps](texcrd---ps.md)             | Copy texture coordinate data as color data                                    | 1                 |      |      |      | x    |
| [texdepth - ps](texdepth---ps.md)         | Calculate depth values                                                        | 1                 |      |      |      | x    |
| [texdp3 - ps](texdp3---ps.md)             | Three-component dot product between texture data and the texture coordinates  | 1                 |      | x    | x    |      |
| [texdp3tex - ps](texdp3tex---ps.md)       | Three-component dot product and 1D texture lookup                             | 1                 |      | x    | x    |      |
| [texkill - ps](texkill---ps.md)           | Cancels rendering of pixels based on a comparison                             | 1                 | x    | x    | x    | x    |
| [texld - ps\_1\_4](texld---ps-1-4.md)     | Sample a texture                                                              | 1                 |      |      |      | x    |
| [texm3x2depth - ps](texm3x2depth---ps.md) | Calculate per-pixel depth values                                              | 1                 |      |      | x    |      |
| [texm3x2pad - ps](texm3x2pad---ps.md)     | First row matrix multiply of a two-row matrix multiply                        | 1                 | x    | x    | x    |      |
| [texm3x2tex - ps](texm3x2tex---ps.md)     | Final row matrix multiply of a two-row matrix multiply                        | 1                 | x    | x    | x    |      |
| [texm3x3 - ps](texm3x3---ps.md)           | 3x3 matrix multiply                                                           | 1                 |      | x    | x    |      |
| [texm3x3pad - ps](texm3x3pad---ps.md)     | First or second row multiply of a three-row matrix multiply                   | 1                 | x    | x    | x    |      |
| [texm3x3spec - ps](texm3x3spec---ps.md)   | Final row multiply of a three-row matrix multiply                             | 1                 | x    | x    | x    |      |
| [texm3x3tex - ps](texm3x3tex---ps.md)     | Texture look up using a 3x3 matrix multiply                                   | 1                 | x    | x    | x    |      |
| [texm3x3vspec - ps](texm3x3vspec---ps.md) | Texture look up using a 3x3 matrix multiply, with non-constant eye-ray vector | 1                 | x    | x    | x    |      |
| [texreg2ar - ps](texreg2ar---ps.md)       | Sample a texture using the alpha and red components                           | 1                 | x    | x    | x    |      |
| [texreg2gb - ps](texreg2gb---ps.md)       | Sample a texture using the green and blue components                          | 1                 | x    | x    | x    |      |
| [texreg2rgb - ps](texreg2rgb---ps.md)     | Sample a texture using the red, green and blue components                     | 1                 |      | x    | x    |      |



 

1.  1 slot in ps\_1\_4; 2 slots in ps\_1\_2 and ps\_1\_3
2.  1 + 1 = 1 arithmetic instruction + 1 texture instruction

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




