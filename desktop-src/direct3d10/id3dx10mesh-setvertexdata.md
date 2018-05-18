---
Description: 'Set vertex data into one of the mesh''s vertex buffers.'
ms.assetid: '930cbc49-4202-431f-ac72-386c31acd87e'
title: 'ID3DX10Mesh::SetVertexData method'
---

# ID3DX10Mesh::SetVertexData method

Set vertex data into one of the mesh's vertex buffers.

## Syntax


```C++
HRESULT SetVertexData(
  [in]       UINT iBuffer,
  [in] const void *pData
);
```



## Parameters

<dl> <dt>

*iBuffer* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The vertex buffer to be filled with pData.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **const void\***

The vertex data to set.

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

 

 




