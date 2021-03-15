---
title: pow - ps
description: Full precision abs(src0)src1. | pow - ps
ms.assetid: 39037c51-a524-459c-8422-bd7831e2aa3d
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# pow - ps

Full precision abs(src0)<sup>src1</sup>.

## Syntax



| pow dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is an input source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.
-   src1 is an input source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| pow                   |      |      |      |      | x    | x    | x     | x    | x     |



 

This instruction works as follows:

dest.x = dest.y = dest.z = dest.w = \[abs(src0)\]<sup>src1</sup>;

This is a scalar instruction, therefore the source registers should have replicate swizzles to indicate which channels are used.

The input power (src1) must be a scalar.

The scalar result is replicated to all four output channels.

This instruction could be expanded as exp(src1 \* log(src0)).

The dst register should be a temporary register, and should not be the same register as src1.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




