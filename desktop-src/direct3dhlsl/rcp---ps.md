---
title: rcp - ps
description: Computes the reciprocal of the source scalar. | rcp - ps
ms.assetid: d8dfc2b3-4404-47ec-aeaf-1adb7e7a342e
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# rcp - ps

Computes the reciprocal of the source scalar.

## Syntax



| rcp dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| rcp                   |      |      |      |      | x    | x    | x     | x    | x     |



 

The output must be exactly 1.0 if the input is exactly 1.0. A source of 0.0 yields infinity.

The scalar result is replicated to all channels in the destination write mask.

Precision should be at least 1.0/(2²²) absolute error over the range (1.0, 2.0) because common implementations will separate mantissa and exponent.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




