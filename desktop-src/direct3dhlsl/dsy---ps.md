---
title: dsy - ps
description: Compute the rate of change in the render target's y-direction.
ms.assetid: b35862d7-fc43-4cf8-bfe3-3eccbda2a133
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dsy - ps

Compute the rate of change in the render target's y-direction.

## Syntax



| dsy dst, src |
|--------------|



 

Where:

-   dst is a destination register.
-   src is an input source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dsy                   |      |      |      |      |      | x    | x     | x    | x     |



 

The rate of change computed from the source register is an approximation on the contents of the same register in adjacent pixel(s) running the pixel shader in lock-step with the current pixel.

The [dsx](dsx---ps.md) And dsy instructions compute their result by looking at the current contents of the source register (per component) for the various pixels in the local area executing in the lock-step. The exact formula used to compute the gradient varies depending on the hardware but should be consistent with the way the hardware does the same operations as part of the level-of-detail calculation process for texture sampling.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> <dt>

[texldd - ps](texldd---ps.md)
</dt> </dl>

 

 




