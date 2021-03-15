---
title: m4x4 - vs
description: Multiplies a 4-component vector by a 4x4 matrix. | m4x4 - vs
ms.assetid: 016100ac-e316-41fd-a606-271be7394a1a
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# m4x4 - vs

Multiplies a 4-component vector by a 4x4 matrix.

## Syntax



| m4x4 dst, src0, src1 |
|----------------------|



 

where

-   dst is the destination register. Result is a 4-component vector.
-   src0 is a source register representing a 4-component vector.
-   src1 is a source register representing a 4x4 matrix, which corresponds to the first of 4 consecutive registers.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| m4x4                   | x    | x    | x    | x     | x    | x     |



 

The xyzw (default) mask is required for the destination register. Negate and swizzle modifiers are allowed for src0, but not for src1.

Swizzle and negate modifiers are invalid for the src0 register. The dest and src0 registers cannot be the same.

The following code fragment shows the operations performed.


```
dest.x = (src0.x * src1.x) + (src0.y * src1.y) + (src0.z * src1.z) + 
        (src0.w * src1.w);
dest.y = (src0.x * src2.x) + (src0.y * src2.y) + (src0.z * src2.z) + 
        (src0.w * src2.w);
dest.z = (src0.x * src3.x) + (src0.y * src3.y) + (src0.z * src3.z) + 
        (src0.w * src3.w);
dest.w = (src0.x * src4.x) + (src0.y * src4.y) + (src0.z * src4.z) + 
        (src0.w * src4.w);
```



The input vector is in register src0. The input 4x4 matrix is in register src1, and the next three higher registers, as shown in the expansion below.

This operation is commonly used for transforming a position by a projection matrix. This instruction is implemented as a series of dot products as shown here.


```
m4x4   r0.xyzw, r1, c0    will be expanded to:

dp4   r0.x, r1, c0
dp4   r0.y, r1, c1
dp4   r0.z, r1, c2
dp4   r0.w, r1, c3
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




