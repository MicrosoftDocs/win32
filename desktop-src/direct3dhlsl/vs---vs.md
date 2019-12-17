---
title: vs
description: This instruction specifies the shader version number. This instruction works on all shader versions.
ms.assetid: edcbaff3-eb32-49e6-80de-621b67d4df75
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# vs

This instruction specifies the shader version number. This instruction works on all shader versions.

## Syntax


```
vs_mainVer_subVer
```



## Input Arguments

Input arguments contain a single main version number with a single sub version number. The allowable combinations are listed in the table below.



| Main versions | Sub versions                   |
|---------------|--------------------------------|
| 1             | 1                              |
| 2             | 0, sw (software), x (extended) |
| 3             | 0, sw (software)               |



 

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| vs                     | x    | x    | x    | x     | x    | x     |



 

This instruction must be the first non-comment instruction in a vertex shader.

This instruction is supported in all vertex shader versions.

Hardware accelerated versions of the software (versions without \_sw in the version number), can process vertices with hardware accelearation or use software vertex processing. Software versions (versions with \_sw in the version number) process vertices only with software.

## Examples

This partial example declares a version 1\_1 vertex shader.


```
vs_1_1
```



This partial example declares a version 2 software vertex shader.


```
vs_2_sw
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




