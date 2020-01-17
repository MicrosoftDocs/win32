---
title: mova - vs
description: Move data from a floating point register to the Address Register, a0.
ms.assetid: 929a0670-f337-4d6d-a7e7-d285e7dc8ae1
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# mova - vs

Move data from a floating point register to the [Address Register](dx9-graphics-reference-asm-vs-registers-address.md), a0.

## Syntax



| mova dst, src |
|---------------|



 

where

-   dst must be the [Address Register](dx9-graphics-reference-asm-vs-registers-address.md), a0.
-   src is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| mova                   |      | x    | x    | x     | x    | x     |



 

Moves floating point data to an integer register. The values are converted from floating point using rounding to nearest.

The address register is the only destination register allowed.

The following code fragment shows the operations performed.


```
if(dest is an integer register)
{
    int intSrc = RoundToNearest(src);
    dest = intSrc;
}
else
{
    dest = src;
}
```



For versions 2\_x and above, the address register is a component vector. Therefore, any write mask is allowed.


```
mova a0.xz, r0
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




