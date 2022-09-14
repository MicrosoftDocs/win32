---
title: Registers - vs_2_0
description: This section contains reference information for the input and output registers implemented by vertex shader version 2\_0.
ms.assetid: e5ef015e-1e4d-41b3-95da-3b44ef0bd73e
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - vs\_2\_0

This section contains reference information for the input and output registers implemented by vertex shader version 2\_0.

## Input Registers



| Register | Name                                                                                      | Count      | R/W | \# Read ports | \# Reads / inst | Dimension | RelAddr | Defaults     | Requires DCL |
|----------|-------------------------------------------------------------------------------------------|------------|-----|---------------|-----------------|-----------|---------|--------------|--------------|
| v\#      | [Input Register](dx9-graphics-reference-asm-vs-registers-input.md)                       | 16         | R   | 1             | Unlimited       | 4         | No      | See note 1   | Yes          |
| r\#      | [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)               | 12         | R/W | 3             | Unlimited       | 4         | No      | None         | No           |
| c\#      | [Constant Float Register](dx9-graphics-reference-asm-vs-registers-constant-float.md)     | See note 2 | R   | 1             | 2               | 4         | a0 / aL | (0, 0, 0, 0) | No           |
| a0       | [Address Register](dx9-graphics-reference-asm-vs-registers-address.md)                   | 1          | R/W | 1             | 2               | 4         | No      | None         | No           |
| b\#      | [Constant Boolean Register](dx9-graphics-reference-asm-vs-registers-constant-boolean.md) | 16         | R   | 1             | 1               | 1         | No      | FALSE        | No           |
| i\#      | [Constant Integer Register](dx9-graphics-reference-asm-vs-registers-constant-integer.md) | 16         | R   | 1             | 1               | 4         | No      | (0, 0, 0, 0) | No           |
| aL       | [Loop Counter Register](dx9-graphics-reference-asm-vs-registers-loop-counter.md)         | 1          | R   | 1             | 2               | 1         | No      | None         | No           |



 

Notes:

1.  Partial (0, 0, 0, 1) - If only a subset of channels are updated, the remaining channels will default to (0, 0, 0, 1).
2.  Equal to D3DCAPS9.MaxVertexShaderConst (at least 256 for vs\_2\_0).

## Output Registers



| Register | Name                                                                                          | Count | R/W | Dimension | RelAddr | Defaults | Requires DCL |
|----------|-----------------------------------------------------------------------------------------------|-------|-----|-----------|---------|----------|--------------|
| oPos     | [Position Register](dx9-graphics-reference-asm-vs-registers-position.md)                     | 1     | W   | 4         | No      | None     | No           |
| oFog     | [Fog Register](dx9-graphics-reference-asm-vs-registers-fog.md)                               | 1     | W   | 1         | No      | None     | No           |
| oPts     | [Point Size Register](dx9-graphics-reference-asm-vs-registers-point-size.md)                 | 1     | W   | 1         | No      | None     | No           |
| oD\#     | [Color Register](dx9-graphics-reference-asm-vs-registers-color.md); See note 1               | 2     | W   | 4         | No      | None     | No           |
| oT\#     | [Texture Coordinate Register](dx9-graphics-reference-asm-vs-registers-texture-coordinate.md) | 8     | W   | 4         | No      | None     | No           |



 

Notes:

-   oD0 is the diffuse color output; oD1 is the specular color output.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




