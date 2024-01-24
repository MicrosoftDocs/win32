---
title: dp4 - ps
description: Computes the four-component dot product of the source registers. | dp4 - ps
ms.assetid: 83ef6097-cacf-4498-842b-3eb03e57bd6f
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dp4 - ps

Computes the four-component dot product of the source registers.

## Syntax



| dp4 dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dp4                   |      | x    | x    | x    | x    | x    | x     | x    | x     |



 

The following code snippet shows the operations performed:


```
dest.x = dest.y = dest.z = dest.w = 
    (src0.x * src1.x) + (src0.y * src1.y) + 
    (src0.z * src1.z) + (src0.w * src1.w);
```



Limitations for ps\_1\_2 and ps\_1\_3:

-   Each shader can use up to a maximum of four dp4 instructions.
-   Each dp4 instruction counts as two arithmetic instructions.

Limitations for 1\_X versions:

-   This instruction cannot be co-issued because dp4 runs in both the vector and alpha pipeline.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




