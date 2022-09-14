---
description: Takes a mesh and returns a new mesh with per-vertex blend weights and a bone combination table. The table describes which bones affect which subsets of the mesh.
ms.assetid: c26a9e84-5731-4394-a047-5f1ffe7688d9
title: ID3DXSkinInfo::ConvertToBlendedMesh method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.ConvertToBlendedMesh
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::ConvertToBlendedMesh method

Takes a mesh and returns a new mesh with per-vertex blend weights and a bone combination table. The table describes which bones affect which subsets of the mesh.

## Syntax


```C++
HRESULT ConvertToBlendedMesh(
  [in]        LPD3DXMESH   pMesh,
  [in]        DWORD        Options,
  [in]  const DWORD        *pAdjacencyIn,
  [in]        LPDWORD      pAdjacencyOut,
  [out]       DWORD        *pFaceRemap,
  [out]       LPD3DXBUFFER *ppVertexRemap,
  [out]       DWORD        *pMaxVertexInfl,
  [out]       DWORD        *pNumBoneCombinations,
  [out]       LPD3DXBUFFER *ppBoneCombinationTable,
  [out]       LPD3DXMESH   *ppMesh
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Input mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Currently unused.

</dd> <dt>

*pAdjacencyIn* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Input mesh adjacency information.

</dd> <dt>

*pAdjacencyOut* \[in\]
</dt> <dd>

Type: **[**LPDWORD**](../winprog/windows-data-types.md)**

Output mesh adjacency information.

</dd> <dt>

*pFaceRemap* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

An array of DWORDs, one per face, that identifies the original mesh face that corresponds to each face in the blended mesh. If the value supplied for this argument is **NULL**, face remap data is not returned.

</dd> <dt>

*ppVertexRemap* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface, which contains a DWORD for each vertex that specifies how the new vertices map to the old vertices. This remap is useful if you need to alter external data based on the new vertex mapping. This parameter is optional; **NULL** may be used.

</dd> <dt>

*pMaxVertexInfl* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to a DWORD that will contain the maximum number of bone influences required per vertex for this skinning method.

</dd> <dt>

*pNumBoneCombinations* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the number of bones in the bone combination table.

</dd> <dt>

*ppBoneCombinationTable* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to the bone combination table. The data is organized in a [**D3DXBONECOMBINATION**](d3dxbonecombination.md) structure.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Pointer to the new mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Each element in the remap array specifies the previous index for that position. For example, if a vertex was in position 3 but has been remapped to position 5, then the fifth element of pVertexRemap will contain 3.

This method does not run on hardware that does not support fixed-function vertex blending.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> </dl>

 

 
