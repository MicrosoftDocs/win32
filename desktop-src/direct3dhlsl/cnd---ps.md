---
title: cnd - ps
description: Conditionally chooses between src1 and src2, based on the comparison src0 0.5.
ms.assetid: 7a3b49e9-d146-47dc-99a8-4f336db7d0d5
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# cnd - ps

Conditionally chooses between src1 and src2, based on the comparison src0 > 0.5.

## Syntax



| cnd dst, src0, src1, src2 |
|---------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.
-   src2 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| cnd                   | x    | x    | x    | x    |      |      |       |      |       |



 

For versions 1\_1 to 1\_3, src0 must be r0.a.


```
// Version 1_1 to 1_3
if (r0.a > 0.5)
  dest = src1
else
  dest = src2
```



Version 1\_4 compares each channel separately.


```
for each component in src0
{
   if (src0.component > 0.5)
     dest.component = src1.component
   else
     dest.component = src2.component
}
```



These examples show a four-channel comparison done in a version 1\_4 shader, as well as a single-channel comparison possible in a version 1\_1 shader.


```
ps_1_4
def c0, -0.5, 0.5, 0, 0.6
def c1,  0,0,0,0
def c2,  1,1,1,1

cnd r1, c0, c1, c2   // r0 contains 1,1,1,0 because
// r1.x = c2.x because c0.x <= 0.5
// r1.y = c2.y because c0.y <= 0.5
// r1.z = c2.z because c0.z <= 0.5
// r1.w = c1.w because c0.w >  0.5
```



Version 1\_1 to 1\_3 compares against the replicated alpha channel of r0 only.


```
ps_1_1
def c0, -0.5, 0.5, 0, 0.6
def c1,  0,0,0,0
def c2,  1,1,1,1
mov r0, c0
cnd r1, r0.a, c1, c2   // r1 gets assigned 0,0,0,0 because 
                       // r0.a > 0.5, therefore r1.xyzw = c1.xyzw
```



This example compares two values, A and B. The example assumes A is loaded into v0 and B is loaded into v1. Both A and B must be in the range of -1 to +1, and since the color registers (vₙ) are defined to be between 0 and 1, the restriction happens to be satisfied in this example.


```
ps_1_1                // Version instruction
sub r0, v0, v1_bias   // r0 = A - (B - 0.5)
cnd r0, r0.a, c0, c1  // r0 = ( A > B ? c0 : c1 )

// r0 = c0 if A > B, otherwise, r0 = c1
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




