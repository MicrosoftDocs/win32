---
title: pow - vs
description: Full precision abs(src0)src1. | pow - vs
ms.assetid: 51da86c6-bafa-42e0-90a5-d1545e39e600
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# pow - vs

Full precision abs(src0)<sup>src1</sup>.

## Syntax



| pow dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is an input source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.
-   src1 is an input source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| pow                    |      | x    | x    | x     | x    | x     |



 

This instruction works as shown here.


```
dest = pow(abs(src0), src1);
```



This is a scalar instruction, therefore the source registers should have replicate swizzles to indicate which channels are used.

The scalar result is replicated to all four output channels.

This instruction could be expanded as exp(src1 \* log(src0)).

Precision is not lower than 15 bits.

The dest register should be a temporary register, and should not be the same register as src1.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




