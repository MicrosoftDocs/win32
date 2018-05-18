---
Description: 'Converts mesh adjacency information to an array of point representatives.'
ms.assetid: 'b8914f9c-8550-498d-813d-bb1afe0fb5b2'
title: 'ID3DXBaseMesh::ConvertAdjacencyToPointReps method'
---

# ID3DXBaseMesh::ConvertAdjacencyToPointReps method

Converts mesh adjacency information to an array of point representatives.

## Syntax


```C++
HRESULT ConvertAdjacencyToPointReps(
  [in]      const DWORD *pAdjacency,
  [in, out]       DWORD *pPRep
);
```



## Parameters

<dl> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh. The number of bytes in this array must be at least 3 \* [**ID3DXBaseMesh::GetNumFaces**](id3dxbasemesh--getnumfaces.md) \* sizeof(DWORD).

</dd> <dt>

*pPRep* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to an array of one DWORD per vertex of the mesh that will be filled with point representative data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




