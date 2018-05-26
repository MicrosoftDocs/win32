---
Description: Clones a mesh using a declarator.
ms.assetid: 47e0329a-ea85-478d-af8b-cf85d2a779f6
title: ID3DXBaseMeshCloneMesh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXBaseMesh::CloneMesh method

Clones a mesh using a declarator.

## Syntax


```C++
HRESULT CloneMesh(
  [in]                DWORD             Options,
  [in]          const D3DVERTEXELEMENT9 *pDeclaration,
  [in]                LPDIRECT3DDEVICE9 pDevice,
  [out, retval]       LPD3DXMESH        *ppCloneMesh
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

A combination of one or more [**D3DXMESH**](direct3d9.d3dxmesh) flags specifying creation options for the mesh.

</dd> <dt>

*pDeclaration* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

An array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements, which specify the vertex format for the vertices in the output mesh.

</dd> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device object associated with the mesh.

</dd> <dt>

*ppCloneMesh* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the cloned mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

**ID3DXBaseMesh::CloneMesh** is used to reformat and change the vertex data layout. This is done by creating a new mesh object. For example, use it to add space for normals, texture coordinates, colors, weights, etc. that were not present before.

[**ID3DXBaseMesh::UpdateSemantics**](id3dxbasemesh--updatesemantics.md) updates the vertex declaration with different semantic information without changing the layout of the vertex buffer. This method does not modify the contents of the vertex buffer. For example, use it to relabel a 3D texture coordinate as a binormal or tangent or vice versa.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> <dt>

[**ID3DXBaseMesh::CloneMeshFVF**](id3dxbasemesh--clonemeshfvf.md)
</dt> <dt>

[**D3DXDeclaratorFromFVF**](d3dxdeclaratorfromfvf.md)
</dt> </dl>

 

 




