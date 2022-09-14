---
title: mad - vs
description: Multiplies and adds sources.
ms.assetid: 059f0bf6-d143-4efc-b074-0ed026edb008
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# mad - vs

Multiplies and adds sources.

## Syntax



| mad dst, src0, src1, src2 |
|---------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.
-   src2 is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| mad                    | x    | x    | x    | x     | x    | x     |



 

The following code fragment shows the operations performed.


```
dest.x = src0.x * src1.x + src2.x;
dest.y = src0.y * src1.y + src2.y;
dest.z = src0.z * src1.z + src2.z;
dest.w = src0.w * src1.w + src2.w;
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




