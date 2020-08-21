---
title: texreg2ar - ps
description: Interprets the alpha and red color components of the source register as texture address data (u,v) to sample the texture at the stage corresponding to the destination register number. The result is stored in the destination register.
ms.assetid: b31a2ee4-f9b9-4aee-b3be-7ccc5b8c6f3e
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texreg2ar - ps

Interprets the alpha and red color components of the source register as texture address data (u,v) to sample the texture at the stage corresponding to the destination register number. The result is stored in the destination register.

## Syntax



| texreg2ar dst, src |
|--------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texreg2ar             | x    | x    | x    |      |      |      |       |      |       |



 

This instruction is useful for color-space remapping operations.

Here is an example of the sequence the instruction follows:

<dl> tex t(n)  
texreg2ar t(m), t(n) where m > n  
// The first instruction loads the texture color (RGBA)  
// into register tn  
tex tn  
// The second instruction remaps the color  
t(m)<sub>RGBA</sub> = TextureSample(stage m)<sub>RGBA</sub> using t(n)<sub>AR</sub> as coordinates  
</dl>

\_bx2 cannot be used on the src register for texreg2ar or [texreg2gb - ps](texreg2gb---ps.md) instructions.

For this instruction, the source register must use unsigned data. Use of signed or mixed data in the source register will produce undefined results. For more information, see [D3DFORMAT](/windows/desktop/direct3d9/d3dformat).

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 