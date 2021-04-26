---
title: texld - ps_1_4
description: Loads the destination register with color data (RGBA) sampled using the contents of the source register as texture coordinates. The sampled texture is the texture associated with the destination register number.
ms.assetid: 1970aed4-4da7-40a1-960d-fba4dfd8c433
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texld - ps\_1\_4

Loads the destination register with color data (RGBA) sampled using the contents of the source register as texture coordinates. The sampled texture is the texture associated with the destination register number.



| texld dst, src |
|----------------|



 

## Registers



|          |                      | vₙ        | cₙ  | tₙ  | rₙ  |              |
|----------|----------------------|-----------|-----|-----|-----|--------------|
| dst      | Destination register |           |     |     | x   | 1\_4         |
| src      | Source register      |           |     | x   |     | 1\_4 phase 1 |
|          |                      |           |     | x   | x   | 1\_4 phase   |



 

When using r(n) as a source register, the first three components (XYZ) must have been initialized in the previous phase of the shader.

To learn more about registers, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

This instruction samples the texture in the texture stage associated with the destination register number. The texture is sampled using texture coordinate data from the source register.

The syntax for the texld and texcrd instructions expose support for a projective divide with a Texture Register Modifier. For pixel shader version 1.4, the D3DTTFF\_PROJECTED texture transform flag is always ignored.

Rules for using texld:

1.  The same .xyz or .xyw modifier must be applied to every read of an individual t(n) register within both texcrd or texld instructions. If .xyw is being used on t(n) register reads, this can be mixed with other reads of the same t(n) register using .xyw\_dw.
2.  The \_dz source modifier is only valid on texld with r(n) source register (thus phase 2 only).
3.  The \_dz source modifier may be used no more than two times per shader.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texld                 |      |      |      | x    |      |      |       |      |       |



 

## Examples

The texld instruction offers some control over which components of the source texture coordinate data are used. The complete set of allowed syntax for texld follows, and includes all valid source register modifiers, selectors, and write mask combinations.


```
texld  r(m), t(n).xyz
// Uses xyz from t(n) to sample 1D, 2D, or 3D texture
```




```
texld  r(m), t(n)
// Same as previous
```




```
texld  r(m), t(n).xyw
// Uses xyw (skipping z) from t(n) to sample 1D, 2D or 3D texture
```




```
texld  r(m), t(n)_dw.xyw  
// Samples 1D or 2D texture at x/w, y/w from t(n). The result
// is undefined for a cube-map lookup.
```




```
texld  r(m), r(n).xyz
// Samples 1D, 2D, or 3D texture at xyz from r(m) 
// This is possible in the second phase of the shader
```




```
texld  r(m), r(n)
// Same as previous
```




```
texld  r(m), r(n)_dz.xyz
// Samples 1D or 2D texture at x/z, y/z from r(m)
// Possible only in second phase
// The result is undefined for a cube-map lookup
```




```
texld  r(n), r(n)_dz
// Same as previous
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




