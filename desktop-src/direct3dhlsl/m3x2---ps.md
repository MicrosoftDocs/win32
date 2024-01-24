---
title: m3x2 - ps
description: Multiplies a 3-component vector by a 3x2 matrix. | m3x2 - ps
ms.assetid: a88e6228-a61a-408c-8d89-a5706dd146d5
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# m3x2 - ps

Multiplies a 3-component vector by a 3x2 matrix.

## Syntax



| m3x2 dst, src0, src1 |
|----------------------|



 

where

-   dst is the destination register. Result is a 2-component vector.
-   src0 is a source register representing a 3-component vector.
-   src1 is a source register representing a 3x2 matrix, which corresponds to the first of 2 consecutive registers.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| m3x2                  |      |      |      |      | x    | x    | x     | x    | x     |



 

The xy mask is required for the destination register. Negate and swizzle modifiers are allowed for src0 but not for src1.

The following equations show how the instruction operates:


```
dest.x = (src0.x*src1.x) + (src0.y*src1.y) + (src0.z*src1.z);
dest.y = (src0.x*src2.x) + (src0.y*src2.y) + (src0.z*src2.z);
```



The input vector is in register src0. The input 3x2 matrix is in register src1 and the next higher register in the same register file, as shown in the following expansion. A 2D result is produced, leaving the other elements of the destination register (dest.z and dest.w) unaffected.

This operation is commonly used for 2D transforms. This instruction is implemented as a pair of dot products as shown here.


```
m3x2   r0.xy, r1, c0   which will be expanded to:

dp3   r0.x, r1, c0
dp3   r0.y, r1, c1
```



Swizzle and negate modifiers are invalid for the src1 register. The dst and src0 register, or any of src1+i registers, cannot be the same.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




