---
title: abs - ps
description: Computes absolute value. | abs - ps
ms.assetid: e97db550-2a03-421a-86f4-a6fc5f8e0bca
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# abs - ps

Computes absolute value.

## Syntax



|              |
|--------------|
| abs dst, src |



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



|                       |      |      |      |      |      |      |       |      |       |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
| abs                   |      |      |      |      | x    | x    | x     | x    | x     |



 

This instruction works as shown here.


```
dest.x = abs(src.x)
dest.y = abs(src.y)
dest.z = abs(src.z)
dest.w = abs(src.w)
```



## Instruction Information



|                          |            |
|--------------------------|------------|
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




