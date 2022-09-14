---
title: texbem - ps
description: Apply a fake bump environment-map transform. This is accomplished by modifying the texture address data of the destination register, using address perturbation data (du,dv), and a 2D bump environment matrix.
ms.assetid: 8e773f4a-c7a2-4caf-973f-8f50dccc9c04
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texbem - ps

Apply a fake bump environment-map transform. This is accomplished by modifying the texture address data of the destination register, using address perturbation data (du,dv), and a 2D bump environment matrix.

## Syntax



| texbem dst, src |
|-----------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texbem                | x    | x    | x    |      |      |      |       |      |       |



 

The red and green color data in the src register is interpreted as the perturbation data (du,dv).

This instruction transforms red and green components in the source register using the 2D bump environment-mapping matrix. The result is added to the texture coordinate set corresponding to the destination register number, and is used to sample the current texture stage.

This operation always interprets du and dv as signed quantities. For versions 1\_0 and 1\_1, the [Source Register Signed Scaling](dx9-graphics-reference-asm-ps-registers-modifiers-signed-scale.md) input modifier (\_bx2) is not permitted on the input argument.

This instruction produces defined results when input textures contain signed format data. Mixed format data works only if the first two channels contain signed data. For more information about surface formats, see [D3DFORMAT](/windows/desktop/direct3d9/d3dformat).

This can be used for a variety of techniques based on address perturbation, including fake per-pixel environment mapping and diffuse lighting (bump mapping).

When using this instruction, texture registers must follow the following sequence.


```
// The texture assigned to stage t(n) contains the (du,dv) data
// The texture assigned to stage t(m) is sampled
tex     t(n)                    
texbem  t(m),  t(n)      where m > n
```



The calculations done within the instruction are shown below.


```
// 1. New values for texture addresses (u',v') are calculated
// 2. Sample the texture using (u',v')
```



u' = TextureCoordinates(stage m)<sub>u</sub> + D3DTSS\_BUMPENVMAT00(stage m)\*t(n)<sub>R</sub> + D3DTSS\_BUMPENVMAT10(stage m)\*t(n)<sub>G</sub> v' = TextureCoordinates(stage m)<sub>v</sub> + D3DTSS\_BUMPENVMAT01(stage m)\*t(n)<sub>R</sub> + D3DTSS\_BUMPENVMAT11(stage m)\*t(n)<sub>G</sub> t(m)<sub>RGBA</sub> = TextureSample(stage m)

// using (u',v') as coordinates

Register data that has been read by a texbem - ps or [texbeml - ps](texbeml---ps.md) instruction cannot be read later, except by another texbem - ps or texbeml - ps.


```
// This example demonstrates the validation error caused by t0 being reread:
ps_1_1
tex t0
texbem t1, t0
add r0, t1, t0

(Instruction Error) (Statement 4) Register data that has been read by 
texbem or texbeml instruction cannot be read by other instructions
```



## Examples

Here is an example shader with the texture maps identified and the texture stages identified.


```
ps_1_1
tex t0              ; Define t0 to get a 2-tuple DuDv
texbem t1, t0       ; Compute (u',v')
                    ; Sample t1 using (u',v')
mov r0, t1          ; Output result
```



texbem requires the following textures in the following texture stages.

-   Stage 0 is assigned a bump map with (du, dv) perturbation data.
-   Stage 1 uses a texture map with color data.
-   This instruction sets the matrix data on the texture stage that is sampled.
-   This is different from the functionality of the fixed function pipeline where the perturbation data and the matrices occupy the same texture stage.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 