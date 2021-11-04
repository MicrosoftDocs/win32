---
description: D3DXSHPRTCompSuperCluster function - Used with compressed results of the vertex version of the precomputed radiance transfer (PRT) simulator.
ms.assetid: 0ec28b8c-5010-48a4-8e45-d7f9aa08185f
title: D3DXSHPRTCompSuperCluster function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHPRTCompSuperCluster
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSHPRTCompSuperCluster function

Used with compressed results of the vertex version of the precomputed radiance transfer (PRT) simulator. Generates "superclusters," which are groups of clusters that can be drawn in the same draw call. A greedy algorithm that minimizes overdraw is used to group the clusters.

## Syntax


```C++
HRESULT D3DXSHPRTCompSuperCluster(
  _In_    UINT       *pClusterIDs,
  _In_    LPD3DXMESH pScene,
  _In_    UINT       MaxNumClusters,
  _In_    UINT       NumClusters,
  _Inout_ UINT       *pSClusterIDs,
  _Inout_ UINT       *pNumSCs
);
```



## Parameters

<dl> <dt>

*pClusterIDs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to a NumVerts cluster IDs (extracted from a compressed buffer.)

</dd> <dt>

*pScene* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to a mesh that represents composite scene passed to the simulator. See [**ID3DXMesh**](id3dxmesh.md).

</dd> <dt>

*MaxNumClusters* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Maximum number of clusters allocated per super cluster.

</dd> <dt>

*NumClusters* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of clusters computed in the simulator.

</dd> <dt>

*pSClusterIDs* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to an array of length *NumClusters*. Contains the index of the super cluster to which the corresponding cluster was assigned.

</dd> <dt>

*pNumSCs* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Number of super clusters allocated.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 
