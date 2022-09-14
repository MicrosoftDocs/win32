---
title: Input Register
description: Input Register
ms.assetid: 7cd8e555-4e69-4905-a541-62e09b41a602
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Input Register

Vertex shader input register.

Data from each vertex (using one or more input vertex streams) is loaded into the vertex input registers before the vertex shader is run. The input registers consist of 16 four-component floating-point vectors, designated as v0 through v15. These registers are read-only. An input register is bound to vertex data through a vertex declaration.

The following register properties control how each register behaves:



| Property        | Description                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| Name            | v\[n\] - n is an optional register number. 0 is the default value used, if it is omitted.     |
| Count           | A maximum of 16 registers, v0 - v15.                                                          |
| I/O permissions | Read-only. This register cannot be written by the API or within the shader.                   |
| Read ports      | 1. This is the number of times a register can be read within a single instruction. See below. |



 

Any single instruction can access only one vertex input register. However, each source in the instruction can independently swizzle and negate that vector as it is read.

## Example

Here is an example using a vertex declaration to bind 2D vertex position data to register v0.

The vertex declaration belongs in the application:


```
D3DVERTEXELEMENT9 decl[] =
{
    { 0, 0, D3DDECLTYPE_FLOAT2, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITION, 0 },
      D3DDECL_END()
};
```



Here is the corresponding vertex shader declaration:


```
dcl_position v0
```





| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Position Register      | x    | x    | x     | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




