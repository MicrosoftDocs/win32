---
title: dcl_inputPrimitive (sm4 - asm)
description: dcl\_inputPrimitive (sm4 - asm)
ms.assetid: 86672fd3-7955-45ac-a8b2-a9cc8d1e8805
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# dcl\_inputPrimitive (sm4 - asm)

Declares the primitive type for geometry-shader inputs.



| dcl\_inputPrimitive *type* |
|----------------------------|



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="type"></span><span id="TYPE"></span><em>type</em><br/></td>
<td>[in] Input-data primitive type, which is one of the following: <br/>
<ul>
<li><em>point</em> - point list</li>
<li><em>line</em> - line list</li>
<li><em>triangle</em> - triangle list</li>
<li><em>line_adj</em> - line list with adjacency data</li>
<li><em>triangle_adj</em> - triangle list with adjacency data</li>
</ul></td>
</tr>
</tbody>
</table>



 

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               | x               |              |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here is an example.


```
dcl_inputPrimitive triangle
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

 

 





