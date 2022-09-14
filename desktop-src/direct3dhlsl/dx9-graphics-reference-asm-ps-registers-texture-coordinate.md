---
title: Texture coordinate register (HLSL PS reference)
description: Pixel shader input register containing texture coordinates.
ms.assetid: 423f249d-fa9f-41f2-adbf-d97ceace06f5
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Texture coordinate register (HLSL PS reference)

Pixel shader input register containing texture coordinates.



| Pixel shader versions       | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------------|------|------|------|------|------|-------|------|------|-------|
| Texture Coordinate Register |      |      |      |      | x    | x     | x    | x    | x     |



 

A texture coordinate register contains texture coordinate data. Before a texture coordinate register is used, it must be declared by a pixel shader declaration. For details about how to declare a texture register, see [dcl - (sm2, sm3 - ps asm)](dcl---ps.md).

In addition, here are some other properties of texture coordinate registers.

-   There are eight pixel-shader texture coordinate registers, t0 to t7.
-   These are read-only registers.
-   They contain four-component RGBA values iterated from input vertices.
-   They contain high precision, high dynamic range data values interpolated from the vertex data. Values are generated with perspective-correct interpolation. Data is floating-point precision, and is signed.
-   There is a maximum of one in a single instruction.
-   Multiple reads of a texture coordinate register within a shader must use identical [Destination Register Write Mask](dx9-graphics-reference-asm-ps-registers-modifiers-write-mask.md).
-   The optional partial precision modifier \[\_pp\] applies to dependent reads. This is because partial precision affects arithmetic operations involving the texture coordinate register. It will not affect the precision of texture address instructions because it does not affect the texture coordinate iterators.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 




