---
title: Position Register
description: This vertex shader output register contains per-vertex position data.
ms.assetid: 98f71027-d94b-4dd0-a6b6-4b263954eff9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Position Register

This vertex shader output register contains per-vertex position data.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Position Register      | x    | x    | x     | x    | x    | x     |



 

A register consists of properties that determine how each register behaves.



| Property        | Description |
|-----------------|-------------|
| Name            | oPos        |
| Count           | 1 vector    |
| I/O permissions | Write-only. |



 

The value is the position in homogeneous clipping space. This value must be written by the vertex shader.

Example


```
    dcl_position v0
    
    def c40, 0.0f,0.0f,0.0f,0.0f;
    // transform into projection space
    m4x4 r0,v0,c8
    max r0.z,c40.z,r0.z //clamp to 0
    max r0.w,c12.x,r0.w //clamp to near clip plane
    mov oPos,r0   
```



## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




