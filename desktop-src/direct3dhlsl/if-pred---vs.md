---
title: if pred - vs
description: Start of an if pred - vs...else - vs...endif - vs block, with the condition taken from the content of the predicate register.
ms.assetid: 03f60ca3-cda0-4653-8582-74d1a75e0aee
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# if pred - vs

Start of an if pred - vs...[else - vs](else---vs.md)...[endif - vs](endif---vs.md) block, with the condition taken from the content of the predicate register.

## Syntax



| if \[!\]pred.replicateSwizzle |
|-------------------------------|



 

Where:

-   \[!\] an optional NOT modifier. This modifies the value in the predicate register.
-   pred is the predicate register, p0. See [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md).
-   replicateSwizzle is a single component that is copied (or replicated) to all four components (swizzled). Valid components are: x, y, z, w or r, g, b, a.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| if pred                |      |      | x    | x     | x    | x     |



 

This instruction is used to skip a block of code, based on a channel of the predicate register. Each if\_pred block must end with an else or endif instruction.

Restrictions include:

if\_pred blocks can be nested. This counts to the total dynamic nesting depth along with [if\_comp](if-comp---vs.md) blocks.

An if\_pred block cannot straddle a loop block, it should be either completely inside it or surround it.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




