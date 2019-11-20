---
title: dp2add - ps
description: Performs a 2D dot product and a scalar addition.
ms.assetid: 4226ee34-2e68-4536-b171-68f3b967182e
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dp2add - ps

Performs a 2D dot product and a scalar addition.

## Syntax


```
dp2add dst, src0, src1, src2.{x|y|z|w}
```



Where:

-   dst is a destination register.
-   src0, src1, and src2 are three source registers.
-   {x\|y\|z\|w} is the required replicate swizzle on src2.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dp2add                |      |      |      |      | x    | x    | x     | x    | x     |



 

The scalar value for add is chosen by the replicate swizzle on src2.

The following code snippet shows the operations performed.


```
dest = src0.r * src1.r + src0.g * src1.g + src2.replicate_swizzle
// The scalar result is replicated to the write mask components
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




