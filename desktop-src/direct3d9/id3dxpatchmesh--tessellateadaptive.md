---
Description: Performs adaptive tessellation based on the z-based adaptive tessellation criterion.
ms.assetid: 9f8f5c18-e866-4893-ba07-2a3c0d26c028
title: ID3DXPatchMesh::TessellateAdaptive method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPatchMesh::TessellateAdaptive method

Performs adaptive tessellation based on the z-based adaptive tessellation criterion.

## Syntax


```C++
HRESULT TessellateAdaptive(
  [in] const D3DXVECTOR4 *pTrans,
  [in]       DWORD       dwMaxTessLevel,
  [in]       DWORD       dwMinTessLevel,
  [in]       LPD3DXMESH  pMesh
);
```



## Parameters

<dl> <dt>

*pTrans* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Specifies a 4D vector that is dotted with the vertices to get the per-vertex adaptive tessellation amount. Each edge is tessellated to the average value of the tessellation levels for the two vertices it connects.

</dd> <dt>

*dwMaxTessLevel* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Maximum limit for adaptive tessellation. This is the number of vertices introduced between existing vertices. This integer value can range from 1 to 32, inclusive.

</dd> <dt>

*dwMinTessLevel* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Minimum limit for adaptive tessellation. This is the number of vertices introduced between existing vertices. This integer value can range from 1 to 32, inclusive.

</dd> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Resulting tessellated mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This function will perform more efficiently if the patch mesh has been optimized using [**ID3DXPatchMesh::Optimize**](id3dxpatchmesh--optimize.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




