---
Description: 'Access the mesh''s adjacency buffer.'
ms.assetid: '42b13f14-4edf-4b56-9198-60a548855542'
title: 'ID3DX10Mesh::GetAdjacencyBuffer method'
---

# ID3DX10Mesh::GetAdjacencyBuffer method

Access the mesh's adjacency buffer.

## Syntax


```C++
HRESULT GetAdjacencyBuffer(
  [out] ID3DX10MeshBuffer **ppAdjacency
);
```



## Parameters

<dl> <dt>

*ppAdjacency* \[out\]
</dt> <dd>

Type: **[**ID3DX10MeshBuffer**](id3dx10meshbuffer.md)\*\***

The adjacency buffer. See [**ID3DX10MeshBuffer**](id3dx10meshbuffer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




