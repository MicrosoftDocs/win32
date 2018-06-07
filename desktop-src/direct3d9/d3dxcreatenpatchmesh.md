---
Description: Creates an N-patch mesh from a triangle mesh.
ms.assetid: f565ed0b-72fc-4184-b423-f68b0acfafb0
title: D3DXCreateNPatchMesh function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXCreateNPatchMesh function

Creates an N-patch mesh from a triangle mesh.

## Syntax


```C++
HRESULT D3DXCreateNPatchMesh(
  _In_    LPD3DXMESH      pMeshSysMem,
  _Inout_ LPD3DXPATCHMESH *pPatchMesh
);
```



## Parameters

<dl> <dt>

*pMeshSysMem* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Address of a pointer to an [**ID3DXMesh**](id3dxmesh.md) interface that represents the triangle mesh object.

</dd> <dt>

*pPatchMesh* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPATCHMESH**](id3dxpatchmesh.md)\***

Address of a pointer to an [**ID3DXPatchMesh**](id3dxpatchmesh.md) interface that represents the created patch mesh object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




