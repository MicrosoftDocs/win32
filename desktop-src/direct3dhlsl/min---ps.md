---
title: min - ps
description: Calculates the minimum of the sources. | min - ps
ms.assetid: 2ee6208d-a353-4747-8037-c21dd1a05016
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# min - ps

Calculates the minimum of the sources.

## Syntax



| min dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| min                   |      |      |      |      | x    | x    | x     | x    | x     |



 

The following code snippet shows the operations performed.


```
dest.x=(src0.x < src1.x) ? src0.x : src1.x;
dest.y=(src0.y < src1.y) ? src0.y : src1.y;
dest.z=(src0.z < src1.z) ? src0.z : src1.z;
dest.w=(src0.w < src1.w) ? src0.w : src1.w;
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




