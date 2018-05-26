---
Description: Gets the mesh vertex buffer.
ms.assetid: 4ea4e99b-5c2c-467b-8b5d-8174c446680a
title: ID3DXPatchMeshGetVertexBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPatchMesh::GetVertexBuffer method

Gets the mesh vertex buffer.

## Syntax


```C++
HRESULT GetVertexBuffer(
  [out] LPDIRECT3DVERTEXBUFFER9 *ppVB
);
```



## Parameters

<dl> <dt>

*ppVB* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DVERTEXBUFFER9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexbuffer9?branch=master)\***

Pointer to the vertex buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method assumes uniform tessellation.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




