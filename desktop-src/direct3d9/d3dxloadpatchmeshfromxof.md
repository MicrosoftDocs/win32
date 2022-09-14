---
description: Loads a patch mesh from an ID3DXFileData object.
ms.assetid: 8054e33e-6bf8-4a56-9f66-30600732c84f
title: D3DXLoadPatchMeshFromXof function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXLoadPatchMeshFromXof
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXLoadPatchMeshFromXof function

Loads a patch mesh from an [**ID3DXFileData**](id3dxfiledata.md) object.

## Syntax


```C++
HRESULT D3DXLoadPatchMeshFromXof(
  _In_  LPD3DXFILEDATA    pxofMesh,
  _In_  DWORD             Options,
  _In_  LPDIRECT3DDEVICE9 pD3DDevice,
  _Out_ LPD3DXBUFFER      *ppMaterials,
  _Out_ LPD3DXBUFFER      *ppEffectInstances,
  _Out_ PDWORD            pNumMaterials,
  _Out_ LPD3DXPATCHMESH   *ppMesh
);
```



## Parameters

<dl> <dt>

*pxofMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXFILEDATA**](id3dxfiledata.md)**

Pointer to an [**ID3DXFileData**](id3dxfiledata.md) interface, representing the file data object to load.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more [**D3DXMESH**](./d3dxmesh.md) flags, specifying creation options for the mesh.

</dd> <dt>

*pD3DDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to the device that the mesh is created from.

</dd> <dt>

*ppMaterials* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Array of materials contained in the mesh. Each material is indexed by an [**ID3DXBuffer**](id3dxbuffer.md) interface.

</dd> <dt>

*ppEffectInstances* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to a buffer containing an array of effect instances, one per attribute group in the returned mesh. An effect instance is a particular instance of state information used to initialize an effect. See [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md). For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*pNumMaterials* \[out\]
</dt> <dd>

Type: **PDWORD**

Pointer that contains the number of materials in the mesh.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXPATCHMESH**](id3dxpatchmesh.md)\***

Address of a pointer to an [**ID3DXPatchMesh**](id3dxpatchmesh.md) interface, representing the loaded mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

For mesh files that do not contain effect instance information, default effect instances will be generated from the material information in the .x file. A default effect instance will have default values that correspond to the members of the [**D3DMATERIAL9**](d3dmaterial9.md) structure.

The default texture name is also filled in, but is handled differently. The name will be Texture0@Name, which corresponds to an effect variable by the name of "Texture0" with an annotation called "Name." This will contain the string file name for the texture.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXEFFECTDEFAULT**](d3dxeffectdefault.md)
</dt> <dt>

[**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md)
</dt> </dl>

 

 
