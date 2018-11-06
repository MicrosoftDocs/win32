---
title: Destination Register Masking
description: Masking specifies which components of the destination register will be updated with the result of an instruction. Texture registers have one set of rules and nontexture registers have another set of rules.
ms.assetid: 989ebe55-1f80-4063-b116-4284520f52cc
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Destination Register Masking

Masking specifies which components of the destination register will be updated with the result of an instruction. Texture registers have one set of rules and nontexture registers have another set of rules.

-   dx9\_graphics\_reference\_asm\_vs\_registers\_modifiers\_masking - This section contains rules for applying masks to destination registers.
-   Texture\_Register\_Masks - Texture registers have some unique rules.

## Destination Register Masking

As shown in the following table, masking (where r is one of the valid vertex shader [Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)) can be applied to the individual components of the vector data.



| Component modifier | Description      |
|--------------------|------------------|
| r.{x}{y}{z}{w}     | Destination mask |



 

-   In general, specifying destination register write masks is good coding style. It makes code easier to read and maintain.
-   Any combination of components may be specified (including none) as long as x precedes y, y precedes z, and z precedes w.
-   The oPts and oFog output registers must use only one mask.
-   Certain instructions require the destination register to use a single write mask: exp, expp, log, logp, pow, rcp, and rsq.
-   In version 1.0, the frc instruction required one of the following mask combinations: .x or .y or .xy. Version 2.0 has no mask restriction.
-   sincos requires one of the following mask combinations: .x or .y or .xyz.
-   m3x2 requires the .xy write mask.
-   m3x3 and m4x3 require the .xyz write mask.
-   m3x4 and m4x4 require either the .xyz write mask or the default write mask (xyzw).

## Texture Register Masks

The validation rules for using modifiers on texture coordinate registers are tighter than the validation rules for other registers.

-   If oTn is written, all previous registers (oTn-1 ~ oT0) have to be written as well.
-   The "combined" write mask for any oT\# register must be exactly one of the following:
    -   .x
    -   .xy
    -   .xyz
    -   .xyzw (which is equivalent to not using any component modifiers)

For example, a vertex shader can output to texture registers in separate instructions.


```
    oT1.y  
    oT0.y  
    oT2  
    oT0.xz  
    oT1.x
```



Or, the instructions can be combined.


```
    oT0.xyz  
    oT1.xy  
    oT2.xyzw    
```



These restrictions apply only to the texture coordinate registers.

## Related topics

<dl> <dt>

[Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md)
</dt> </dl>

 

 




