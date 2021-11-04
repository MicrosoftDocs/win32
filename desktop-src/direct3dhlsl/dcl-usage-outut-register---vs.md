---
title: dcl_usage output (sm1, sm2, sm3 - vs asm)
description: The various types of output registers have been collapsed into twelve output registers (two for color, eight for texture, one for position, and one for fog and point size).
ms.assetid: 500ca6b3-0f8a-446e-b1b9-edc51f006ad4
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_usage output (sm1, sm2, sm3 - vs asm)

The various types of output registers have been collapsed into twelve output registers (two for color, eight for texture, one for position, and one for fog and point size). These can be used for anything the user wants to interpolate for the pixel shader: texture coordinates, colors, fog, and so on.

Output registers require declarations that include semantics. For instance, the old position and point size registers are replaced by declaring an output register with a position or point-size semantic.

Of the twelve output registers, any ten (not necessarily o0 to o9) have four components (xyzw), another one must be declared as position (and must also include all four components), and optionally one more can be a scalar point size.

## Syntax

The syntax for declaring output registers is similar to the declarations for the input register:



|                                  |
|----------------------------------|
| dcl\_semantics o\[.write\_mask\] |



 

Where:

-   dcl\_semantics can use the same set of semantics as for the input declaration. Semantic names come from [**D3DDECLUSAGE**](/windows/desktop/direct3d9/d3ddeclusage) (and are paired with an index, such as position3). There always has to be one output register with the positiont0 semantic when not used for processing vertices. The positiont0 semantic and the pointsize0 semantic are the only ones that have meaning beyond simply allowing linkage from vertex to pixel shaders. For shaders with flow control, it is assumed that the worst case output is declared. There are no defaults if a shader does not actually output what it declares it should (due to flow control).
-   o is an output register. See [Output\_Registers](dx9-graphics-reference-asm-vs-registers-vs-3-0.md).
-   write\_mask indicates the same output register that can be declared multiple times (so different semantics can be applied to individual components), each time with a unique write mask. However, the same semantic cannot be used multiple times in a declaration. This means that vectors must be four components or less, and cannot go across four-component register boundaries (individual registers). When the point-size semantic is used, it should have full write mask because it is considered a scalar. When the position semantic is used, it should have a full write mask because all four components have to be written.

## Remarks



| Vertex shader versions | 3\_0 | 3\_sw |
|------------------------|------|-------|
| dcl\_usage             | x    | x     |



 

All [dcl\_usage](dcl-usage-input-register---vs.md) instructions must appear before the first executable instruction.

## Declaration Examples


```
vs_3_0
dcl_color4     o3.x    // color4 is a semantic name.
dcl_texcoord3  o3.yz   // Different semantics can be packed into one register.
dcl_fog        o3.w 
dcl_tangent    o4.xyz
dcl_position   o7.xyzw // position must be declared to some unique register 
                       //   in a vertex shader, with all 4 components.

dcl_psize      o6      // Pointsize cannot have a mask 
                       //   (that is, mask is full .xyzw)
                       // This is an implied scalar register. 
                       // No other semantics can be assigned to any components
                       //   of this register.
                       // If pointsize declaration is not used (typical),
                       //   only 11 "out" registers are available, not 12.
                       // Pixel shaders cannot see this value.

```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 
