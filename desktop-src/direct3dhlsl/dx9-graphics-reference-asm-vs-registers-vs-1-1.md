---
title: Registers - vs_1_1
description: This section contains reference information for the input and output registers implemented by vertex shader version 1\_1.
ms.assetid: 8b19a0da-1561-450f-a36a-35ac7ea6e17a
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - vs\_1\_1

This section contains reference information for the input and output registers implemented by vertex shader version 1\_1.

## Input Registers



| Register | Name                                                                                  | Count      | R/W | \# Read ports | \# Reads / inst | Dimension  | RelAddr | Defaults     | Requires DCL |
|----------|---------------------------------------------------------------------------------------|------------|-----|---------------|-----------------|------------|---------|--------------|--------------|
| a0       | [Address Register](dx9-graphics-reference-asm-vs-registers-address.md)               | 1          | R/W | 1             | Unlimited       | See note 3 | No      | None         | No           |
| c\#      | [Constant Float Register](dx9-graphics-reference-asm-vs-registers-constant-float.md) | See note 2 | R   | 1             | Unlimited       | 4          | a0.x    | (0, 0, 0, 0) | No           |
| v\#      | [Input Register](dx9-graphics-reference-asm-vs-registers-input.md)                   | 16         | R   | 1             | Unlimited       | 4          | No      | See note 1   | Yes          |
| r\#      | [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)           | 12         | R/W | 3             | Unlimited       | 4          | No      | None         | No           |



 

Notes:

1.  Partial (0, 0, 0, 1) - If only a subset of channels are updated, the remaining channels will default to (0, 0, 0, 1).
2.  Equal to D3DCAPS9.MaxVertexShaderConst (at least 96 for vs\_1\_1).
3.  Only .x channel is available.

## Output Registers



| Register | Name                        | Count | R/W | Dimension | RelAddr | Defaults | Requires DCL |
|----------|-----------------------------|-------|-----|-----------|---------|----------|--------------|
| oPos     | Position Register           | 1     | W   | 4         | No      | None     | No           |
| oFog     | Fog Register                | 1     | W   | 1         | No      | None     | No           |
| oPts     | Point Size Register         | 1     | W   | 1         | No      | None     | No           |
| oD\#     | Color Register; See note 1  | 2     | W   | 4         | No      | None     | No           |
| oT\#     | Texture Coordinate Register | 8     | W   | 4         | No      | None     | No           |



 

Notes:

-   oD0 is the diffuse color output; oD1 is the specular color output.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




