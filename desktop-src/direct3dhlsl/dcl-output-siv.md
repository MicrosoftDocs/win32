---
title: dcl_output_siv (sm4 - asm)
description: dcl\_output\_siv (sm4 - asm)
ms.assetid: 5a87a113-7413-48ef-9a6a-13eb185650be
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_output\_siv (sm4 - asm)

Declares an output register that contains a [system-value](dx-graphics-hlsl-semantics.md) parameter.



| dcl\_output\_siv oN\[*.masks*\], *systemValue* |
|------------------------------------------------|



 



| Item                                                                                                                               | Description                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="oN"></span><span id="on"></span><span id="ON"></span>o*N*<br/>                                                     | \[in\] An output data register; *N* is an integer that denotes the register number.<br/>                                                      |
| <span id="_.mask_"></span><span id="_.MASK_"></span>*\[.mask\]*<br/>                                                         | \[in\] Optional. A component mask (.xyzw) that specifies which of the register components to use.<br/>                                        |
| <span id="systemValueName"></span><span id="systemvaluename"></span><span id="SYSTEMVALUENAME"></span>*systemValueName*<br/> | \[in\] The system-value name which is a string (see [system-value semantics](dx-graphics-hlsl-semantics.md)) without the "SV\_" prefix.<br/> |



 

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               |              |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here are some examples.


```
dcl_output o[0].y
dcl_output_siv o[0].w, clipDistance
dcl_output_siv o[0].z, cullDistance
```



## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





