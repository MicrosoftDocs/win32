---
title: sge - vs
description: Computes the sign if the first source is greater than or equal to the second source.
ms.assetid: 88e8eb68-8189-40c3-b20e-f395576f5f6a
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# sge - vs

Computes the sign if the first source is greater than or equal to the second source.

## Syntax



| sge dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| sge                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows the operations performed.


```
 
dest.x = (src0.x >= src1.x) ? 1.0f : 0.0f;
dest.y = (src0.y >= src1.y) ? 1.0f : 0.0f;
dest.z = (src0.z >= src1.z) ? 1.0f : 0.0f;
dest.w = (src0.w >= src1.w) ? 1.0f : 0.0f;
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




