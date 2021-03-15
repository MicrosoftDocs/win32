---
description: Creates a skin mesh from another mesh.
ms.assetid: 4c69377e-61ef-42b8-8864-c116164d4b22
title: D3DXCreateSkinInfoFromBlendedMesh function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCreateSkinInfoFromBlendedMesh
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreateSkinInfoFromBlendedMesh function

Creates a skin mesh from another mesh.

## Syntax


```C++
HRESULT D3DXCreateSkinInfoFromBlendedMesh(
  _In_        LPD3DXBASEMESH      pMesh,
  _In_        DWORD               NumBones,
  _In_  const D3DXBONECOMBINATION *pBoneCombinationTable,
  _Out_       LPD3DXSKININFO      *ppSkinInfo
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXBASEMESH**](id3dxbasemesh.md)**

Pointer to an [**ID3DXBaseMesh**](id3dxbasemesh.md) object, the mesh from which to create the skin mesh.

</dd> <dt>

*NumBones* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

The length of the array attached to the BoneId. See [**D3DXBONECOMBINATION**](d3dxbonecombination.md).

</dd> <dt>

*pBoneCombinationTable* \[in\]
</dt> <dd>

Type: **const [**D3DXBONECOMBINATION**](d3dxbonecombination.md)\***

Pointer to an array of bone combinations. See [**D3DXBONECOMBINATION**](d3dxbonecombination.md).

</dd> <dt>

*ppSkinInfo* \[out\]
</dt> <dd>

Type: **[**LPD3DXSKININFO**](id3dxskininfo.md)\***

Address of a pointer to an [**ID3DXSkinInfo**](id3dxskininfo.md) interface representing the created skin mesh object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
