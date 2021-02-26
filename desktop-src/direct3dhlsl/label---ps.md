---
title: label - ps
description: Mark the next instruction as having a label index. | label - ps
ms.assetid: 21afa062-c536-4891-ba69-ca5284b0539c
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# label - ps

Mark the next instruction as having a label index.

## Syntax



| label l\# |
|-----------|



 

where \# identifies the label number.

For ps\_2\_x, the label number must be between between 0 and 15.

For ps\_2\_sw, ps\_3\_0, and ps\_3\_sw, the label number must be between between 0 and 2047.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| label                 |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction defines a label located at the next shader instruction. The label instruction can only be present directly after a [ret](ret---ps.md) instruction (which defines the end of the previous subroutine or main program).

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




