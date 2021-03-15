---
title: dst - vs
description: Calculates a distance vector. | dst - vs
ms.assetid: 4315a29f-58e7-427f-aaa0-1fe1a81eb392
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dst - vs

Calculates a distance vector.

## Syntax



| dst dest, src0, src1 |
|----------------------|



 

where

-   dest is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| dst                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows the operations performed:


```
dest.x = 1;
dest.y = src0.y * src1.y;
dest.z = src0.z;
dest.w = src1.w;
```



The first source operand (src0) is assumed to be the vector (ignored, d\*d, d\*d, ignored) and the second source operand (src1) is assumed to be the vector (ignored, 1/d, ignored, 1/d). The destination (dest) is the result vector (1, d, d\*d, 1/d).

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




