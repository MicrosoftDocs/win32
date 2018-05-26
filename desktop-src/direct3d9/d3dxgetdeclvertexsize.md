---
Description: Returns the size of a vertex from the vertex declaration.
ms.assetid: a2524f96-103e-43ab-bdcb-b99e7402fd89
title: D3DXGetDeclVertexSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXGetDeclVertexSize function

Returns the size of a vertex from the vertex declaration.

## Syntax


```C++
UINT D3DXGetDeclVertexSize(
  _In_ const D3DVERTEXELEMENT9 *pDecl,
  _In_       DWORD             Stream
);
```



## Parameters

<dl> <dt>

*pDecl* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

A pointer to the vertex declaration. See [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

</dd> <dt>

*Stream* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

The zero-based stream index.

</dd> </dl>

## Return value

Type: **[**UINT**](winprog.windows_data_types)**

The vertex declaration size, in bytes.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




