---
Description: 'Retrieves the data in an index buffer.'
ms.assetid: '8e14a047-a8a6-4763-88c7-3b439044eeb4'
title: 'ID3DXBaseMesh::GetIndexBuffer method'
---

# ID3DXBaseMesh::GetIndexBuffer method

Retrieves the data in an index buffer.

## Syntax


```C++
HRESULT GetIndexBuffer(
  [out, retval] LPDIRECT3DINDEXBUFFER9 *ppIB
);
```



## Parameters

<dl> <dt>

*ppIB* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECT3DINDEXBUFFER9**](idirect3dindexbuffer9.md)\***

Address of a pointer to an [**IDirect3DIndexBuffer9**](idirect3dindexbuffer9.md) interface, representing the index buffer object associated with the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




