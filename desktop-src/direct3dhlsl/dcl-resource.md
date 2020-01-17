---
title: dcl_resource (sm4 - asm)
description: dcl\_resource (sm4 - asm)
ms.assetid: 045610f0-f7db-4bf2-bfea-501bbee94601
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_resource (sm4 - asm)

Declares a non-multisampled shader-input resource.



| dcl\_resource *tN*, *resourceType*, *returnType(s)* |
|-----------------------------------------------------|



 

Declares a multisampled shader-input resource.



| dcl\_resource *tN*, *resourceType\[size\]NN*, *returnType(s)* |
|---------------------------------------------------------------|



 



| Item                                                                                                                                                     | Description                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="tN"></span><span id="tn"></span><span id="TN"></span>t*N*<br/>                                                                           | \[in\] The texture register, where *N* is an integer that denotes the register number.<br/>                                                                                                                                                                        |
| <span id="resourceType"></span><span id="resourcetype"></span><span id="RESOURCETYPE"></span>*resourceType*<br/>                                   | \[in\] Any object type listed in the [texture-object](dx-graphics-hlsl-to-type.md) page.<br/>                                                                                                                                                                     |
| <span id="resourceType_size_NN"></span><span id="resourcetype_size_nn"></span><span id="RESOURCETYPE_SIZE_NN"></span>*resourceType\[size\]NN*<br/> | \[in\] A Texture2D or a Texture2DArray object type (see the [texture-object](dx-graphics-hlsl-to-type.md) page); *size* is an optional integer that denotes the number of elements in the array; *NN* is an integer that denotes the number of multisamples.<br/> |
| <span id="returnType_s_"></span><span id="returntype_s_"></span><span id="RETURNTYPE_S_"></span>*returnType(s)*<br/>                               | \[in\] Per-component return type which is one of the following: UNORM, SNORM, SINT, UINT, or FLOAT. The number of return types can be as few as 1 (if all components are the same type), but can be as many as four.<br/>                                          |



 

A resource is accessed in HLSL using [load](dx-graphics-hlsl-to-load.md); a non-multisampled texture can also be accessed using any of the HLSL [texture object](dx-graphics-hlsl-to-type.md) sample methods.

If a resource is bound to a shader stage, the resource format will be validated against the return type.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here is an example.


```
dcl_resource t3, buffer, UNORM
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

 

 





