---
title: texcrd - ps
description: Copies texture coordinate data from the source texture coordinate iterator register as color data in the destination register.
ms.assetid: b3330d70-6e18-4494-a01c-51f0a282e305
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texcrd - ps

Copies texture coordinate data from the source texture coordinate iterator register as color data in the destination register.

## Syntax



| texcrd dst, src |
|-----------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texcrd                |      |      |      | x    |      |      |       |      |       |



 

This instruction interprets coordinate data as color data (RGBA).

No texture is sampled by this instruction. Only texture coordinates set on this texture stage are relevant.

When using texcrd, keep in mind the following detail about how data is copied from the source register to the destination register. The source texture coordinate register (t\#) holds data in the range \[-D3DCAPS9.MaxTextureRepeat, D3DCAPS9.MaxTextureRepeat\], while the destination register (r\#) can hold data only in the (likely smaller) range \[-D3DCAPS9.PixelShader1xMaxValue, D3DCAPS9.PixelShader1xMaxValue\]. Note that for pixel shader version 1\_4, D3DCAPS9.PixelShader1xMaxValue must be a minimum of eight. The texcrd instruction, in the process of clamping source data that is out of range of the destination register, is likely to behave differently on different hardware. The first pixel shader version 1\_4 hardware on the market will perform a special clamp for values outside of range. This clamp is designed to produce a number that can fit into the destination register, but also to preserve texture addressing behavior for out-of-range data (see [**D3DTEXTUREADDRESS**](/windows/desktop/direct3d9/d3dtextureaddress)) if the data were to be subsequently used for texture sampling. However, new hardware from different manufacturers might not exhibit this behavior and might just chop data to fit the destination register range. Therefore, the safest course of action when using pixel shader version 1\_4 texcrd is to supply texture coordinate data only into the pixel shader that is already within the range \[-8,8\] so that you do not rely on the way hardware clamps.

Unlike texcoord\_, texcrd does not clamp values between 0 and 1.

Rules for using texcrd :

1.  The same .xyz or .xyw modifier must be applied to every read of an individual t(n) register within a texcrd or texld instruction.
2.  The fourth channel result of texcrd is unset/undefined in all cases.
3.  The third channel is unset/undefined for the xyw\_dw case.

## Examples

The complete set of allowed syntax for texcrd, taking into account all valid source modifier/selector and destination write mask combinations, is shown below. Note that the .rgba and .xyzw notation can be used interchangeably.

Copies first three channels of texture coordinate iterator register, t(n), into r(m). The fourth channel of r(m) is uninitialized.


```
texcrd  r(m).rgb, t(n).xyz  

// Produces the same result as the previous instruction
texcrd  r(m).rgb, t(n)
```



Puts first, second, and fourth components of t(n) into first three channels of r(m). The fourth channel of r(m) is uninitialized.


```
texcrd  r(m).rgb, t(n).xyw
```



Here is a projective divide example using the \_dw modifier.

This example copies x/w and y/w from t(n) into the first two channels of r(m). The third and fourth channels of r(m) are uninitialized. Any data previously written to the third channel of r(m) will be lost. Data in the fourth channel of r(m) is lost due to the phase marker. For version 1\_4, the D3DTTFF\_PROJECTED flag is ignored.


```
texcrd  r(m).rg,  t(n)_dw.xyw
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 