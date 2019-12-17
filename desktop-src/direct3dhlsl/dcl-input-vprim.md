---
title: dcl_input vPrim (sm4 - asm)
description: dcl\_input vPrim (sm4 - asm)
ms.assetid: 75287673-21d6-4eb7-829f-7f2f340aec54
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_input vPrim (sm4 - asm)

Declares that a geometry shader uses its scalar input-register vPrim.



| dcl\_input *vPrim* |
|--------------------|



 



| Item                                                                                       | Description                                                                                              |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <span id="vPrim"></span><span id="vprim"></span><span id="VPRIM"></span>*vPrim*<br/> | \[in\] A 32-bit scalar, which can be applied to each interior primitive in a geometry shader.<br/> |



 

The scalar cannot be applied to any adjacent primitives.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               | x               |              |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

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

 

 





