---
description: Splits a mesh into meshes smaller than the specified size.
ms.assetid: 55cdd82f-91fa-4805-969f-8fbe53cbde58
title: D3DXSplitMesh function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSplitMesh
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSplitMesh function

Splits a mesh into meshes smaller than the specified size.

## Syntax


```C++
void D3DXSplitMesh(
  _In_        LPD3DXMESH   pMeshIn,
  _In_  const DWORD        *pAdjacencyIn,
  _In_  const DWORD        MaxSize,
  _In_  const DWORD        Options,
  _Out_       DWORD        *pMeshesOut,
  _Out_       LPD3DXBUFFER *ppMeshArrayOut,
  _Out_       LPD3DXBUFFER *ppAdjacencyArrayOut,
  _Out_       LPD3DXBUFFER *ppFaceRemapArrayOut,
  _Out_       LPD3DXBUFFER *ppVertRemapArrayOut
);
```



## Parameters

<dl> <dt>

*pMeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the source mesh.

</dd> <dt>

*pAdjacencyIn* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh to be simplified.

</dd> <dt>

*MaxSize* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)**

Maximum number of vertices in the resulting mesh.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)**

Option flags for the new meshes.

</dd> <dt>

*pMeshesOut* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Number of meshes returned.

</dd> <dt>

*ppMeshArrayOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing an array of [**ID3DXMesh**](id3dxmesh.md) interfaces for the new meshes. For a source mesh split into n meshes, *ppMeshArrayOut* is an array of n **ID3DXMesh** pointers.

</dd> <dt>

*ppAdjacencyArrayOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing an array of adjacency arrays (DWORDs) for the new meshes. See [**ID3DXBuffer**](id3dxbuffer.md). This parameter is optional.

</dd> <dt>

*ppFaceRemapArrayOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing an array of face remap arrays (DWORDs) for the new meshes. See [**ID3DXBuffer**](id3dxbuffer.md). This parameter is optional.

</dd> <dt>

*ppVertRemapArrayOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing an array of vertex remap arrays for the new meshes. See [**ID3DXBuffer**](id3dxbuffer.md). This parameter is optional.

</dd> </dl>

## Return value

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

A common use of this function is to split a mesh with 32-bit indices (more than 65535 vertices) into more than one mesh, each of which has 16-bit indices.

The adjacency, vertex remap and face remap arrays are arrays are DWORDs where each array contains n DWORD pointers, followed by the DWORD data referenced by the pointers. For example, to obtain the face remap information for face 3 in mesh 2, the following code could be used, assuming the face remap data was returned in a variable named *ppFaceRemapArrayOut*.


```
   
const DWORD **face_remaps = 
    static_cast<DWORD **>(ppFaceRemapArrayOut->GetBufferPointer());
const DWORD remap = face_remaps[2][3];
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
