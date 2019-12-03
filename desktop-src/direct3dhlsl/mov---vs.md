---
title: mov - vs
description: Move floating-point data between registers.
ms.assetid: bf013ab2-593e-4201-ba75-faebd0c9f97a
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# mov - vs

Move floating-point data between registers.

## Syntax



| mov dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| mov                    | x    | x    | x    | x     | x    | x     |



 

Can be used for floating point data. For version vs\_1\_1, it can also be used to write the address register. When used to update address registers, the values are converted from floating point using rounding to nearest.

The following code fragment shows the operations performed.


```
if(dest is an integer register)
{
    int intSrc = RoundToNearest(src.w);
    dest = intSrc;
}
else
{
    dest = src;
}
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




