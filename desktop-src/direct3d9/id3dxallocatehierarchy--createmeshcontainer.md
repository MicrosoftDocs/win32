---
description: Requests allocation of a mesh container object.
ms.assetid: ec66b393-016b-4572-94dc-5c8903b506a3
title: ID3DXAllocateHierarchy::CreateMeshContainer method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAllocateHierarchy.CreateMeshContainer
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAllocateHierarchy::CreateMeshContainer method

Requests allocation of a mesh container object.

## Syntax


```C++
HRESULT CreateMeshContainer(
  [in]                LPCSTR              Name,
  [in]          const D3DXMESHDATA        *pMeshData,
  [in]          const D3DXMATERIAL        *pMaterials,
  [in]          const D3DXEFFECTINSTANCE  *pEffectInstances,
  [in]                DWORD               NumMaterials,
  [in]          const DWORD               *pAdjacency,
  [in]                LPD3DXSKININFO      pSkinInfo,
  [out, retval]       LPD3DXMESHCONTAINER *ppNewMeshContainer
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Name of the mesh.

</dd> <dt>

*pMeshData* \[in\]
</dt> <dd>

Type: **const [**D3DXMESHDATA**](d3dxmeshdata.md)\***

Pointer to the mesh data structure. See [**D3DXMESHDATA**](d3dxmeshdata.md).

</dd> <dt>

*pMaterials* \[in\]
</dt> <dd>

Type: **const [**D3DXMATERIAL**](d3dxmaterial.md)\***

Array of materials used in the mesh.

</dd> <dt>

*pEffectInstances* \[in\]
</dt> <dd>

Type: **const [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md)\***

Array of effect instances used in the mesh. See [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md).

</dd> <dt>

*NumMaterials* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of materials in the materials array.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Adjacency array for the mesh.

</dd> <dt>

*pSkinInfo* \[in\]
</dt> <dd>

Type: **[**LPD3DXSKININFO**](id3dxskininfo.md)**

Pointer to the skin mesh object if skin data is found. See [**ID3DXSkinInfo**](id3dxskininfo.md).

</dd> <dt>

*ppNewMeshContainer* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXMESHCONTAINER**](d3dxmeshcontainer.md)\***

Returns the created mesh container. See [**D3DXMESHCONTAINER**](d3dxmeshcontainer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from D3DERR or D3DXERR, as this will cause [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) to fail also, and return the error.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAllocateHierarchy](id3dxallocatehierarchy.md)
</dt> </dl>

 

 
