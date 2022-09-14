---
title: ps_2_0 Registers
description: This article contains reference information for the input and output registers implemented by pixel shader version 2_0.
ms.assetid: 8002e3eb-b9d4-4ecb-a9e5-ae58a9e20ace
keywords:
- Registers - ps_2_0
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_2\_0 Registers

Pixel shaders depend on registers to get vertex data, to output pixel data, to hold temporary results during calculations, and to identify texture sampling stages. There are several types of registers, each with a unique functionality. This section contains reference information for the input and output registers implemented by pixel shader version 2\_x.

## Input Register Types



| Register | Name                                                                                          | Count      | R/W        | \# Read ports | \# Reads/inst | Dimension | RelAddr | Defaults                  | Requires DCL |
|----------|-----------------------------------------------------------------------------------------------|------------|------------|---------------|---------------|-----------|---------|---------------------------|--------------|
| v\#      | [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md)               | 2          | R          | 1             | Unlimited     | 4         | N       | Partial(0001). See note 4 | Y            |
| r\#      | [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md)                   | See note 1 | R/W        | 3             | Unlimited     | 4         | N       | None                      | N            |
| c\#      | [Constant Float Register](dx9-graphics-reference-asm-ps-registers-constant-float.md)         | 32         | R          | 1             | 2             | 4         | N       | 0000                      | N            |
| i\#      | [Constant Integer Register](dx9-graphics-reference-asm-ps-registers-constant-integer.md)     | 16         | See note 2 | 1             | 1             | 4         | N       | 0000                      | N            |
| b\#      | [Constant Boolean Register](dx9-graphics-reference-asm-ps-registers-constant-boolean.md)     | 16         | See note 2 | 1             | 1             | 1         | N       | FALSE                     | N            |
| p0       | [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md)                   | 1          | See note 2 | 1             | 1             | 1         | N       | None                      | Y            |
| s\#      | [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md)            | 16         | See note 3 | 1             | 1             | 4         | N       | See note 5                | Y            |
| t\#      | [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md) | 8          | R          | 1             | 1             | 4         | N       | None                      | Y            |



 

Notes:

1.  12 min/32 max: The number of r\# registers is determined by D3DPSHADERCAPS2\_0.NumTemps (which ranges from 12 to 32).
2.  Only usable by a flow control instruction.
3.  Only usable by a texture sampling instruction.
4.  partial(x, y, z, w) - If only a subset of channels are updated in the register, the remaining channels will default to specified values (x, y, z, w).
5.  Defaults for sampler lookups exist, but values depend on texture format.

The number of readports is the number of different registers (for each register type) that can be read in a single instruction.

## Output Register Types



| Register | Name                                                                              | Count                                                                             | R/W | Dimension | RelAddr | Defaults | Requires DCL |
|----------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----|-----------|---------|----------|--------------|
| oC#     | [Output Color Register](dx9-graphics-reference-asm-ps-registers-output-color.md) | See [Multiple-element Textures (Direct3D 9)](/windows/desktop/direct3d9/multiple-element-textures) | W   | 4         | N       | None     | N            |
| oDepth   | [Output Depth Register](dx9-graphics-reference-asm-ps-registers-output-depth.md) | 1                                                                                 | W   | 1         | N       | None     | N            |



 

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 