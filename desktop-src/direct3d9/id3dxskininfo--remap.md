---
description: Updates bone influence information to match vertices after they are reordered. This method should be called if the target vertex buffer has been reordered externally.
ms.assetid: bff5229f-e547-4ab3-84c6-58b15a7825e9
title: ID3DXSkinInfo::Remap method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo.Remap
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::Remap method

Updates bone influence information to match vertices after they are reordered. This method should be called if the target vertex buffer has been reordered externally.

## Syntax


```C++
HRESULT Remap(
  [in] DWORD NumVertices,
  [in] DWORD *pVertexRemap
);
```



## Parameters

<dl> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of vertices to remap.

</dd> <dt>

*pVertexRemap* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Array of DWORDS whose length is specified by NumVertices.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Each element in pVertexRemap specifies the previous vertex index for that position. For example, if a vertex was in position 3 but has been remapped to position 5, then the fifth element of pVertexRemap should contain 3. The vertex remap array returned by [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) can be used.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> </dl>

 

 
