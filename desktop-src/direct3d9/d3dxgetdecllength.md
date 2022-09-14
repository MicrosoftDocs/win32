---
description: Returns the number of elements in the vertex declaration.
ms.assetid: 3ce24e59-0ec3-4d53-8bc8-8a5a7cdf53b2
title: D3DXGetDeclLength function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXGetDeclLength
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXGetDeclLength function

Returns the number of elements in the vertex declaration.

## Syntax


```C++
UINT D3DXGetDeclLength(
  _In_ const D3DVERTEXELEMENT9 *pDecl
);
```



## Parameters

<dl> <dt>

*pDecl* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

A pointer to the vertex declaration. See [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

</dd> </dl>

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of elements in the vertex declaration.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
