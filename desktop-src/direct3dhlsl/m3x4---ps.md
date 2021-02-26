---
title: m3x4 - ps
description: Multiplies a 3-component vector by a 3x4 matrix. | m3x4 - ps
ms.assetid: b749d3cd-2acf-450c-94f2-fea5e1c8f4d2
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# m3x4 - ps

Multiplies a 3-component vector by a 3x4 matrix.

## Syntax



| m3x4 dst, src0, src1 |
|----------------------|



 

where

-   dst is the destination register. Result is a 4-component vector.
-   src0 is a source register representing a 3-component vector.
-   src1 is a source register representing a 3x4 matrix, which corresponds to the first of 4 consecutive registers.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| m3x4                  |      |      |      |      | x    | x    | x     | x    | x     |



 

The xyzw (default) mask is required for the destination register. Negate and swizzle modifiers are allowed for src0 but not for src1.

The following code snippet shows the operations performed.


```
 
dest.x = (src0.x*src1.x) + (src0.y*src1.y) + (src0.z*src1.z);
dest.y = (src0.x*src2.x) + (src0.y*src2.y) + (src0.z*src2.z);
dest.z = (src0.x*src3.x) + (src0.y*src3.y) + (src0.z*src3.z);
dest.w = (src0.x*src4.x) + (src0.y*src4.y) + (src0.z*src4.z);
```



The input vector is in register src0. The input 3x4 matrix is in register src1, and the next two higher registers, as shown in the expansion below.

This operation is commonly used for transforming a position vector by a matrix that has a projective effect but applies no translation. This instruction is implemented as a pair of dot products as shown here.


```
m3x4   r0.xyzw, r1, c0   will be expanded to: 

dp3 r0.x, r1, c0
dp3 r0.y, r1, c1
dp3 r0.z, r1, c2
dp3 r0.w, r1, c3
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




