---
title: dcl\_outputTopology (sm4 - asm)
description: dcl\_outputTopology (sm4 - asm)
ms.assetid: 'a03a6feb-ec34-4655-a68c-a91e31e7140b'
---

# dcl\_outputTopology (sm4 - asm)

Declares the primitive type geometry-shader output data.



| dcl\_outputTopology *Type* |
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
<td><span id="Type"></span><span id="type"></span><span id="TYPE"></span><em>Type</em><br/></td>
<td>[in] An output primitive topology, which is one of the following values: <br/>
<ul>
<li><em>pointlist</em></li>
<li><em>linestrip</em></li>
<li><em>trianglestrip</em></li>
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
dcl_outputTopology trianglestrip
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

 

 





