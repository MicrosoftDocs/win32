---
description: Sets the attribute table for a mesh and the number of entries stored in the table.
ms.assetid: 22d46708-cffd-48da-bdad-8a43f9076356
title: ID3DXMesh::SetAttributeTable method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMesh.SetAttributeTable
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMesh::SetAttributeTable method

Sets the attribute table for a mesh and the number of entries stored in the table.

## Syntax


```C++
HRESULT SetAttributeTable(
  [in] const D3DXATTRIBUTERANGE *pAttribTable,
  [in]       DWORD              cAttribTableSize
);
```



## Parameters

<dl> <dt>

*pAttribTable* \[in\]
</dt> <dd>

Type: **const [**D3DXATTRIBUTERANGE**](d3dxattributerange.md)\***

Pointer to an array of [**D3DXATTRIBUTERANGE**](d3dxattributerange.md) structures, representing the entries in the mesh attribute table.

</dd> <dt>

*cAttribTableSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of attributes in the mesh attribute table.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

If an application keeps track of the information in an attribute table, and rearranges the table as a result of changes to attributes or faces, this method allows the application to update the attribute tables instead of calling [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) again.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMesh](id3dxmesh.md)
</dt> <dt>

[**ID3DXMesh::LockAttributeBuffer**](id3dxmesh--lockattributebuffer.md)
</dt> <dt>

**ID3DXMesh::LockAttributeBuffer**
</dt> </dl>

 

 
