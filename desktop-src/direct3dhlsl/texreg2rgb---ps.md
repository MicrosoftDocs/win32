---
title: texreg2rgb - ps
description: Interprets the red, green, and blue (RGB) color components of the source register as texture address data in order to sample the texture at the stage corresponding to the destination register number. The result is stored in the destination register.
ms.assetid: 8ec44014-d796-407c-8fe0-036decaf2a3d
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texreg2rgb - ps

Interprets the red, green, and blue (RGB) color components of the source register as texture address data in order to sample the texture at the stage corresponding to the destination register number. The result is stored in the destination register.

## Syntax



| texreg2rgb dst, src |
|---------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texreg2rgb            |      | x    | x    |      |      |      |       |      |       |



 

This instruction is useful for color-space remapping operations. It supports two-dimensional (2D) and three-dimensional (3D) coordinates. It can be used just like the [texreg2ar - ps](texreg2ar---ps.md) or [texreg2gb - ps](texreg2gb---ps.md) to remap 2D data. However, this instruction also supports 3D data so it can be used with cube maps and 3D volume textures.

Here is an example of the sequence the instruction follows.


```
 
tex t(n)
texreg2rgb t(m), t(n)     where m > n
```



Here is more detail about how the remapping is accomplished.

<dl> // The first instruction loads the texture color (RGBA) into register tn  
tex tn  
// The second instruction remaps the color  
t(m)<sub>RGBA</sub> = TextureSample(stage m)<sub>RGBA</sub> using t(n)<sub>RGB</sub> as coordinates  
</dl>

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




