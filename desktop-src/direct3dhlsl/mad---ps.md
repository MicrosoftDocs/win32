---
title: mad - ps
description: Multiply and add instruction. Sets the destination register to (src0 \ src1) + src2.
ms.assetid: 0bcf5dcc-3657-4ee0-9aeb-bd2d8feea7a6
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# mad - ps

Multiply and add instruction. Sets the destination register to (src0 \* src1) + src2.

## Syntax



| mad dst, src0, src1, src2 |
|---------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.
-   src2 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| mad                   | x    | x    | x    | x    | x    | x    | x     | x    | x     |



 

The following code snippet shows the operations performed.


```
dest.x = src0.x * src1.x + src2.x;
dest.y = src0.y * src1.y + src2.y;
dest.z = src0.z * src1.z + src2.z;
dest.w = src0.w * src1.w + src2.w;
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




