---
title: if bool - vs
description: Starts an if...else...endif - vs block.
ms.assetid: d77e2f81-400c-4997-9c34-426b6e6f47be
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# if bool - vs

Starts an if...[else](else---vs.md)...[endif - vs](endif---vs.md) block.

## Syntax



| if bool |
|---------|



 

where bool is a bool register number. See [Constant Boolean Register](dx9-graphics-reference-asm-vs-registers-constant-boolean.md).

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| if bool                |      | x    | x    | x     | x    | x     |



 

If the source Boolean register in the if statement is true, the code enclosed by the if statement and the matching else is run. Otherwise, the code enclosed by the [else](else---vs.md)...[endif - vs](endif---vs.md) statements is run. This instruction consumes one instruction slot.

if blocks can be nested.

An if block cannot straddle a loop block.

## Example

This instruction provides conditional static flow control.


```
defb b2, TRUE

...

if b2
// Instructions to run if b2 is nonzero

else
// Instructions to run otherwise

endif
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> <dt>

[else - vs](else---vs.md)
</dt> <dt>

[endif - vs](endif---vs.md)
</dt> </dl>

 

 




