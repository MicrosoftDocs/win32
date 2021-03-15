---
description: Retrieves albedo values of the mesh vertices.
ms.assetid: 12b8d6d1-c806-4dcd-80ac-f3963215dcf4
title: ID3DXPRTEngine::GetVertexAlbedo method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.GetVertexAlbedo
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::GetVertexAlbedo method

Retrieves albedo values of the mesh vertices.

## Syntax


```C++
HRESULT GetVertexAlbedo(
  [in, out] D3DXCOLOR *pVertColors,
  [in]      UINT      NumVerts
);
```



## Parameters

<dl> <dt>

*pVertColors* \[in, out\]
</dt> <dd>

Type: **[**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a destination array of albedo values of the mesh vertices. See [**D3DXCOLOR**](d3dxcolor.md).

</dd> <dt>

*NumVerts* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vertices in the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
