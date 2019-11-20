---
title: ps
description: This instruction specifies the shader version number and works on all shader versions.
ms.assetid: 953b1d66-09c1-4ad5-96d4-acb49a1f244c
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# ps

This instruction specifies the shader version number and works on all shader versions.

## Syntax


```
ps_mainVer_subVer
```



## Input Arguments

Input arguments contain a single main version number with a single sub version number. The allowable combinations are listed in the table below.



| Main versions | Sub versions                   |
|---------------|--------------------------------|
| 1             | 1, 2, 3, 4                     |
| 2             | 0, x (extended), sw (software) |
| 3             | 0, sw (software)               |



 

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| ps                    | x    | x    | x    | x    | x    | x    | x     | x    | x     |



 

This instruction must be the first non-comment instruction in a pixel shader.

Hardware accelerated versions of the software (versions without \_sw in the version number), can process vertices with hardware accelearation or use software vertex processing. Software versions (versions with \_sw in the version number) process vertices only with software.

## Examples

This partial example declares a version 1\_1 pixel shader.


```
ps_1_1
```



This partial example declares a version 1\_4 pixel shader.


```
ps_1_4
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




