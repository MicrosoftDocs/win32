---
Description: Retrieves the vertex buffer associated with the mesh.
ms.assetid: 5caa6ce1-feab-4919-944e-f92fad3ad443
title: ID3DXBaseMesh::GetVertexBuffer method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXBaseMesh.GetVertexBuffer
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseMesh::GetVertexBuffer method

Retrieves the vertex buffer associated with the mesh.

## Syntax


```C++
HRESULT GetVertexBuffer(
  [out, retval] LPDIRECT3DVERTEXBUFFER9 *ppVB
);
```



## Parameters

<dl> <dt>

*ppVB* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECT3DVERTEXBUFFER9**](https://msdn.microsoft.com/library/Bb205915(v=VS.85).aspx)\***

Address of a pointer to an [**IDirect3DVertexBuffer9**](https://msdn.microsoft.com/library/Bb205915(v=VS.85).aspx) interface, representing the vertex buffer object associated with the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




