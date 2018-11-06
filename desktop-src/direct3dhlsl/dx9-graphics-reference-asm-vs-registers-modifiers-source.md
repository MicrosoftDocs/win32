---
title: Vertex Shader Source Register Modifiers
description: Source modifiers can be applied to modify the data read from a source register before the data is used by the instruction.
ms.assetid: 516ff7ca-0071-44ac-a246-612a9faa7e7b
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Vertex Shader Source Register Modifiers

Source modifiers can be applied to modify the data read from a source register before the data is used by the instruction.

## Negate

Negate the contents of the source register.



| Component modifier | Description     |
|--------------------|-----------------|
| \- r               | Source negation |



 

The negate modifier cannot be used on second source register of these instructions: [m3x2 - vs](m3x2---vs.md), [m3x3 - vs](m3x3---vs.md), [m3x4 - vs](m3x4---vs.md), [m4x3 - vs](m4x3---vs.md), [m4x4 - vs](m4x4---vs.md).



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| \-                     | x    | x    | x    | x     | x    | x     |



 

## Absolute Value

Take the absolute value of the register.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| abs                    |      |      |      |       | x    | x     |



 

If any version 3 shader reads from one or more constant float registers (c\#), one of the following must be true.

-   All of the constant floating-point registers must use the abs modifier.
-   None of the constant floating-point registers can use the abs modifier.

## Related topics

<dl> <dt>

[Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md)
</dt> </dl>

 

 




