---
title: dcl_indexRange (sm4 - asm)
description: dcl\_indexRange (sm4 - asm)
ms.assetid: 88af30f3-dbf9-4556-b170-a7371680f9b9
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_indexRange (sm4 - asm)

Declares a range of registers that will be accessed by index (an integer computed in the shader).



| dcl\_indexRange *minRegisterM*, *maxRegisterN* |
|------------------------------------------------|



 




| Item | Description | 
|------|-------------|
| <span id="minRegisterM"></span><span id="minregisterm"></span><span id="MINREGISTERM"></span><em>minRegisterM</em><br /> | [in] The first register to access by index. <br /><ul><li><em>minRegister</em> is either <strong>v</strong> for a vertex or pixel shader input register, or <strong>o</strong> for a vertex shader output register.</li><li><em>M</em> is an integer that denotes the register number.</li></ul> | 
| <span id="maxRegisterN"></span><span id="maxregistern"></span><span id="MAXREGISTERN"></span><em>maxRegisterN</em><br /> | [in] The last register to access by index. Same form as <em>minRegister</em> except <em>N</em> is the register number.<br /> | 




 

The following restrictions apply to all registers:

-   The min and max registers must be the same type and have the same component masks (if masks are declared).
-   A register may have multiple index ranges, as long as they do no not overlap.
-   The min register number must be less than the max register number.
-   An index register cannot contain a [system-value](dx-graphics-hlsl-semantics.md).
-   Indexing a register outside of the max index declaration produces undefined results.

Pixel shader input registers must use the same interpolation mode; pixel shader output registers are not indexable.

A geometry shader input register has two dimensions (vertex axis, attribute axis); the index range applies only to the attribute axis because the vertex axis is always fully indexable.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here is an example.


```
dcl_indexRange v1, v3
dcl_indexRange v4, v9
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

 

 





