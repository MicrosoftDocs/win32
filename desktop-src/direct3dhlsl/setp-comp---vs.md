---
title: setp_comp - vs
description: Set the predicate register. | setp_comp - vs
ms.assetid: bfead3f8-f7fe-4fc1-939f-8e5fbc3e0adf
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# setp\_comp - vs

Set the predicate register.

## Syntax



| setp\_comp dst, src0, src1 |
|----------------------------|



 

Where:

-   \_comp is a per-channel comparison between the two source registers. It can be one of the following: 

    | Syntax | Comparison            |
    |--------|-----------------------|
    | \_gt   | Greater than          |
    | \_lt   | Less than             |
    | \_ge   | Greater than or equal |
    | \_le   | Less than or equal    |
    | \_eq   | Equal to              |
    | \_ne   | Not equal to          |

    

     

-   dst is the [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md) register, p0.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| setp\_comp             |      |      | x    | x     | x    | x     |



 

This instruction operates as:


```
per channel in destination write mask
{
  dst.channel = src0.channel cmp src1.channel
}
```



For each channel that can be written according to the destination write mask, save the boolean result of the comparison operation between the corresponding channels of src0 and src1 (after the source modifier swizzles have been resolved).

Source registers allow arbitrary component swizzles to be specified.

The destination register allows arbitrary write masks.

The dest register must be the predicate register.

## Applying the Predicate Register

Once the predicate register has been initialized with setp, it can be used to control an instruction per component. Here's the syntax:


```
([!]p0[.swizzle]) instruction dest, srcReg, ...
```



Where:

-   \[!\] is an optional boolean NOT
-   p0 is the predicate register
-   \[.swizzle\] is an optional swizzle to apply to the contents of the predicate register before using it to mask the instruction. The available swizzles are: .xyzw (default when none specified), or any replicate swizzle: .x/.r, .y/.g, .z/.b or .a/.w.
-   instruction is any aritmetic, or texture instruction. This cannot be a static or dynamic flow control instruction.
-   dest, srcReg, ... are the registers required by the instruction

Assuming the predicate register has been set up with (true, true, false, false) component values, it can be applied to this instruction:


```
// given r0 = 0,0,1,1
// given r1 = 1,1,0,0
setp_le p0, r0, r1
(p0) add r2, r3, r4
```



to perform a 2 component add.


```
r2.x = r3.x + r4.x
r2.y = r3.y + r4.y
```



The x and y components of r2 will not be written since the predicate register contained false in components z and w.

Applying the predicate register to an arithmetic or texture instruction increases its instruction slot count by 1.

The predicate register can also be applied to [if pred - vs](if-pred---vs.md), [callnz pred - vs](callnz-pred---vs.md) and [breakp - vs](breakp---vs.md) instructions. These flow control instructions do not have any increase in the instruction slot count when using the predicate register.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




