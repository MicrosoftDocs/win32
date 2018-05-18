---
Description: 'Converts point representative data to mesh adjacency information.'
ms.assetid: '6ae40486-74be-45a8-9971-f20517c8dcf0'
title: 'ID3DXBaseMesh::ConvertPointRepsToAdjacency method'
---

# ID3DXBaseMesh::ConvertPointRepsToAdjacency method

Converts point representative data to mesh adjacency information.

## Syntax


```C++
HRESULT ConvertPointRepsToAdjacency(
  [in]      const DWORD *pPRep,
  [in, out]       DWORD *pAdjacency
);
```



## Parameters

<dl> <dt>

*pPRep* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to an array of one DWORD per vertex of the mesh that contains point representative data. This parameter is optional. Supplying a **NULL** value will cause this parameter to be interpreted as an "identity" array.

</dd> <dt>

*pAdjacency* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh. The number of bytes in this array must be at least 3 \* [**ID3DXBaseMesh::GetNumFaces**](id3dxbasemesh--getnumfaces.md) \* sizeof(DWORD).

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

 

 




