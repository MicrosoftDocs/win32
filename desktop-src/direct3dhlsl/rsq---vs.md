---
title: rsq - vs
description: Computes the reciprocal square root (positive only) of the source scalar. | rsq - vs
ms.assetid: 1ac37dad-0cea-41af-8dae-f299896462b1
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# rsq - vs

Computes the reciprocal square root (positive only) of the source scalar.

## Syntax



| rsq dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| rsq                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows the operations performed.


```
float f = abs(src0);
if (f == 0)
    f = FLT_MAX
else
{
    if (f != 1.0)
        f = 1.0/(float)sqrt(f);
}

dest.z = dest.y = dest.z = dest.w = f;
```



The absolute value is taken before processing.

Precision should be at least 1.0/(2²²) absolute error over the range (1.0, 4.0) because common implementations will separate mantissa and exponent.

If source has no subscripts, the x-component is used. The output must be exactly 1.0 if the input is exactly 1.0. A source of 0.0 yields infinity.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




