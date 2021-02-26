---
title: frc - vs
description: Returns the fractional portion of each input component. | frc - vs
ms.assetid: 6b6a4475-b665-4de0-9423-88ea8103e606
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# frc - vs

Returns the fractional portion of each input component.

## Syntax



| frc dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| frc                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows conceptually how the instruction operates.


```
dest.x = src.x - (float)floor(src.x);
dest.y = src.y - (float)floor(src.y);
dest.z = src.z - (float)floor(src.z);
dest.w = src.w - (float)floor(src.w);
```



The floor function converts the argument passed in to the greatest integer that is less than (or equal to) the argument. This is converted to a float and then subtracted fom the original value. The resulting fractional value ranges from 0.0 through 1.0.

For version 1\_1, the allowable write masks are .y and .xy (.x is not allowed).

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




