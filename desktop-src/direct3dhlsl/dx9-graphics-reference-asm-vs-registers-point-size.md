---
title: Point Size Register
description: This vertex shader output register contains per-vertex point size data.
ms.assetid: 1aa6cd7d-9d29-4e7e-8448-8b9a6b251a02
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Point Size Register

This vertex shader output register contains per-vertex point size data.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Point Size Register    | x    | x    | x     | x    | x    | x     |



 

A register consists of properties that determine how each register behaves.



| Property        | Description                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------|
| Name            | oPts                                                                                            |
| Count           | 1 vector, of which of only 1 component can be used and must be specified by the component mask. |
| I/O permissions | Write-only.                                                                                     |



 

Only the scalar x-component of the point size is used.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




