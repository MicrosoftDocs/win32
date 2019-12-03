---
title: texm3x3tex - ps
description: Performs a 3x3 matrix multiply and uses the result to do a texture lookup. texm3x3tex must be used with two texm3x3pad - ps instructions.
ms.assetid: bb61cd6f-57d0-4b2d-9186-f04f7f4d3516
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texm3x3tex - ps

Performs a 3x3 matrix multiply and uses the result to do a texture lookup. texm3x3tex must be used with two [texm3x3pad - ps](texm3x3pad---ps.md) instructions.

## Syntax



| texm3x3tex dst, src |
|---------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texm3x3tex            | x    | x    | x    |      |      |      |       |      |       |



 

This instruction is used as the final of three instructions representing a 3x3 matrix multiply operation, followed by a texture lookup. The 3x3 matrix is comprised of the texture coordinates of the third texture stage and the two preceding texture stages. The resulting three-component vector (u,v,w) is used to sample the texture in stage 3. Any texture assigned to the preceding two texture stages is ignored. The 3x3 matrix multiply is typically useful for orienting a normal vector to the correct tangent space for the surface being rendered.

This instruction must be used with the texm3x3pad instruction. Texture registers must use the following sequence.


```
 
tex t(n)                 // Define tn as a standard 3-vector (tn must
                         //   be defined in some way before it is used)
texm3x3pad t(m),   t(n)  //   where m > n
                         // Perform first row of matrix multiply
texm3x3pad t(m+1), t(n)  // Perform second row of matrix multiply
texm3x3tex t(m+2), t(n)  // Perform third row of matrix multiply to get a
                         //   3-vector with which to sample texture
                         //   associated with texture stage m+2
```



Here is more detail about how the 3x3 multiply is accomplished.

The first texm3x3pad instruction performs the first row of the multiply to find u<sup>'</sup>.

u<sup>'</sup> = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The second texm3x3pad instruction performs the second row of the multiply to find v<sup>'</sup>.

v<sup>'</sup> = TextureCoordinates(stage m+1)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The texm3x3spec instruction performs the third row of the multiply to find w<sup>'</sup>.

w<sup>'</sup> = TextureCoordinates(stage m+2)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

Lastly, the texm3x3tex instruction samples t(m+2) with (u<sup>'</sup>,v<sup>'</sup>,w<sup>'</sup>) and stores the result in t(m+2).

t(m+2)<sub>RGBA</sub> = TextureSample(stage m+2)<sub>RGBA</sub> using (u<sup>'</sup> , v<sup>'</sup> , w<sup>'</sup> ) as coordinates.

## Examples

Here is an example shader with the texture maps identified and the texture stages identified.


```
ps_1_1
tex t0                // Bind texture in stage 0 to register t0
texm3x3pad  t1,  t0   // First row of matrix multiply
texm3x3pad  t2,  t0   // Second row of matrix multiply
texm3x3tex  t3,  t0   // Third row of matrix multiply to get a
                      // 3-vector with which to sample texture at 
mov r0, t3            // stage 3 output result
```



This example requires the following texture stage setup.

-   Stage 0 is assigned a texture map with normal data. This is often referred to as a bump map. The data is (XYZ) normals for each texel. Texture coordinate set 0 defines how to sample this normal map.
-   Texture coordinate set 1 is assigned to row 1 of the 3x3 matrix. Any texture assigned to stage 1 is ignored.
-   Texture coordinate set 2 is assigned to row 2 of the 3x3 matrix. Any texture assigned to stage 2 is ignored.
-   Texture coordinate set 3 is assigned to row 3 of the 3x3 matrix. A volume or cube texture should be set to stage 3 for lookup by the transformed 3D vector.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




