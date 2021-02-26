---
title: label - vs
description: Mark the next instruction as having a label index. | label - vs
ms.assetid: e1aee8bc-4655-4bd5-8012-bd7a2d46e712
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# label - vs

Mark the next instruction as having a label index.

## Syntax



| label l\# |
|-----------|



 

where \# identifies the label number.

For vs\_2\_0, and vs\_2\_x, the label number must be between between 0 and 15.

For vs\_2\_sw, vs\_3\_0 and vs\_3\_sw, the label number must be between between 0 and 2047.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| label                  |      | x    | x    | x     | x    | x     |



 

This instruction defines a label located at the next shader instruction. The label instruction can only be present directly after a [ret](ret---vs.md) instruction (which defines the end of the previous subroutine or main program).

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




