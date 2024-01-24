---
title: callnz bool - ps
description: Call if not zero. Performs a conditional call to the instruction marked by the label index. | callnz bool - ps
ms.assetid: 1b9ff276-c2b8-46cc-96ac-a5b5455c5cc0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# callnz bool - ps

Call if not zero. Performs a conditional call to the instruction marked by the label index.

## Syntax



| callnz l\#, \[!\]b\# |
|----------------------|



 

Where:

-   l\# is a [label - ps](label---ps.md) marking the beginning of the subroutine to be called.
-   \[!\] is an optional negate modifier.
-   b\# identifies a [Constant Boolean Register](dx9-graphics-reference-asm-ps-registers-constant-boolean.md).

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| callnz bool           |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction does the following:


```
if (specified Boolean register is not zero)
{
    Push address of the next instruction to the return address stack
    Continue execution from the instruction marked by the label
}
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




