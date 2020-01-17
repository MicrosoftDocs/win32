---
title: callnz pred - ps
description: Call with a predicate, if not zero. Performs a conditional call to the instruction marked by the label index. Predication uses a Boolean value to determine whether of not to perform the instruction.
ms.assetid: 9c839fc7-8b4d-4ca1-b30f-5c3f8fb45eae
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# callnz pred - ps

Call with a predicate, if not zero. Performs a conditional call to the instruction marked by the label index. Predication uses a Boolean value to determine whether of not to perform the instruction.

## Syntax



| callnz l\#, \[!\]p0.{x\|y\|z\|w} |
|----------------------------------|



 

Where:

-   where l\# is a [label - ps](label---ps.md) marking the beginning of the subroutine to be called.
-   \[!\] is an optional negate modifier.
-   p0 is the predicate register. See [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md).
-   {x\|y\|z\|w} is the required replicate swizzle on p0.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| callnz pred           |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction does the following:


```
if (specified register component is not zero)
{
    Push address of the next instruction to the return address stack
    Continue execution from the instruction marked by the label
}
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




