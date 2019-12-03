---
title: texm3x3pad - ps
description: Performs the first or second row multiply of a three-row matrix multiply. This instruction must be used in combination with texm3x3 - ps, texm3x3spec - ps, texm3x3vspec - ps, or texm3x3tex - ps.
ms.assetid: 375526ee-cd58-4179-9b21-c63f17282f6b
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x3pad - ps

Performs the first or second row multiply of a three-row matrix multiply. This instruction must be used in combination with [texm3x3 - ps](texm3x3---ps.md), [texm3x3spec - ps](texm3x3spec---ps.md), [texm3x3vspec - ps](texm3x3vspec---ps.md), or [texm3x3tex - ps](texm3x3tex---ps.md).

## Syntax



| texm3x3pad dst, src |
|---------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x3pad            | x    | x    | x    |      |      |      |       |      |       |



 

This instruction cannot be used by itself.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




