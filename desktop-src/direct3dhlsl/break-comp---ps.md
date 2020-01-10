---
title: break_comp - ps
description: Break out of the current loop at the nearest endloop - ps or endrep - ps, based on a per-component comparison.
ms.assetid: d21e850f-05db-4a29-b15b-85bb1c1410d0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# break\_comp - ps

Break out of the current loop at the nearest [endloop - ps](endloop---ps.md) or [endrep - ps](endrep---ps.md), based on a per-component comparison.

## Syntax



| break\_comp src0, src1 |
|------------------------|



 

Where:

-   \_comp is a scalar (or single) comparison between the two source registers. It can be one of the following: 

    | Syntax | Comparison            |
    |--------|-----------------------|
    | \_gt   | Greater than          |
    | \_lt   | Less than             |
    | \_ge   | Greater than or equal |
    | \_le   | Less than or equal    |
    | \_eq   | Equal to              |
    | \_ne   | Not equal to          |

    

     

-   src0 is a source register. Replicate swizzle is required if selecting a single component.
-   src1 is a source register. Replicate swizzle is required if selecting a single component.

## Remarks

This instruction is supported in the following versions.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| break\_comp           |      |      |      |      |      | x    | x     | x    | x     |



 

When the comparison is true, it breaks out of the current loop, as shown.


```
if (!(src0 comparison src1))
   jump to the corresponding endloop or endrep instruction;
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




