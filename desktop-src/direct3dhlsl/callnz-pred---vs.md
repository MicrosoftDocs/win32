---
title: callnz pred - vs
description: Call if not zero, with a predicate. Performs a conditional call to the instruction marked by the label index. Predication uses a boolean value to determine whether of not to perform the instruction.
ms.assetid: 3417f3e3-7e73-4131-8069-09c0de1469a7
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# callnz pred - vs

Call if not zero, with a predicate. Performs a conditional call to the instruction marked by the label index. Predication uses a boolean value to determine whether of not to perform the instruction.

## Syntax



| callnz l\#, \[!\]p0.{x\|y\|z\|w} |
|----------------------------------|



 

where:

-   l\# is a [label - vs](label---vs.md) marking the beginning of the subroutine to be called.
-   \[!\] is an optional negate modifier.
-   p0 is the [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md).
-   {x\|y\|z\|w} is the required replicate swizzle on p0.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| callnz pred            |      |      | x    | x     | x    | x     |



 

This instruction does the following:


```
if (specified register component is not zero)
{
    Push address of the next instruction to the return address stack.
    Continue execution from the instruction marked by the label.
}
```



This instruction consumes one vertex shader instruction slot.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




