---
title: Input Color Register
description: Pixel shader input register containing vertex color.
ms.assetid: d2e21f87-000e-410a-aaba-172000ed1c5f
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Input Color Register

Pixel shader input register containing vertex color.

## Syntax


```
dcl v#.writeMask
```



where:

-   [dcl - (sm2, sm3 - ps asm)](dcl---ps.md) is a register declaration instruction.
-   v is an input register and \# is the register number. The number of registers allowed is determined by the shader version.
-   writeMask determines which components (up to four) are written. Valid components are: (x,y,z,w) or (r,g,b,a).

## Remarks

Color registers are read-only registers. Each register contains four-component RGBA values iterated from input vertices. They have lower precision than most registers, guaranteed to have 8 bits of unsigned data in the range (0, +1). You cannot use more than one in a single instruction.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> <dt>

[ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md)
</dt> <dt>

[ps\_2\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-2-0.md)
</dt> <dt>

[ps\_2\_x Registers](dx9-graphics-reference-asm-ps-registers-ps-2-x.md)
</dt> <dt>

[ps\_3\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md)
</dt> </dl>

 

 




