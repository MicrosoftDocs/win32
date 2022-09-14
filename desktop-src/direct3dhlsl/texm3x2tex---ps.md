---
title: texm3x2tex - ps
description: Performs the final row of a 3x2 matrix multiply and uses the result to do a texture lookup. texm3x2tex must be used in conjunction with the texm3x2pad - ps instruction.
ms.assetid: c6cfbf75-4a63-4c82-9fb6-286b51b7f883
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x2tex - ps

Performs the final row of a 3x2 matrix multiply and uses the result to do a texture lookup. texm3x2tex must be used in conjunction with the [texm3x2pad - ps](texm3x2pad---ps.md) instruction.

## Syntax



| texm3x2tex dst, src |
|---------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x2tex            | x    | x    | x    |      |      |      |       |      |       |



 

The instruction is used as one of two instructions representing a 3x2 matrix multiply operation. This instruction must be used with the [texm3x2pad - ps](texm3x2pad---ps.md) instruction.

When using these two instructions, texture registers must use the following sequence.


```
 
tex t(n)                      // Define tn as a standard 3-vector (tn must 
                              // be defined in some way before it is used)
texm3x2pad  t(m),   t(n)      // where m > n
                              // Perform first row of matrix multiply
texm3x2tex  t(m+1), t(n)      // Perform second row of matrix multiply 
                              // to get (u,v) to sample texture 
                              // associated with stage m+1
```



Here is more detail about how the 3x2 multiply is accomplished.

The texm3x2pad instruction performs the first row of the multiply to find u<sup>'</sup>.

u<sup>'</sup> = t(n)<sub>RGB</sub> \* TextureCoordinates(stage m)<sub>UVW</sub>

The texm3x2tex instruction performs the second row of the multiply to find v<sup>'</sup>.

v<sup>'</sup> = t(n)<sub>RGB</sub> \* TextureCoordinates(stage m+1)<sub>UVW</sub>

The texm3x2tex instruction samples the texture on stage (m+1) with (u<sup>'</sup>,v<sup>'</sup>) and stores the result in t(m+1).

t(m+1)<sub>RGB</sub> = TextureSample(stage m+1)<sub>RGB</sub> using (u<sup>'</sup>, v<sup>'</sup> ) as coordinates

## Examples

Here is an example shader with the texture maps and the texture stages identified.


```
ps_1_1
tex t0                // Bind texture in stage 0 to register t0
texm3x2pad  t1,  t0   // First row of matrix multiply
texm3x2tex  t2,  t0   // Second row of matrix multiply to get (u,v)
                      // with which to sample texture in stage 2
mov r0, t2            // Output result
```



This example requires the following textures in the following texture stages.

-   Stage 0 takes a map with (x,y,z) perturbation data.
-   Stage 1 holds texture coordinates. No texture is required in the texture stage.
-   Stage 2 holds both texture coordinates as well as a 2D texture set at that texture stage.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




