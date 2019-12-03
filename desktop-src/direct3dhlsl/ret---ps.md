---
title: ret - ps
description: Takes the address of an instruction from the return address stack and continues execution from it. In the case of the main function, this instruction stops shader execution.
ms.assetid: f853a137-8944-4f6e-89c0-7fd37d1a468e
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# ret - ps

Takes the address of an instruction from the return address stack and continues execution from it. In the case of the main function, this instruction stops shader execution.

## Syntax



| ret |
|-----|



 

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| ret                   |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction takes the address of an instruction from the return address stack and continues execution from it. In the case of the main function, this instruction stops shader execution.

The ret instruction consumes one vertex shader instruction slot.

If a shader contains no subroutines, using ret at the end of the main program is optional.

Multiple return statements are not permitted in the main program or in any subroutine, the first return statement is treated as the end of the main program or subroutine.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




