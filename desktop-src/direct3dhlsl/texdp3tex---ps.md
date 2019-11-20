---
title: texdp3tex - ps
description: Performs a three-component dot product and uses the result to do a 1D texture lookup.
ms.assetid: 'vs|directx_sdk|~\texdp3tex___ps.htm'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texdp3tex - ps

Performs a three-component dot product and uses the result to do a 1D texture lookup.

## Syntax



| texdp3tex dst, src |
|--------------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texdp3tex             |      | x    | x    |      |      |      |       |      |       |



 

Texture registers must use the following sequence.


```
 
tex       t(n)        // Define tn as a standard 3-vector (tn must be 
                      // defined in some way before texdp3tex uses it)
texdp3tex t(m), t(n)  // where m > n                 
                      // Perform a three-component dot product between t(n) and 
                      // the texture coordinate set m. Use the scalar result to
                      // do a 1D texture lookup at texturestage m and place
                      // the result in t(m)
```



Here is more detail about how the dot product and texture lookup are done.

The texdp3tex instruction performs a three-component dot product.

u' = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

The result is used to sample the texture at texture stage m by performing a 1D lookup.

t(m)<sub>RGBA</sub> = TextureSample(stage m)<sub>RGBA</sub> using (u',0,0) as coordinates

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




