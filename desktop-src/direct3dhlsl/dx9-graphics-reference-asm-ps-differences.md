---
title: Pixel Shader Differences
description: Pixel Shader Differences
ms.assetid: 11aefb26-eb82-486c-81ff-7c0cfbab1b7a
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Pixel Shader Differences

## Instruction Slots

Each version supports a different number of maximum instruction slots.



| Version  | Maximum number of instruction slots                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------|
| ps\_1\_1 | 4 texture + 8 arithmetic                                                                                              |
| ps\_1\_2 | 4 texture + 8 arithmetic                                                                                              |
| ps\_1\_3 | 4 texture + 8 arithmetic                                                                                              |
| ps\_1\_4 | 6 texture + 8 arithmetic per phase                                                                                    |
| ps\_2\_0 | 32 texture + 64 arithmetic                                                                                            |
| ps\_2\_x | 96 minimum, and up to the number of slots in D3DCAPS9.D3DPSHADERCAPS2\_0.NumInstructionSlots. See D3DPSHADERCAPS2\_0. |
| ps\_3\_0 | 512 minimum, and up to the number of slots in D3DCAPS9.MaxPixelShader30InstructionSlots. See D3DPSHADERCAPS2\_0.      |



 

For information about the limitations of software shaders, see [Software Shaders](dx9-graphics-reference-asm-software-shaders.md).

## Flow Control Nesting Limits

-   See [Flow Control Limitations](dx9-graphics-reference-asm-ps-instructions-flow-control.md).

## ps\_1\_x Features

New instructions:

See [ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-1-x.md).

New registers:

See [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## ps\_2\_0 Features

New features:

-   Three new swizzles - .yzxw, .zxyw, .wzyx
-   Number of [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) increased to 12
-   Number of [Constant Float Register](dx9-graphics-reference-asm-ps-registers-constant-float.md) registers (c\#) increased to 32
-   Number of [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md)s (t\#) increased to 8

New instructions:

-   Setup instructions - [dcl - (sm2, sm3 - ps asm)](dcl---ps.md), [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md)
-   Arithmetic instructions - [abs - ps](abs---ps.md), [crs - ps](crs---ps.md), [dp2add - ps](dp2add---ps.md), [exp - ps](exp---ps.md), [frc - ps](frc---ps.md), [log - ps](log---ps.md), [m3x2 - ps](m3x2---ps.md), [m3x3 - ps](m3x3---ps.md), [m3x4 - ps](m3x4---ps.md), [m4x3 - ps](m4x3---ps.md), [m4x4 - ps](m4x4---ps.md), [max - ps](max---ps.md), [min - ps](min---ps.md), [nrm - ps](nrm---ps.md), [pow - ps](pow---ps.md), [rcp - ps](rcp---ps.md), [rsq - ps](rsq---ps.md), [sincos - ps](sincos---ps.md)
-   Texture instructions - [texld - ps\_2\_0 and up](texld---ps-2-0.md) (different syntax), [texldb - ps](texldb---ps.md), [texldp - ps](texldp---ps.md)

New registers:

-   [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#)

## ps\_2\_x Features

New features (See [**D3DPSHADERCAPS2\_0**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dpshadercaps2_0).):

-   Dynamic flow control
-   Static flow control
-   Nesting for dynamic and static flow control instructions
-   Number of [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md)s (r\#) increased
-   Arbitrary source swizzle
-   Gradient instructions
-   Predication
-   No dependent texture read limit
-   No texture instruction limit

New instructions:

-   Static flow control instructions - [if bool - ps](if-bool---ps.md), [call - ps](call---ps.md), [callnz bool - ps](callnz-bool---ps.md), [else - ps](else---ps.md), [endif - ps](endif---ps.md), [rep - ps](rep---ps.md), [endrep - ps](endrep---ps.md), [label - ps](label---ps.md), [ret - ps](ret---ps.md)
-   Dynamic flow control instructions - [break - ps](break---ps.md), [break\_comp - ps](break-comp---ps.md), [breakp - ps](break-p---ps.md), [callnz pred - ps](callnz-pred---ps.md), [if\_comp - ps](if-comp---ps.md), [if pred - ps](if-pred---ps.md), [setp\_comp - ps](setp-comp---ps.md)
-   Arithmetic instructions - [dsx - ps](dsx---ps.md), [dsy - ps](dsy---ps.md)
-   Texture instruction - [texldd - ps](texldd---ps.md)

New registers:

-   [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md) (p0)

## ps\_3\_0 Features

New features:

-   Consolidated 10 [Input Register](dx9-graphics-reference-asm-ps-registers-ps-3-0.md)s (v\#)
-   Indexable [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md) (v\#) with the [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) (aL)
-   Number of [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md)s (r\#) increased to 32
-   Number of [Constant Float Register](dx9-graphics-reference-asm-ps-registers-constant-float.md)s (c\#) increased to 224

New instructions:

-   Setup instruction - [dcl\_semantics (sm3 - ps asm)](dcl-usage---ps.md)
-   Static flow instructions - [loop - ps](loop---ps.md), [endloop - ps](endloop---ps.md)
-   Arithmetic instruction - [sincos - ps](sincos---ps.md) (new syntax)
-   Texture instruction - [texldl - ps](texldl---ps.md)

New registers:

-   [Input Register](dx9-graphics-reference-asm-ps-registers-ps-3-0.md) (v\#)
-   [Position Register](dx9-graphics-reference-asm-ps-registers-ps-3-0.md) (vPos)
-   [Face Register](dx9-graphics-reference-asm-ps-registers-ps-3-0.md) (vFace)

## Related topics

<dl> <dt>

[Pixel Shaders](dx9-graphics-reference-asm-ps.md)
</dt> </dl>

 

 