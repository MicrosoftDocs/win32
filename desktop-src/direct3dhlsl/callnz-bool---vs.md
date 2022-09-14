---
title: callnz bool - vs
description: Call if not zero. Performs a conditional call to the instruction marked by the label index. | callnz bool - vs
ms.assetid: 9be030b9-fa21-459f-bd6c-f34ad6f177fc
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# callnz bool - vs

Call if not zero. Performs a conditional call to the instruction marked by the label index.

## Syntax



| callnz l\#, \[!\]b\# |
|----------------------|



 

where:

-   where l\# is a [label - vs](label---vs.md) marking the beginning of the subroutine to be called.
-   \[!\] is the optional boolean NOT modifier.
-   b\# identifies a [Constant Boolean Register](dx9-graphics-reference-asm-vs-registers-constant-boolean.md).

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| callnz bool            |      | x    | x    | x     | x    | x     |



 

This instruction does the following:


```
if (specified boolean register is not zero)
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

 

 




