---
title: Fog Register
description: This vertex shader output register contains a per-vertex fog color.
ms.assetid: b2b06aa9-ad75-48df-857d-fd8719176713
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Fog Register

This vertex shader output register contains a per-vertex fog color.

A register consists of properties that determine how each register behaves.



| Property        | Description                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------|
| Name            | oFog                                                                                            |
| Count           | One vector, of which only one component can be used and must be specified by the component mask |
| I/O permissions | Write-only.                                                                                     |



 

The output fog value registers. The value is the fog factor to be interpolated and then routed to the fog table. Only the scalar x-component of the fog is used.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




