---
title: dcl - (sm2, sm3 - ps asm)
description: Declare a pixel shader input register.
ms.assetid: d6fcd94e-80d7-4e8a-8b4f-ff86c980cc38
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl - (sm2, sm3 - ps asm)

Declare a pixel shader input register.

## Syntax

dcl\[\_pp\] dest\[.mask\]



 

Where:

-   \[\_pp\] is optional partial precision. See [Partial Precision](dx9-graphics-reference-asm-ps-instructions-modifiers-ps-2-0.md).
-   dest is a destination register. It must be either a [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md) (vn), or an [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md) (tn).
-   \[.mask\] is an optional write mask that controls which components of the destination register that can be written to. See [Destination Register Write Mask](dx9-graphics-reference-asm-ps-registers-modifiers-write-mask.md).

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dcl                   |      |      |      |      | x    | x    | x     | x    | x     |



 

All dcl instructions must appear before the first executable instruction.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




