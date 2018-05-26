---
Description: Performs uniform tessellation based on the tessellation level.
ms.assetid: 0fc701b4-0636-450e-b8e0-e7a490871316
title: ID3DXPatchMeshTessellate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPatchMesh::Tessellate method

Performs uniform tessellation based on the tessellation level.

## Syntax


```C++
HRESULT Tessellate(
  [in] FLOAT      fTessLevel,
  [in] LPD3DXMESH pMesh
);
```



## Parameters

<dl> <dt>

*fTessLevel* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Tessellation level. This is the number of vertices introduced between existing vertices. The range of this float parameter is 0 &lt; fTessLevel &lt;= 32.

</dd> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Resulting tessellated mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




