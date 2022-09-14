---
title: if pred - ps
description: Start of an if bool - ps...else - ps...endif - ps block, with the condition taken from the content of the predicate register.
ms.assetid: 7b43bf71-a2e9-468f-805f-620de065db08
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# if pred - ps

Start of an [if bool - ps](if-bool---ps.md)...[else - ps](else---ps.md)...[endif - ps](endif---ps.md) block, with the condition taken from the content of the predicate register.

## Syntax



| if \[!\]pred.replicateSwizzle |
|-------------------------------|



 

Where:

-   \[!\] is an optional NOT modifier. This modifies the value in the predicate register.
-   pred is the [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md).
-   replicateSwizzle is a single component that is copied (or replicated) to all four components (swizzled). Valid components are: \[x, y, z, w\] or \[r, g, b, a\].

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| if\_pred              |      |      |      |      |      | x    | x     | x    | x     |



 

This instruction is used to skip a block of code, based on a channel of the predicate register. Each if\_pred block must end with an [else - ps](else---ps.md) or [endif - ps](endif---ps.md) instruction.

Restrictions include:

if\_pred blocks can be nested. This counts to the total dynamic nesting depth along with [if\_comp](if-comp---ps.md) blocks.

An if\_pred block cannot straddle a loop block; it should either be completely inside it or surround it.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




