---
Description: 'Unlock the vertex buffer.'
ms.assetid: '98b82fd1-56e8-45f3-bf26-a1e3b54c2979'
title: 'ID3DXPatchMesh::UnlockVertexBuffer method'
---

# ID3DXPatchMesh::UnlockVertexBuffer method

Unlock the vertex buffer.

## Syntax


```C++
HRESULT UnlockVertexBuffer();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

The vertex buffer is usually locked, written to, and then unlocked for reading.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




