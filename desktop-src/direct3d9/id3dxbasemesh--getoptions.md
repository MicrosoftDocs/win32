---
description: Retrieves the mesh options enabled for this mesh at creation time.
ms.assetid: 4be990d7-77ab-4273-b852-e6283a89ac6c
title: ID3DXBaseMesh::GetOptions method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseMesh.GetOptions
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseMesh::GetOptions method

Retrieves the mesh options enabled for this mesh at creation time.

## Syntax


```C++
DWORD GetOptions();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Returns a combination of one or more of the following flags, indicating the options enabled for this mesh at creation time.



| Value                   | Description                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DXMESH\_32BIT         | Use 32-bit indices.                                                                                                                                                                              |
| D3DXMESH\_DONOTCLIP     | Use the D3DUSAGE\_DONOTCLIP usage flag for vertex and index buffers.                                                                                                                             |
| D3DXMESH\_DYNAMIC       | Equivalent to specifying both D3DXMESH\_VB\_DYNAMIC and D3DXMESH\_IB\_DYNAMIC.                                                                                                                   |
| D3DXMESH\_RTPATCHES     | Use the D3DUSAGE\_RTPATCHES usage flag for vertex and index buffers.                                                                                                                             |
| D3DXMESH\_NPATCHES      | Specifying this flag causes the vertex and index buffer of the mesh to be created with D3DUSAGE\_NPATCHES flag. This is required if the mesh object is to be rendered using N-Patch enhancement. |
| D3DXMESH\_MANAGED       | Equivalent to specifying both D3DXMESH\_VB\_MANAGED and D3DXMESH\_IB\_MANAGED.                                                                                                                   |
| D3DXMESH\_POINTS        | Use the D3DUSAGE\_POINTS usage flag for vertex and index buffers.                                                                                                                                |
| D3DXMESH\_IB\_DYNAMIC   | Use the D3DUSAGE\_DYNAMIC usage flag for index buffers.                                                                                                                                          |
| D3DXMESH\_IB\_MANAGED   | Use the D3DPOOL\_MANAGED memory class for index buffers.                                                                                                                                         |
| D3DXMESH\_IB\_SYSTEMMEM | Use the D3DPOOL\_SYSTEMMEM memory class for index buffers.                                                                                                                                       |
| D3DXMESH\_IB\_WRITEONLY | Use the D3DUSAGE\_WRITEONLY usage flag for index buffers.                                                                                                                                        |
| D3DXMESH\_SYSTEMMEM     | Equivalent to specifying both D3DXMESH\_VB\_SYSTEMMEM and D3DXMESH\_IB\_SYSTEMMEM.                                                                                                               |
| D3DXMESH\_VB\_DYNAMIC   | Use the D3DUSAGE\_DYNAMIC usage flag for vertex buffers.                                                                                                                                         |
| D3DXMESH\_VB\_MANAGED   | Use the D3DPOOL\_MANAGED memory class for vertex buffers.                                                                                                                                        |
| D3DXMESH\_VB\_SYSTEMMEM | Use the D3DPOOL\_SYSTEMMEM memory class for vertex buffers.                                                                                                                                      |
| D3DXMESH\_VB\_WRITEONLY | Use the D3DUSAGE\_WRITEONLY usage flag for vertex buffers.                                                                                                                                       |
| D3DXMESH\_WRITEONLY     | Equivalent to specifying both D3DXMESH\_VB\_WRITEONLY and D3DXMESH\_IB\_WRITEONLY.                                                                                                               |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 
