---
title: texm3x3vspec - ps
description: Performs a 3x3 matrix multiply and uses the result to perform a texture lookup.
ms.assetid: 3798bc23-2929-48fe-93ae-5aa025823714
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x3vspec - ps

Performs a 3x3 matrix multiply and uses the result to perform a texture lookup. This can be used for specular reflection and environment mapping where the eye-ray vector is not constant. texm3x3vspec must be used in conjunction with two [texm3x3pad - ps](texm3x3pad---ps.md) instructions. If the eye-ray vector is constant, the [texm3x3spec - ps](texm3x3spec---ps.md) instruction will perform the same matrix multiply and texture lookup.

## Syntax



| texm3x3vspec dst, src |
|-----------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x3vspec          | x    | x    | x    |      |      |      |       |      |       |



 

This instruction performs the final row of a 3x3 matrix multiply operation, interprets the resulting vector as a normal vector to reflect an eye-ray vector, and then uses the reflected vector as a texture address for a texture lookup. It works just like [texm3x3spec - ps](texm3x3spec---ps.md), except that the eye-ray vector is taken from the fourth component of the texture coordinates. The 3x3 matrix multiply is typically useful for orienting a normal vector to the correct tangent space for the surface being rendered.

The 3x3 matrix is comprised of the texture coordinates of the third texture stage and the two preceding texture stages. The resulting post-reflection vector (UVW) is used to sample the texture in stage 3. Any texture assigned to the preceding two texture stages is ignored.

This instruction must be used with the texm3x3pad instruction. Texture registers must use the following sequence.


```
tex t(n)                    // Define tn as a standard 3-vector (tn must
                            //   be defined in some way before it is used)
texm3x3pad   t(m),   t(n)   // where m > n
                            // Perform first row of matrix multiply
texm3x3pad   t(m+1), t(n)   // Perform second row of matrix multiply
texm3x3vspec t(m+2), t(n)   // Perform third row of matrix multiply
                            // Then do a texture lookup on the texture
                            // associated with texture stage m+2
```



The first texm3x3pad instruction performs the first row of the multiply to find u<sup>'</sup>.

u<sup>'</sup> = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n) <sub>RGB</sub>

The second texm3x3pad instruction performs the second row of the multiply to find v<sup>'</sup>.

v<sup>'</sup> = TextureCoordinates(stage m+1)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The texm3x3spec instruction performs the third row of the multiply to find w<sup>'</sup>.

w<sup>'</sup> = TextureCoordinates(stage m+2)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The texm3x3vspec instruction also does a reflection calculation.

(u<sup>'</sup> , v<sup>'</sup> , w<sup>'</sup> ) = 2\*\[(N\*E)/(N\*N)\]\*N - E

// where the normal N is given by

// N = (u<sup>'</sup> , v<sup>'</sup> , w<sup>'</sup> )

// and the eye-ray vector E is given by

// E = (TextureCoordinates(stage m)<sub>Q</sub> ,

// TextureCoordinates(stage m+1)<sub>Q</sub> ,

// TextureCoordinates(stage m+2)<sub>Q</sub> )

Lastly, the texm3x3vspec instruction samples t(m+2) with (u<sup>'</sup>,v<sup>'</sup>,w<sup>'</sup>)and stores the result in t(m+2).

t(m+2)<sub>RGBA</sub> = TextureSample(stage m+2)<sub>RGBA</sub> using (u<sup>'</sup> , v<sup>'</sup> , w<sup>'</sup> ) as coordinates

## Examples

Here is an example shader with the texture maps identified and the texture stages identified.


```
ps_1_1
tex t0                // Bind texture in stage 0 to register t0
texm3x3pad   t1,  t0  // First row of matrix multiply
texm3x3pad   t2,  t0  // Second row of matrix multiply
texm3x3vspec t3,  t0  // Third row of matrix multiply to get a 3-vector
                      // Reflect 3-vector by the eye-ray vector
                      // Use reflected vector to do a texture lookup
                      //   at stage 3
mov r0, t3            // Output the result
```



This example requires the following texture stage setup.

-   Stage 0 is assigned a texture map with normal data. This is often referred to as a bump map. The data is (XYZ) normals for each texel. Texture coordinates at stage n defines how to sample this normal map.
-   Texture coordinate set m is assigned to row 1 of the 3x3 matrix. Any texture assigned to stage m is ignored.
-   Texture coordinate set m+1 is assigned to row 2 of the 3x3 matrix. Any texture assigned to stage m+1 is ignored.
-   Texture coordinate set m+2 is assigned to row 3 of the 3x3 matrix. Stage m+2 is assigned a volume or cube texture map. The texture provides color data (RGBA).
-   The eye-ray vector E is passed into the instruction in the fourth component (q) of the texture coordinate data at stages m, m+1, and m+2.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




