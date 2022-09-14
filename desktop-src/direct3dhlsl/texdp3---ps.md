---
title: texdp3 - ps
description: Performs a three-component dot product between data in the texture register number and the texture coordinate set corresponding to the destination register number.
ms.assetid: 82e02f3f-4b88-4007-b4be-0c66223d9c66
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texdp3 - ps

Performs a three-component dot product between data in the texture register number and the texture coordinate set corresponding to the destination register number.

## Syntax



| texdp3 dst, src |
|-----------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texdp3                |      | x    | x    |      |      |      |       |      |       |



 

Texture registers must use the following sequence.


```
 
tex    t(n)        // Define tn as a standard 3-vector (tn must be 
                   //   defined in some way before texdp3 uses it)
texdp3 t(m), t(n)  // where m > n
                   // Perform a three-component dot product between tn and 
                   //   the texture coordinate set m. The scalar result is
                   //   replicated to all components of t(m)
```



Here is more detail about how the dot product is accomplished.

The texdp3 instruction performs a three-component dot product and replicates it to all four color channels.

t(m)<sub>RGBA</sub> = TextureCoordinates(stage m)<sub>UVW</sub> \* t(n)<sub>RGB</sub>

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




