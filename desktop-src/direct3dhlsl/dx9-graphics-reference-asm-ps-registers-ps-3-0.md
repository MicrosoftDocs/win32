---
title: ps_3_0 Registers
description: This article contains reference information for the input and output registers implemented by pixel shader version 3_0.
ms.assetid: 01bee50a-c1b7-4b15-9df8-1dd52d9ff163
keywords:
- vPos
- Position Register, Pixel Shader
- Registers - ps_3_0
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_3\_0 Registers

Pixel shaders depend on registers to get vertex data, to output pixel data, to hold temporary results during calculations, and to identify texture sampling stages. There are several types of registers, each with a unique functionality. This section contains reference information for the input and output registers implemented by pixel shader version 3\_0.

## New Registers

### Input Register

The Input Registers (v\#) are now fully floating point and the [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md)s (t\#) have been consolidated into it. The [dcl\_semantics (sm3 - ps asm)](dcl-usage---ps.md) at the top of the shader is used to describe what is containted in a particular Input\_Register. A semantic for the pixel types is introduced (analogous to the vertex side) for this model. No clamping is performed when the input registers are defined as colors (like texture coordinates). The evaluation of the registers defined as color differs from the texture coordinates when multisampling.

### Face Register

The face register (vFace) is new for this model. This is a floating point scalar register that will eventually contain the primitive area. In ps\_3\_0, however, only the sign of this register is valid. Hence, if the value is less than zero (the sign bit is set negative) the primitive is the back face (the area is negative, counterclockwise). Therefore, in ps\_3\_0 it only makes sense to compare this register against 0 (> 0 or < 0). Inside the pixel shader, the application can make a decision as to which lighting technique to use. Two-sided lighting can be achieved this way. This register requires a declaration, so undeclared usage will be flagged as an error. For lines and point primitives, this register is undefined. The face register can only be used as condition with the following instructions: [setp\_comp - ps](setp-comp---ps.md), [if\_comp - ps](if-comp---ps.md), or [break\_comp - ps](break-comp---ps.md).

### Loop Counter Register

The [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) (aL) is new for this model. It automatically gets incremented in each execution of the [loop - ps](loop---ps.md)/[endloop - ps](endloop---ps.md) block. It can be used in the block for relative addressing if needed. It is invalid to use Loop Counter Register outside the loop.

### Position Register

The Position Register (vPos) is new for this model. It contains the current pixels (x, y) in the corresponding channels. The (z, w) channels are undefined. This register requires a declaration, so undeclared usage will be flagged as an error. When declared, this register must have exactly one of the following masks: .x, .y, .xy.

## Input Register Types



| Register | Name                                                                                      | Count | R/W | \# Read ports | \# Reads/inst | Dimension | RelAddr | Defaults   | Requires DCL |
|----------|-------------------------------------------------------------------------------------------|-------|-----|---------------|---------------|-----------|---------|------------|--------------|
| v\#      | [Input Register](dx9-graphics-reference-asm-ps-registers-input-color.md)                 | 10    | R   | 1             | Unlimited     | 4         | aL      | None       | Yes          |
| r\#      | [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md)               | 32    | R/W | 3             | Unlimited     | 4         | No      | None       | No           |
| c\#      | [Constant Float Register](dx9-graphics-reference-asm-ps-registers-constant-float.md)     | 224   | R   | 1             | Unlimited     | 4         | No      | 0000       | No           |
| i\#      | [Constant Integer Register](dx9-graphics-reference-asm-ps-registers-constant-integer.md) | 16    | R   | 1             | 1             | 4         | No      | 0000       | No           |
| b\#      | [Constant Boolean Register](dx9-graphics-reference-asm-ps-registers-constant-boolean.md) | 16    | R   | 1             | 1             | 1         | No      | FALSE      | No           |
| p0       | [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md)               | 1     | R   | 1             | 1             | 1         | No      | None       | No           |
| s\#      | [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md)        | 16    | R   | 1             | 1             | 4         | No      | See note 1 | Yes          |
| vFace    | Face\_Register                                                                            | 1     | R   | 1             | Unlimited     | 1         | No      | None       | Yes          |
| vPos     | Position\_Register                                                                        | 1     | R   | 1             | Unlimited     | 4         | No      | None       | Yes          |
| aL       | Loop\_Counter\_Register                                                                   | 1     | R   | 1             | Unlimited     | 1         | n/a     | None       | No           |



 

Notes:

-   Defaults for sampler lookups exist, but values depend on texture format.

The number of readports is the number of different registers (for each register type) that can be read in a single instruction.

## Output Register Types



| Register | Name                                                                              | Count                                                                             | R/W | Dimension | RelAddr | Defaults | Requires DCL |
|----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----|-----------|---------|----------|--------------|
| oC#     | [Output Color Register](dx9-graphics-reference-asm-ps-registers-output-color.md) | See [Multiple-element Textures (Direct3D 9)](/windows/desktop/direct3d9/multiple-element-textures) | W   | 4         | No      | None     | No           |
| oDepth   | [Output Depth Register](dx9-graphics-reference-asm-ps-registers-output-depth.md) | 1                                                                                 | W   | 1         | No      | None     | No           |



 

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 