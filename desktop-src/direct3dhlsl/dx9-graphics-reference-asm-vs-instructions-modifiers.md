---
title: Instruction modifiers (HLSL VS reference)
description: Instruction modifiers
ms.assetid: b713d847-c858-4492-918c-7a105f751624
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Instruction modifiers (HLSL VS reference)

Instruction modifiers affect the result of the instruction before it is written into the destination register.

## \_sat

Saturates (or clamps) the instruction result to \[0,1\] range before writing to the destination register.

For example:


```
add_sat dst, src0, src1
```



Where:

dst = clamp\_between\_0\_and\_1(src0 + src1)

The \_sat instruction modifier costs no additional instruction slots.

If supported, the \_sat instruction modifier can be used with any instruction except: [frc - vs](frc---vs.md), [sincos - vs](sincos---vs.md), and [texldl - vs](texldl---vs.md).



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| \_sat                  |      |      |      |       | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




