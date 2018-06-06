---
Description: Retrieves either an attribute table for a mesh, or the number of entries stored in an attribute table for a mesh.
ms.assetid: 15b24137-0ff9-4299-971b-90fa4ef2686d
title: ID3DXBaseMesh::GetAttributeTable method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXBaseMesh::GetAttributeTable method

Retrieves either an attribute table for a mesh, or the number of entries stored in an attribute table for a mesh.

## Syntax


```C++
HRESULT GetAttributeTable(
  [in, out] D3DXATTRIBUTERANGE *pAttribTable,
  [in, out] DWORD              *pAttribTableSize
);
```



## Parameters

<dl> <dt>

*pAttribTable* \[in, out\]
</dt> <dd>

Type: **[**D3DXATTRIBUTERANGE**](d3dxattributerange.md)\***

Pointer to an array of [**D3DXATTRIBUTERANGE**](d3dxattributerange.md) structures, representing the entries in the mesh's attribute table. Specify **NULL** to retrieve the value for pAttribTableSize.

</dd> <dt>

*pAttribTableSize* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to either the number of entries stored in pAttribTable or a value to be filled in with the number of entries stored in the attribute table for the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

An attribute table is created by [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) and passing D3DXMESHOPT\_ATTRSORT for the Flags parameter.

An attribute table is used to identify areas of the mesh that need to be drawn with different textures, render states, materials, and so on. In addition, the application can use the attribute table to hide portions of a mesh by not drawing a given attribute identifier when drawing the frame.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




