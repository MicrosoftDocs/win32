---
title: if bool - ps
description: Start of an if block.
ms.assetid: cff53072-1c73-4cf8-9ecd-11032a9c4bbb
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# if bool - ps

Start of an if block.

## Syntax



| if bool |
|---------|



 

Where:

-   bool is a bool (Boolean) register number. See [Constant Boolean Register](dx9-graphics-reference-asm-ps-registers-constant-boolean.md).

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| if bool               |      |      |      |      |      | x    | x     | x    | x     |



 

If the source Boolean register in the if statement is true, the code enclosed by the if statement and the matching [endif - ps](endif---ps.md) or [else - ps](else---ps.md) is executed. Otherwise, the code enclosed by the else - ps...endif - ps statements is executed. This instruction consumes one instruction slot.

An if block can be nested.

An if block cannot straddle a loop block.

An if block can be followed by a statement block, and/or an [else - ps](else---ps.md) instruction, and/or an [endif - ps](endif---ps.md) instruction.

## Example

This instruction provides conditional static flow control.


```
defb b3, true

if b3
// Instructions to run if b3 is nonzero
else
// Instructions to run otherwise
endif
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> <dt>

[else - ps](else---ps.md)
</dt> <dt>

[endif - ps](endif---ps.md)
</dt> </dl>

 

 




