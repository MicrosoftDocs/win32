---
title: m3x3 - vs
description: Multiplies a 3-component vector by a 3x3 matrix. | m3x3 - vs
ms.assetid: 6a749ed0-097d-4354-bc70-fbcd879eafab
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# m3x3 - vs

Multiplies a 3-component vector by a 3x3 matrix.

## Syntax



| m3x3 dst, src0, src1 |
|----------------------|



 

where

-   dst is the destination register. Result is a 3-component vector.
-   src0 is a source register representing a 3-component vector.
-   src1 is a source register representing a 3x3 matrix, which corresponds to the first of 3 consecutive registers.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| m3x3                   | x    | x    | x    | x     | x    | x     |



 

The xyz mask is required for the destination register. Negate and swizzle modifiers are allowed for src0 but not for src1.

The following code fragment shows the operations performed.


```
dest.x = (src0.x * src1.x) + (src0.y * src1.y) + (src0.z * src1.z);
dest.y = (src0.x * src2.x) + (src0.y * src2.y) + (src0.z * src2.z);
dest.z = (src0.x * src3.x) + (src0.y * src3.y) + (src0.z * src3.z);
```



The input vector is in register src0. The input 3x3 matrix is in register src1, and the next two higher registers, as shown in the expansion below. A 3D result is produced, leaving the other element of the destination register (dest.w) unaffected.

This operation is commonly used for transforming normal vectors during lighting computations. This instruction is implemented as a pair of dot products as shown below.


```
m3x3 r0.xyz, r1, c0  which will be expanded to:

dp3   r0.x, r1, c0
dp3   r0.y, r1, c1
dp3   r0.z, r1, c2
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




