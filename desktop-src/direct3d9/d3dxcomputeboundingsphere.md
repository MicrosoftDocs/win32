---
Description: Computes a bounding sphere for the mesh.
ms.assetid: efa1365b-fe3a-4165-a3cb-bc1cd2ba03c0
title: D3DXComputeBoundingSphere function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXComputeBoundingSphere function

Computes a bounding sphere for the mesh.

## Syntax


```C++
HRESULT D3DXComputeBoundingSphere(
  _In_  const D3DXVECTOR3 *pFirstPosition,
  _In_        DWORD       NumVertices,
  _In_        DWORD       dwStride,
  _Out_       D3DXVECTOR3 *pCenter,
  _Out_       FLOAT       *pRadius
);
```



## Parameters

<dl> <dt>

*pFirstPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to first position.

</dd> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of vertices.

</dd> <dt>

*dwStride* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of bytes between position vectors. Use [**GetNumBytesPerVertex**](id3dxbasemesh--getnumbytespervertex.md), [**D3DXGetFVFVertexSize**](d3dxgetfvfvertexsize.md), or [**D3DXGetDeclVertexSize**](d3dxgetdeclvertexsize.md) to get the vertex stride.

</dd> <dt>

*pCenter* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

[**D3DXVECTOR3**](d3dxvector3.md) structure, defining the coordinate center of the returned bounding sphere.

</dd> <dt>

*pRadius* \[out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Radius of the returned bounding sphere.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




