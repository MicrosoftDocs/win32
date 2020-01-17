---
title: texm3x2pad - ps
description: Performs the first row multiplication of a two-row matrix multiply. This instruction must be combined with either texm3x2tex - ps or texm3x2depth - ps. Refer to either of these instructions for details on using texmpad.
ms.assetid: 26eb3237-6e48-4880-b40d-37de8d65daa6
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x2pad - ps

Performs the first row multiplication of a two-row matrix multiply. This instruction must be combined with either [texm3x2tex - ps](texm3x2tex---ps.md) or [texm3x2depth - ps](texm3x2depth---ps.md). Refer to either of these instructions for details on using texmpad.

## Syntax



| tex3x2pad dst, src |
|--------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x2pad            | x    | x    | x    |      |      |      |       |      |       |



 

This instruction cannot be used by itself.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




