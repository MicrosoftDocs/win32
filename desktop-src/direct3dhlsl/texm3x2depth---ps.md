---
title: texm3x2depth - ps
description: Calculate the depth value to be used in depth testing for this pixel.
ms.assetid: bacdd471-a6ee-4998-badd-93ffd4fd61d4
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x2depth - ps

Calculate the depth value to be used in depth testing for this pixel.

## Syntax



| texm3x2depth dst, src |
|-----------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x2depth          |      |      | x    |      |      |      |       |      |       |



 

This instruction must be used with the [texm3x2pad - ps](texm3x2pad---ps.md) instruction.

When using these two instructions, texture registers must use the following sequence.


```
 
tex t(n)                     // Define tn as a standard 3-vector.(tn must be 
                             // defined in some way before it is used
texm3x2pad   t(m),   t(n)    // Where m > n
                             // Calculate z value
texm3x2depth t(m+1), t(n)    // Calculate w value; use both z and w to
                             // find depth
```



The depth calculation is done after using a dot product operation to find z and w. Here is more detail about how the depth calculation is accomplished.

The texm3x2pad instruction calculates z.

z = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The texm3x2depth instruction calculates w.

w = TextureCoordinates(stage m+1)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

Calculate depth and store the result in t(m+1).


```
 
if (w == 0)
  t(m+1) = 1.0
else
  t(m+1) = z/w
```



The calculated depth is tagged to be used in the depth test for the pixel, replacing the existing depth test value for the pixel.

Be sure to clamp z/w to be in the range of (0-1). If z/w is outside this range, the result stored in the depth buffer will be undefined.

After running texm3x2depth, register t(m+1) is no longer available for use in the shader.

When multisampling, using this instruction eliminates most of the benefit of the higher resolution depth buffer. Because the pixel shader runs once per pixel, the single depth value output by texm3x2depth or [texdepth - ps](texdepth---ps.md) will be used for each of the subpixel depth comparison tests.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




