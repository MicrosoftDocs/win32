---
title: breakp - ps
description: Conditionally break out of the current loop at the nearest endloop - ps or endrep - ps. Use one of the components of the predicate register as a condition to determine whether or not to perform the instruction.
ms.assetid: be219239-fccb-4561-8b71-083c47ba915b
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# breakp - ps

Conditionally break out of the current loop at the nearest [endloop - ps](endloop---ps.md) or [endrep - ps](endrep---ps.md). Use one of the components of the predicate register as a condition to determine whether or not to perform the instruction.

## Syntax



| breakp \[!\]p0.{x\|y\|z\|w} |
|-----------------------------|



 

Where:

-   \[!\] is an optional negate modifier.
-   p0 is the [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md).
-   {x\|y\|z\|w} is the required replicate swizzle on p0.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| breakp                |      |      |      |      |      | x    | x     | x    | x     |



 

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




