---
title: dcl_semantics (sm3 - ps asm)
description: Declare the association between vertex shader output and pixel shader input.
ms.assetid: 4f4dc6fe-0efa-4d84-aefd-583e90ab9a61
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_semantics (sm3 - ps asm)

Declare the association between vertex shader output and pixel shader input.

## Syntax



|                                                   |
|---------------------------------------------------|
| dcl\_semantics \[\_centroid\] dst\[.write\_mask\] |



 

Where:

-   \_semantics: Identifies the intended data usage, and may be any of the values in [**D3DDECLUSAGE**](/windows/desktop/direct3d9/d3ddeclusage) (without the D3DDECLUSAGE\_ prefix). Additionally, an integer index can be appended to the semantic to distinguish parameters that use similar semantics.
-   \[\_[Centroid](dx9-graphics-reference-asm-ps-instructions-modifiers-ps-2-0.md)\] is an optional instruction modifier. It is is supported on dcl\_usage instructions that declare the input registers and on texture lookup instructions. The centroid is appended with no space.
-   dst: destination register. See [ps\_3\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md).
-   write\_mask: The same output register may be declared multiple times, each time with a unique write mask (so different semantics can be applied to individual components). However, the same semantic cannot be used multiple times in a declaration. This means that vectors must be four components or less, and cannot go across four-component register boundaries (individual output registers). When the \_psize semantic is used, it should have a full write mask because it is considered a scalar. When the \_position semantic is used, it should have full write mask because all four components have to be written.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dcl\_usage            |      |      |      |      |      |      |       | x    | x     |



 

All dcl\_usage instructions must appear before the first executable instruction.

## Declaration Examples


```
ps_3_0

; Declaring inputs
dcl_normal      v0.xyz
dcl_blendweight v0.w ; Must be same reg# as normal, matching vshader packing
dcl_texcoord1   v1.y ; Mask can be any subset of mask from vshader semantic
dcl_texcoord0   v1.zw; Has to be same reg# as texcoord1, to match vshader

; Declaring samplers
dcl_2d s0
dcl_2d s1

def c0, 0, 0, 0, 0

mov r0.x, v1.y ; texcoord1
mov r0.y, c0
texld r0, r0, s0

texld r1, v1.zw, s1
...
(output regs in ps_3_0 are same as ps_2_0: oC0-oC3, oDepth)
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> <dt>

[Antialias Sample](https://msdn.microsoft.com/library/Ee415231(v=VS.85).aspx)
</dt> </dl>

 

 
