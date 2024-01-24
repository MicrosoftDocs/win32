---
description: Validates a patch mesh, returning the number of degenerate vertices and patches.
ms.assetid: a95ff9d9-d476-42ac-8d7e-1dc42418f763
title: D3DXValidPatchMesh function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXValidPatchMesh
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXValidPatchMesh function

Validates a patch mesh, returning the number of degenerate vertices and patches.

## Syntax


```C++
HRESULT D3DXValidPatchMesh(
  _In_  LPD3DXPATCHMESH pMeshIn,
  _Out_ DWORD           *pNumDegenerateVertices,
  _Out_ DWORD           *pNumDegeneratePatches,
  _Out_ LPD3DXBUFFER    *ppErrorsAndWarnings
);
```



## Parameters

<dl> <dt>

*pMeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXPATCHMESH**](id3dxpatchmesh.md)**

Pointer to an [**ID3DXPatchMesh**](id3dxpatchmesh.md) interface, representing the patch mesh to be tested.

</dd> <dt>

*pNumDegenerateVertices* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Returns the number of degenerate vertices in the patch mesh.

</dd> <dt>

*pNumDegeneratePatches* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Returns the number of degenerate patches in the patch mesh.

</dd> <dt>

*ppErrorsAndWarnings* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a pointer to a buffer containing a string of errors and warnings that explain the problems found in the patch mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method validates the mesh by checking for invalid indices. Error information is available from the debugger output.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
