---
title: dcl_temps (sm4 - asm)
description: dcl\_temps (sm4 - asm)
ms.assetid: ecfbdd1e-0f2d-4371-91cc-ebc3e5ee8ee7
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_temps (sm4 - asm)

Declares temporary registers.



| dcl\_temps N |
|--------------|



 



| Item                                                   | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| <span id="N"></span><span id="n"></span>*N*<br/> | \[in\] The number of temporary registers.<br/> |



 

Each register has space for a 32-bit four-component value. The total number of temporary and [indexable-temporary](dcl-indexabletemp.md) registers must be less than or equal to 4096.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here is an example.


```
dcl_temps 10; // Declare r0-r9
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

 

 





