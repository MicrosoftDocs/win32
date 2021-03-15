---
title: frc - ps
description: Returns the fractional portion of each input component. | frc - ps
ms.assetid: 378bc516-c81e-4538-8d6f-987536b19467
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# frc - ps

Returns the fractional portion of each input component.

## Syntax



| frc dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| frc                   |      |      |      |      | x    | x    | x     | x    | x     |



 

The following code snippet shows conceptually how the instruction operates.


```
dest.x = src.x - (float)floor(src.x);
dest.y = src.y - (float)floor(src.y);
dest.z = src.z - (float)floor(src.z);
dest.w = src.w - (float)floor(src.w);
```



The floor function converts the argument passed in to the greatest integer that is less than (or equal to) the argument. This is converted to a float and then subtracted fom the original value. The resulting fractional value ranges from 0.0 through 1.0.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




