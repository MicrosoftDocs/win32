---
title: Loop Counter Register (HLSL VS reference)
description: Read about the loop counter register for vertex shaders. The only register in this bank is the current loop counter (aL) register.
ms.assetid: b32fabf8-38d3-446c-bb80-c647d5aa028d
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Loop Counter Register (HLSL VS reference)

The only register in this bank is the current loop counter (aL) register. It automatically gets incremented in each execution of the [loop - vs](loop---vs.md)...[endloop - vs](endloop---vs.md) block. So it can be used in the block for relative addressing if needed and is invalid to use it outside the loop.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




