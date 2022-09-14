---
title: bem - ps
description: Apply a fake bump environment-map transform.
ms.assetid: b41009d4-a2bb-4397-ad23-c95ef2620a66
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# bem - ps

Apply a fake bump environment-map transform.

## Syntax



| bem dst.rg, src0, src1 |
|------------------------|



 

where

-   dst.rg dst is the destination register. The red and green component write mask must be used.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| bem                   |      |      |      | x    |      |      |       |      |       |



 

This instruction performs the following calculation.


```
(Given n == dest register #)
dest.r = src0.r + D3DTSS_BUMPENVMAT00(stage n) * src1.r 
                + D3DTSS_BUMPENVMAT10(stage n) * src1.g

dest.g = src0.g + D3DTSS_BUMPENVMAT01(stage n) * src1.r
                + D3DTSS_BUMPENVMAT11(stage n) * src1.g
```



Rules for using bem:

1.  bem must appear in the first phase of a shader (that is, before a phase marker).
2.  bem consumes two arithmetic instruction slots.
3.  Only one use of this instruction is allowed per shader.
4.  Destination writemask must be .rg /.xy.
5.  This instruction cannot be co-issued.
6.  Aside from the restriction that destination write mask be .rg, modifiers on source src0, src1, and instruction modifiers are unconstrained.

## Instruction Information



| Requirement                         | Value           |
|--------------------------|------------|
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




