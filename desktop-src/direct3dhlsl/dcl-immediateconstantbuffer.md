---
title: dcl_immediateConstantBuffer (sm4 - asm)
description: dcl\_immediateConstantBuffer (sm4 - asm)
ms.assetid: 55e21ab1-0749-4200-8e68-bb098e935dac
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_immediateConstantBuffer (sm4 - asm)

Declares a shader immediate-constant buffer.



| dcl\_immediateConstantBuffer *value(s)* |
|-----------------------------------------|



 

<dl> <dt>

<span id="value_s_"></span><span id="VALUE_S_"></span>*value(s)*
</dt> <dd>

\[in\] The buffer must contain at least one value, but not more than 4096 values.

</dd> </dl>

### Remarks

A shader is allowed one immediate-constant buffer. An immediate-constant buffer is accessed just like a constant buffer with dynamic indexing.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

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

 

 




