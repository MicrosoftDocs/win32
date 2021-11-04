---
title: Loop counter register (HLSL PS reference)
description: Read about the loop counter register for pixel shaders. The only register in this bank is the current loop counter (aL) register.
ms.assetid: 36999873-a251-4939-aac0-faa7f910bc33
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Loop counter register (HLSL PS reference)

The only register in this bank is the current loop counter (aL) register. It automatically gets incremented in each execution of the [loop - ps](loop---ps.md)/[endloop - ps](endloop---ps.md) block. So it can be used in the block for relative addressing if needed and is invalid to use it outside the loop.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|-------|------|------|-------|
| Loop Counter Register |      |      |      |      |      |       |      | x    | x     |



 

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 




