---
title: cmp - ps
description: Choose src1 if src0 0. Otherwise, choose src2. The comparison is done per channel.
ms.assetid: 8fabd548-3f5e-4b78-bf1e-16e4f1548ccd
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# cmp - ps

Choose src1 if src0 >= 0. Otherwise, choose src2. The comparison is done per channel.

## Syntax



| cmp dst, src0, src1, src2 |
|---------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.
-   src2 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| cmp                   |      | x    | x    | x    | x    | x    | x     | x    | x     |



 

There are a few additional limitations for versions 1\_2 and 1\_3:

-   Each shader can use up to a maximum of three cmp instructions.
-   The destination register cannot be the same as any of the source registers.

This example does a four-channel comparison.


```
ps_1_4
def c0, -0.6, 0.6, 0, 0.6
def c1  0,0,0,0
def c2  1,1,1,1

mov r1, c1
mov r2, c2

cmp r0, c0, r1, r2   // r0 is assigned 1,0,0,0 based on the following:

// r0.x = c2.x because c0.x < 0
// r0.y = c1.y because c0.y >= 0
// r0.z = c1.z because c0.z >= 0
// r0.w = c1.w because c0.w >= 0
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




