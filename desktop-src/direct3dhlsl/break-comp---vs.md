---
title: break_comp - vs
description: Conditionally break out of the current loop at the nearest endloop - vs or endrep - vs.
ms.assetid: 01745e03-874a-4594-b6ab-12db22d0cb4a
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# break\_comp - vs

Conditionally break out of the current loop at the nearest [endloop - vs](endloop---vs.md) or [endrep - vs](endrep---vs.md).

## Syntax



| break\_comp src0, src1 |
|------------------------|



 

Where:

-   \_comp is a comparison between the two source registers. It can be one of the following: 

    | Syntax | Comparison            |
    |--------|-----------------------|
    | \_gt   | Greater than          |
    | \_lt   | Less than             |
    | \_ge   | Greater than or equal |
    | \_le   | Less than or equal    |
    | \_eq   | Equal to              |
    | \_ne   | Not equal to          |

    

     

-   src0 is a source register. Replicate swizzle is required to select a single component.
-   src1 is a source register. Replicate swizzle is required to select a single component.

## Remarks

This instruction is supported in the following versions.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| break\_comp            |      |      | x    | x     | x    | x     |



 

When the comparison is true, it breaks out of the current loop, as shown.


```
if (src0 comparison src1)
   jump to the corresponding endloop or endrep instruction;
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




