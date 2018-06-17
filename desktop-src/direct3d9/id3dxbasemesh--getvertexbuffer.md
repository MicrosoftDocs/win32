---
Description: Retrieves the vertex buffer associated with the mesh.
ms.assetid: 5caa6ce1-feab-4919-944e-f92fad3ad443
title: ID3DXBaseMesh::GetVertexBuffer method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**LPDIRECT3DVERTEXBUFFER9**](/windows/desktop/api)\***

Address of a pointer to an [**IDirect3DVertexBuffer9**](/windows/desktop/api) interface, representing the vertex buffer object associated with the mesh.

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

 

 




