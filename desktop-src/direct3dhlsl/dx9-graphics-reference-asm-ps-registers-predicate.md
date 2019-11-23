---
title: Predicate register (HLSL PS reference)
description: This pixel shader output register contains a per-channel boolean value.
ms.assetid: dc5bff90-4efa-4390-b744-dd1e894ff540
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Predicate register (HLSL PS reference)

This pixel shader output register contains a per-channel boolean value.

A predicate register is supported by the following versions:



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|-------|------|------|-------|
| predicate register    |      |      |      |      |      |       | x    | x    | x     |



 

Here are the register properties.



| Register type | Count | R/W | \# Read ports | \# Reads/inst | Dimension | RelAddr | Defaults | Requires DCL |
|---------------|-------|-----|---------------|---------------|-----------|---------|----------|--------------|
| Predicate(p)  | 1     | R/W | 1             | 1             | 4         | N/A     | None     | N            |



 

The predicate register can be modified with [setp\_comp - ps](setp-comp---ps.md). There are no default values for this register; an application needs to set the register before it is used.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 




