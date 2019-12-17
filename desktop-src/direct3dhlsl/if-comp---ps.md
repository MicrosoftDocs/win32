---
title: if_comp - ps
description: Start an if bool - ps...else - ps...endif - ps block, with a condition based on values that could be computed in a shader. This instruction is used to skip a block of code, based on a condition.
ms.assetid: a641e347-df28-4a3f-a461-0b6aee758e59
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# if\_comp - ps

Start an [if bool - ps](if-bool---ps.md)...[else - ps](else---ps.md)...[endif - ps](endif---ps.md) block, with a condition based on values that could be computed in a shader. This instruction is used to skip a block of code, based on a condition.

## Syntax



| if\_comp src0, src1 |
|---------------------|



 

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

    

     

-   src0 is a source register. Replicate swizzle is required to select a component.
-   src1 is a source register. Replicate swizzle is required to select a component.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| if\_comp              |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction is used to skip a block of code, based on a condition.


```
if (src0 comparison src1)
   jump to the corresponding else or endif instruction;
```



Be careful using the equals and not equals comparison modes on floating point numbers. Because rounding occurs during during floating point calculations, the comparison can be done against an epsilon value (small nonzero number) to avoid errors.

Restrictions include:

-   if\_comp...[else - ps](else---ps.md)...[endif - ps](endif---ps.md) blocks (along with the predicated [if](if-bool---ps.md) blocks) can be nested up to 24 layers deep.
-   src0 and src1 registers require a replicate swizzle.
-   if\_comp blocks must end with an [else - vs](else---vs.md) or [endif - vs](endif---vs.md) instruction.
-   if\_comp...[else - ps](else---ps.md)...[endif - ps](endif---ps.md) blocks cannot straddle a loop block. The if\_comp block must be completely inside or outside the loop block.

## Example

This instruction provides conditional dynamic flow control.


```
if_lt r3.x, r4.y
// Instructions to run if r3.x < r4.y

else
// Instructions to run otherwise

endif
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




