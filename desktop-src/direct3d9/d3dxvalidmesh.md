---
Description: 'Validates a mesh.'
ms.assetid: 'e5bec2f3-e914-4677-8114-77c71b8a586e'
title: D3DXValidMesh function
---

# D3DXValidMesh function

Validates a mesh.

## Syntax


```C++
HRESULT D3DXValidMesh(
  _In_        LPD3DXMESH   pMeshIn,
  _In_  const DWORD        *pAdjacency,
  _Out_       LPD3DXBUFFER *ppErrorsAndWarnings
);
```



## Parameters

<dl> <dt>

*pMeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the mesh to be tested.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh to be tested.

</dd> <dt>

*ppErrorsAndWarnings* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a string of errors and warnings, which explain the problems found in the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DXERR\_INVALIDMESH, D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method validates the mesh by checking for invalid indices. Error information is available from the debugger output.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




