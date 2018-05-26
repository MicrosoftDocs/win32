---
Description: Copies per-vertex albedo values from a mesh.
ms.assetid: 3a6f1cc2-a870-4463-98df-599d9fbd9d78
title: ID3DXPRTEngineExtractPerVertexAlbedo method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTEngine::ExtractPerVertexAlbedo method

Copies per-vertex albedo values from a mesh.

## Syntax


```C++
HRESULT ExtractPerVertexAlbedo(
  [in] LPD3DXMESH   pMesh,
  [in] D3DDECLUSAGE Usage,
  [in] UINT         NumChanIn
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to the [**ID3DXMesh**](id3dxmesh.md) mesh object used in [**D3DXCreatePRTEngine**](d3dxcreateprtengine.md) to create the [**ID3DXPRTEngine**](id3dxprtengine.md) object.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**D3DDECLUSAGE**](direct3d9.d3ddeclusage)**

Vertex usage descriptions to copy from the mesh. See [**D3DDECLUSAGE**](direct3d9.d3ddeclusage).

</dd> <dt>

*NumChanIn* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of color channels to copy from the mesh. Set to 1 to specify gray materials (R = G = B), or 3 to enable color bleeding effects.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




