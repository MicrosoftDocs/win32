---
title: crs - vs
description: Computes a cross product using the right-hand rule. | crs - vs
ms.assetid: 102108f5-acc8-49ce-a84b-b8060decbaa7
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# crs - vs

Computes a cross product using the right-hand rule.

## Syntax



| crs dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| crs                    |      | x    | x    | x     | x    | x     |



 

This instruction works as shown here.


```
dest.x = src0.y * src1.z - src0.z * src1.y;
dest.y = src0.z * src1.x - src0.x * src1.z;
dest.z = src0.x * src1.y - src0.y * src1.x;
```



Some restrictions on use:

-   src0 cannot be the same register as dest.
-   src1 cannot be the same register as dest.
-   src0 cannot have any swizzle other than the default swizzle (.xyzw).
-   src1 cannot have any swizzle other than the default swizzle (.xyzw).
-   dest has to have exactly one of the following seven masks: .x \| .y \| .z \| .xy \| .xz \| .yz \| .xyz.
-   dest must be a temporary register.
-   dest must not be the same register as src0 or src1

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




