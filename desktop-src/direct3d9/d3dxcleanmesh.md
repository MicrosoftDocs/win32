---
Description: Cleans a mesh, preparing it for simplification.
ms.assetid: 2b586ecc-db87-4b20-a4fc-c8b547bebf65
title: D3DXCleanMesh function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCleanMesh function

Cleans a mesh, preparing it for simplification.

## Syntax


```C++
HRESULT D3DXCleanMesh(
  _In_        D3DXCLEANTYPE CleanType,
  _In_        LPD3DXMESH    pMeshIn,
  _In_  const DWORD         *pAdjacencyIn,
  _Out_       LPD3DXMESH    *ppMeshOut,
  _Out_       DWORD         *pAdjacencyOut,
  _Out_       LPD3DXBUFFER  *ppErrorsAndWarnings
);
```



## Parameters

<dl> <dt>

*CleanType* \[in\]
</dt> <dd>

Type: **[**D3DXCLEANTYPE**](direct3d9.d3dxcleantype)**

Vertex operations to perform in preparation for mesh cleaning. See [**D3DXCLEANTYPE**](direct3d9.d3dxcleantype).

</dd> <dt>

*pMeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the mesh to be cleaned.

</dd> <dt>

*pAdjacencyIn* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh to be cleaned.

</dd> <dt>

*ppMeshOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the returned cleaned mesh. The same mesh is returned that was passed in if no cleaning was necessary.

</dd> <dt>

*pAdjacencyOut* \[out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the output mesh.

</dd> <dt>

*ppErrorsAndWarnings* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a string of errors and warnings, which explain the problems found in the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This function cleans a mesh using the cleaning method and options specified in the CleanType parameter. See the [**D3DXCLEANTYPE**](direct3d9.d3dxcleantype) enumeration for a description of the available options.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




