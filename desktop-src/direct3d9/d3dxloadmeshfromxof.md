---
description: Loads a mesh from an ID3DXFileData object.
ms.assetid: 3fcf6a91-fcd4-46da-8278-13bda8af8274
title: D3DXLoadMeshFromXof function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXLoadMeshFromXof
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXLoadMeshFromXof function

Loads a mesh from an [**ID3DXFileData**](id3dxfiledata.md) object.

## Syntax


```C++
HRESULT D3DXLoadMeshFromXof(
  _In_    LPD3DXFILEDATA    pxofMesh,
  _Out_   DWORD             Options,
  _In_    LPDIRECT3DDEVICE9 pDevice,
  _Out_   LPD3DXBUFFER      *ppAdjacency,
  _Inout_ LPD3DXBUFFER      *ppMaterials,
  _Out_   LPD3DXBUFFER      *ppEffectInstances,
  _Inout_ DWORD             *pNumMaterials,
  _Out_   LPD3DXMESH        *ppMesh
);
```



## Parameters

<dl> <dt>

*pxofMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXFILEDATA**](id3dxfiledata.md)**

Pointer to an [**ID3DXFileData**](id3dxfiledata.md) interface, representing the file data object to load.

</dd> <dt>

*Options* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more flags from the [**D3DXMESH**](./d3dxmesh.md) enumeration, specifying creation options for the mesh.

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface, the device object associated with the mesh.

</dd> <dt>

*ppAdjacency* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to a buffer that contains adjacency data. The adjacency data contains an array of three DWORDs per face that specify the three neighbors for each face in the mesh. For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*ppMaterials* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface. When the method returns, this parameter is filled with an array of [**D3DXMATERIAL**](d3dxmaterial.md) structures.

</dd> <dt>

*ppEffectInstances* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to a buffer containing an array of effect instances, one per attribute group in the returned mesh. An effect instance is a particular instance of state information used to initialize an effect. See [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md). For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*pNumMaterials* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the number of [**D3DXMATERIAL**](d3dxmaterial.md) structures in the *ppMaterials* array, when the method returns.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the loaded mesh.

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

 

 
