---
title: Address Register
description: The a0 register is an address register.
ms.assetid: ad86013c-3358-4770-a01c-544c868691f4
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Address Register

The a0 register is an address register. A single register is available in version vs\_1\_1. The address register, designated as a0.x in vs\_1\_1, can be used as a signed integer offset for relative addressing into the constant register file. For versions vs\_2\_0 and above, all four components (.x, .y, .z, .w) are available for relative addressing.


```
c[a0.x + n]
```



The address register cannot be read by a vertex shader, it can only be used for relative addressing of a constant register. Reading values outside of the legal range will return (0.0, 0.0, 0.0, 0.0). The address register can only be a destination for the [mov - vs](mov---vs.md) instruction. If a floating-point number is moved into an integer register, a round-to-nearest conversion happens.

All shaders must initialize the address register before using it. For version vs\_2\_0 and above, the [mova - vs](mova---vs.md) instruction can move a floating-point value to an address register.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Address Register       | x    | x    | x     | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




