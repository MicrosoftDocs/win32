---
title: texreg2gb - ps
description: Interprets the green and blue color components of the source register as texture address data to sample the texture at the stage corresponding to the destination register number.
ms.assetid: 81d3fb3e-ef53-4d25-b65d-c4c9fea0c74c
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texreg2gb - ps

Interprets the green and blue color components of the source register as texture address data to sample the texture at the stage corresponding to the destination register number.

## Syntax



| texreg2gb dst, src |
|--------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texreg2gb             |      | x    | x    |      |      |      |       |      |       |



 

This instruction is useful for color-space remapping operations.

Here is an example of the sequence the instruction follows.

<dl> tex t(n)  
texreg2gb t(m), t(n) where m > n  
// The first instruction loads the texture color (RGBA)  
// into register tn  
tex tn  
// The second instruction remaps the color  
t(m)<sub>RGBA</sub> = TextureSample(stage m)<sub>RGBA</sub> using t(n)<sub>GB</sub> as coordinates  
</dl>

\_bx2 cannot be used on the src register for [texreg2ar - ps](texreg2ar---ps.md) or texreg2gb instructions.

For this instruction, the source register must use unsigned data. Use of signed or mixed data in the source register will produce undefined results. For more information, see [D3DFORMAT](/windows/desktop/direct3d9/d3dformat).

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 