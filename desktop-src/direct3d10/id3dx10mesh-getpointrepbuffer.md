---
Description: 'Get the mesh''s point rep buffer.'
ms.assetid: '4be7bee5-15ea-496f-83c2-a3a9bafd97c6'
title: 'ID3DX10Mesh::GetPointRepBuffer method'
---

# ID3DX10Mesh::GetPointRepBuffer method

Get the mesh's point rep buffer.

## Syntax


```C++
HRESULT GetPointRepBuffer(
  [out] ID3DX10MeshBuffer **ppPointReps
);
```



## Parameters

<dl> <dt>

*ppPointReps* \[out\]
</dt> <dd>

Type: **[**ID3DX10MeshBuffer**](id3dx10meshbuffer.md)\*\***

Pointer to a mesh buffer containing the mesh's point rep data. See [**ID3DX10MeshBuffer**](id3dx10meshbuffer.md).

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

 

 




