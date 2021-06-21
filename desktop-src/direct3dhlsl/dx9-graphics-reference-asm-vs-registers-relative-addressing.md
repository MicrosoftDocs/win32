---
title: Relative Addressing (HLSL VS reference)
description: For vertex shaders, the \ \ syntax can be used only in register types that can be relatively addressed in certain shader models.
ms.assetid: 9f9d2499-73a5-4c9d-9dce-94c914933334
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Relative Addressing (HLSL VS reference)

The \[ \] syntax can be used only in register types that can be relatively addressed in certain shader models. The supported forms of \[ \] syntax are listed as follows:

Where:

-   "R" denotes any register type that can be relatively addressed.
-   "A" denotes any register that can be used as an index to relatively address other registers.
-   n0 - ni, m0 - mj, and k are integers >= 0.



| \[ \] syntax                              | Effective index                       | Examples                         |
|-------------------------------------------|---------------------------------------|----------------------------------|
| R\[ A + m0 + ... + mj \]                  | A + m0 + ... + mj                     | c\[ a0.x + 3 + 7 \]              |
| R\[ k \] ( = Rk )                         | k                                     | c\[ 10 \] ( = c10 )              |
| R\[ A \]                                  | A                                     | c\[ a0.y \]                      |
| Rk\[ n0 + ... + ni + A + m0 + ... + mj \] | A + k + n0 + ... + ni + m0 + ... + mj | c8\[ 3 + 2 + a0.w + 5 + 6 + 1 \] |
| R\[ n0 + ... + ni + A + m0 + ... + mj \]  | A + n0 + ... + ni + m0 + ... + mj     | c\[ 2 + 1 + aL + 3 + 4 + 5 \]    |
| Rk\[ A \]                                 | A + k                                 | c12\[ aL \], c0\[ a0.z \]        |
| Rk\[ A + m0 + ... + mj \]                 | A + k + m0 + ... + mj                 | v1\[ aL + 4 + 8 \]               |
| R\[ n0 + ... + ni + A \]                  | A + n0 + ... + ni                     | o\[ 3 + 1 + aL \]                |
| Rk\[ n0 + ... + ni + A \]                 | A + k + n0 + ... + ni                 | o1\[ 2 + 1 + 3 + aL \]           |



 

The registers are available in the following versions:



| Register type | Vertex Shader Versions |
|---------------|------------------------|
| a0            | All                    |
| aL            | vs\_2\_0 and higher    |
| cn            | vs\_1\_1 and higher    |
| on            | vs\_3\_0               |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




