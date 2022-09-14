---
title: dcl_constantBuffer (sm4 - asm)
description: dcl\_constantBuffer (sm4 - asm)
ms.assetid: 164fb2a4-8782-42f0-b4ba-1f87d9c7255d
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_constantBuffer (sm4 - asm)

Declares a shader constant buffer.



| dcl\_constantBuffer *cbN\[size\]*, *AccessPattern* |
|----------------------------------------------------|



 



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="cbN_size_"></span><span id="cbn_size_"></span><span id="CBN_SIZE_"></span>cb<em>N[size]</em><br/></td>
<td>[in] A shader constant buffer where N is an integer that denotes the constant-buffer-register number and size is an integer that denotes the number of elements in the buffer.<br/></td>
</tr>
<tr class="even">
<td><span id="AccessPattern"></span><span id="accesspattern"></span><span id="ACCESSPATTERN"></span><em>AccessPattern</em><br/></td>
<td>[in] The way that the buffer will be accessed by shader code, which is one of the following: <br/> 
<table>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>immediateIndexed</td>
<td>Index the buffer with a literal value.</td>
</tr>
<tr class="even">
<td>dynamic_indexed</td>
<td>Index the buffer with the result of an evaluated expression.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

This example declares a constant buffer for register cb0, which has 19 elements. These elements are accessed with a literal index.


```
dcl_constantbuffer  cb0[19], immediateIndexed
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

 

 





