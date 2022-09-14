---
title: texm3x3 - ps
description: Performs a 3x3 matrix multiply when used in conjunction with two texm3x3pad - ps instructions.
ms.assetid: d0b14c87-3507-4237-9f2c-1eb94a6df71c
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x3 - ps

Performs a 3x3 matrix multiply when used in conjunction with two [texm3x3pad - ps](texm3x3pad---ps.md) instructions.

## Syntax



| texm3x3 dst, src |
|------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x3               |      | x    | x    |      |      |      |       |      |       |



 

This instruction is the same as the [texm3x3tex - ps](texm3x3tex---ps.md) instruction, without the texture lookup.

This instruction is used as the final of three instructions representing a 3x3 matrix multiply operation. The 3x3 matrix is comprised of the texture coordinates of the third texture stage, and by the two preceding texture stages. Any texture assigned to any of the three texture stages is ignored.

This instruction must be used with two texm3x3pad instructions. Texture registers must follow the following sequence.


```
 
tex t(n)                 // Define tn as a standard 3-vector (tn must
                         // be defined in some way before it is used)
texm3x3pad t(m),   t(n)  // where m > n
                         // Perform first row of matrix multiply
texm3x3pad t(m+1), t(n)  // Perform second row of matrix multiply
texm3x3    t(m+2), t(n)  // Perform third row of matrix multiply to get a
                         // 3-vector result
```



Here is more detail about how the 3x3 multiply is accomplished.

The first texm3x3pad instruction performs the first row of the multiply to find u<sup>'</sup>.

u<sup>'</sup> = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The second texm3x3pad instruction performs the second row of the multiply to find v<sup>'</sup>.

v<sup>'</sup> = TextureCoordinates(stage m+1)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The texm3x3tex instruction performs the third row of the multiply to find w<sup>'</sup>.

w<sup>'</sup> = TextureCoordinates(stage m+2)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

Place the result of the matrix multiply in the destination register.

t(m+2)<sub>RGBA</sub> = (u<sup>'</sup> , v<sup>'</sup> , w<sup>'</sup> , 1)

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




