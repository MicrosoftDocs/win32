---
title: rsq - ps
description: Computes the reciprocal square root (positive only) of the source scalar. | rsq - ps
ms.assetid: deb1bd12-6347-4b1e-b21b-f3ef48da4c13
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# rsq - ps

Computes the reciprocal square root (positive only) of the source scalar.

## Syntax



| rsq dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| rsq                   |      |      |      |      | x    | x    | x     | x    | x     |



 

The absolute value is taken before processing.

Precision should be at least 1.0/(2²²) absolute error over the range (1.0, 4.0) because common implementations will separate mantissa and exponent.

The output must be exactly 1.0 if the input is exactly 1.0. A source of 0.0 yields infinity.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




