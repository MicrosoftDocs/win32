---
description: Concatenates a group of meshes into one common mesh. This method can optionally apply a matrix transformation to each input mesh and its texture coordinates.
ms.assetid: 0f2af63a-ece5-4c99-8cb8-045099eca3ea
title: D3DXConcatenateMeshes function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXConcatenateMeshes
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXConcatenateMeshes function

Concatenates a group of meshes into one common mesh. This method can optionally apply a matrix transformation to each input mesh and its texture coordinates.

## Syntax


```C++
HRESULT D3DXConcatenateMeshes(
  _In_        LPD3DXMESH        *ppMeshes,
  _In_        UINT              NumMeshes,
  _In_        DWORD             Options,
  _In_  const D3DXMATRIX        *pGeomXForms,
  _In_  const D3DXMATRIX        *pTextureXForms,
  _In_  const D3DVERTEXELEMENT9 *pDecl,
  _In_        LPDIRECT3DDEVICE9 pD3DDevice,
  _Out_       LPD3DXMESH        *ppMeshOut
);
```



## Parameters

<dl> <dt>

*ppMeshes* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Array of input mesh pointers (see [**ID3DXMesh**](id3dxmesh.md)). The number of elements in the array is NumMeshes.

</dd> <dt>

*NumMeshes* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of input meshes to concatenate.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Mesh creation options; this is a combination of one or more [**D3DXMESH**](./d3dxmesh.md) flags. The mesh creation options are equivalent to the options parameter required by [**D3DXCreateMesh**](d3dxcreatemesh.md).

</dd> <dt>

*pGeomXForms* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Optional array of geometry transforms. The number of elements in the array is NumMeshes; each element is a transformation matrix (see [**D3DXMATRIX**](d3dxmatrix.md)). May be **NULL**.

</dd> <dt>

*pTextureXForms* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Optional array of texture transforms. The number of elements in the array is NumMeshes; each element is a transformation matrix (see [**D3DXMATRIX**](d3dxmatrix.md)). This parameter may be **NULL**.

</dd> <dt>

*pDecl* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Optional pointer to a vertex declaration (see [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)). This parameter may be **NULL**.

</dd> <dt>

*pD3DDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to a [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) device that is used to create the new mesh.

</dd> <dt>

*ppMeshOut* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to the mesh created (see [**ID3DXMesh**](id3dxmesh.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of these: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

If no [vertex declaration](vertex-declaration.md) is given as part of the Options mesh creation parameter, the method will generate a union of all of the vertex declarations of the submeshes, promoting channels and types if necessary. The method will create an attribute table from attribute tables of the input meshes. To ensure creation of an attribute table, call [**Optimize**](id3dxmesh--optimize.md) with Flags set to D3DXMESHOPT\_COMPACT and D3DXMESHOPT\_ATTRSORT (see [**D3DXMESHOPT**](./d3dxmeshopt.md)).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
