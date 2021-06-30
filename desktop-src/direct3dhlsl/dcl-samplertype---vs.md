---
title: dcl_samplerType (sm3 - vs asm)
description: Declare a vertex shader sampler.
ms.assetid: 733307ac-24ab-4db7-bf70-58a83b4c39b1
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_samplerType (sm3 - vs asm)

Declare a vertex shader sampler.

## Syntax

dcl\_samplerType s\#



 

where:

-   \_samplerType defines the sampler data type. This determines how many coordinates are required by each texture coordinate when sampling. The following texture coordinate dimensions are defined.
    -   \_2d
    -   \_cube
    -   \_volume
-   s\# identifies a sampler where s is an abbreviation for the sampler, and \# is the sampler number. [Sampler (Direct3D 9 asm-vs)](dx9-graphics-reference-asm-vs-registers-sampler.md)s are pseudo registers because you cannot directly read or write to them.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| dcl\_samplerType       |      |      |      |       | x    | x     |



 

All dcl\_samplerType instructions must appear before the first executable instruction.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




