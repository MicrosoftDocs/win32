---
title: Temporary register (HLSL PS reference)
description: Pixel shader input temporary registers are used to hold intermediate results.
ms.assetid: e61daaa1-0a9b-4b1c-b91c-56573be59ed9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Temporary register (HLSL PS reference)

Pixel shader input temporary registers are used to hold intermediate results.

Syntax


```
no declaration is required
```





| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|-------|------|------|-------|
| Temporary Register    |      |      |      |      | x    | x     | x    | x    | x     |



 

-   There are 12 pixel-shader temporary registers: r0 to r11.
-   These registers are used for storing intermediate results during computations.
-   If a temporary register uses components that are not defined in previous code, shader validation will fail.
-   These are at least floating-point precision.
-   A maximum of three can be used in a single instruction.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 




