---
title: abs - vs
description: Computes absolute value.
ms.assetid: d3b4cf06-dc87-4c71-aa2d-5ade4cf98caa
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# abs - vs

Computes absolute value.

## Syntax



|              |
|--------------|
| abs dst, src |



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



|                        |      |      |      |       |      |       |
|------------------------|------|------|------|-------|------|-------|
| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
| abs                    |      | x    | x    | x     | x    | x     |



 

This instruction works as shown here.


```
dest.x = abs(src.x)
dest.y = abs(src.y)
dest.z = abs(src.z)
dest.w = abs(src.w)
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




