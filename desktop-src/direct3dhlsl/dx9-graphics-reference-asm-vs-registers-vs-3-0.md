---
title: Registers - vs_3_0
description: This section contains reference information for the input and output registers implemented by vertex shader version 3\_0.
ms.assetid: af81f1c4-9c11-455e-a565-1b80f1ee8683
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - vs\_3\_0

This section contains reference information for the input and output registers implemented by vertex shader version 3\_0.

## Input Registers



| Register | Name                                                                                      | Count      | R/W | \# Read ports | \# Reads / inst | Dimension | RelAddr | Defaults     | Requires DCL |
|----------|-------------------------------------------------------------------------------------------|------------|-----|---------------|-----------------|-----------|---------|--------------|--------------|
| v\#      | [Input Register](dx9-graphics-reference-asm-vs-registers-input.md)                       | 16         | R   | 1             | Unlimited       | 4         | a0/aL   | See note 1   | Yes          |
| r\#      | [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)               | 32         | R/W | 3             | Unlimited       | 4         | No      | None         | No           |
| c\#      | [Constant Float Register](dx9-graphics-reference-asm-vs-registers-constant-float.md)     | See note 2 | R   | 1             | Unlimited       | 4         | a0/aL   | (0, 0, 0, 0) | No           |
| a0       | [Address Register](dx9-graphics-reference-asm-vs-registers-address.md)                   | 1          | R/W | 1             | Unlimited       | 4         | No      | None         | No           |
| b\#      | [Constant Boolean Register](dx9-graphics-reference-asm-vs-registers-constant-boolean.md) | 16         | R   | 1             | 1               | 1         | No      | FALSE        | No           |
| i\#      | [Constant Integer Register](dx9-graphics-reference-asm-vs-registers-constant-integer.md) | 16         | R   | 1             | 1               | 4         | No      | (0, 0, 0, 0) | No           |
| aL       | [Loop Counter Register](dx9-graphics-reference-asm-vs-registers-loop-counter.md)         | 1          | R   | 1             | Unlimited       | 1         | No      | None         | No           |
| p0       | [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md)               | 1          | R/W | 1             | 1               | 4         | no      | none         | no           |
| s\#      | [Sampler (Direct3D 9 asm-vs)](dx9-graphics-reference-asm-vs-registers-sampler.md)        | 4          | R   | 1             | 1               | 4         | No      | See note 3   | Yes          |



 

Notes:

1.  Partial (0, 0, 0, 1) - If only a subset of channels are updated, the remaining channels will default to (0, 0, 0, 1).
2.  Equal to D3DCAPS9.MaxVertexShaderConst (at least 256 for vs\_3\_0).
3.  Defaults for sampler lookup exist, but values depend on texture format.

## Output Registers

Output registers have been collapsed into 12 o\# (output) registers. These can be used for anything the user wants to interpolate for the pixel shader: texture coordinates, colors, fog, etc.



| Register | Name            | Count | R/W | Dimension | RelAddr | Defaults | Requires DCL |
|----------|-----------------|-------|-----|-----------|---------|----------|--------------|
| o\#      | Output Register | 12    | W   | 4         | aL      | None     | Yes          |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




