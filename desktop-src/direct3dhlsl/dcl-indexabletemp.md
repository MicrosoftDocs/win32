---
title: dcl_indexableTemp (sm4 - asm)
description: dcl\_indexableTemp (sm4 - asm)
ms.assetid: 32d8e7ce-4b28-48c3-b794-56ace96394f0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_indexableTemp (sm4 - asm)

Declares an indexable, temporary register.



| dcl\_indexableTemp xN\[size\], ComponentCount |
|-------------------------------------------------|



 



| Item                                                                                                                           | Description                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span id="xN"></span><span id="xn"></span>*xN*<br/>                                                                         | \[in\] A temporary indexable register.<br/><ul><li><em>N</em> is an integer that identifies the register number.</li><li><em>*\[size\]*</em> is an optional integer value. The number of elements in the register array.</li></ul> |
| <span id="ComponentCount"></span><span id="componentcount"></span><span id="COMPONENTCOUNT"></span>*ComponentCount*<br/> | \[in\] An optional integer value.The number of components in the register array.<br/> |



 

A register contains enough space for a 32-bit four-component value; the number of elements in the array of temporary registers (indexable and [non-indexable](dcl-temps.md)) cannot exceed 4096.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here are some examples of the code generated for indexable registers.


```
dcl_indexableTemp x0[23], 2 ; // An indexable array of 23, 2-component, 32-bit elements
dcl_indexableTemp x1[16], 4 ; // An indexable array of 16, 4-component, 32-bit elements
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

 

 





