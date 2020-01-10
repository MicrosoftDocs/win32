---
title: Predicate Register (HLSL VS reference)
description: This vertex shader output register contains a per-channel Boolean value.
ms.assetid: 4b06e19a-78c7-4886-a0e2-225d419282e7
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Predicate Register (HLSL VS reference)

This vertex shader output register contains a per-channel Boolean value.

A predicate register is supported by the following versions.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| predicate register     |      |      |       | x    | x    | x     |



 

Here are the register properties.



| Register type | Count | R/W | \# Read ports | \# Reads/inst | Dimension | RelAddr | Defaults | Requires DCL |
|---------------|-------|-----|---------------|---------------|-----------|---------|----------|--------------|
| Predicate(p)  | 1     | R/W | 1             | 1             | 4         | N/A     | None     | N            |



 

The predicate register can be modified with [setp\_comp - vs](setp-comp---vs.md). There are no default values for this register, an application needs to set the register before it is used.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




