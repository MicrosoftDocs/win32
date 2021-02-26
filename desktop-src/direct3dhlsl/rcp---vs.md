---
title: rcp - vs
description: Computes the reciprocal of the source scalar. | rcp - vs
ms.assetid: be638a42-b693-461d-ab0a-3a6c0fa1acfc
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# rcp - vs

Computes the reciprocal of the source scalar.

## Syntax



| rcp dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| rcp                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows the operations performed.


```
float f = src0;
if(f == 0.0f)
{
    f = FLT_MAX;
}
else 
{
    if(f != 1.0)
    {
        f = 1/f;
    }
}

dest = f;
```



The output must be exactly 1.0 if the input is exactly 1.0. A source of 0.0 yields infinity.

Precision should be at least 1.0/(2²²) absolute error over the range (1.0, 2.0) because common implementations will separate mantissa and exponent.

If the source has no subscripts, the x-component is used.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




