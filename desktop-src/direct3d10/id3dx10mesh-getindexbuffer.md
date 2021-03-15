---
description: Retrieves the data in an index buffer.
ms.assetid: 7e25ad67-7f9d-4c23-a029-a2262034ef38
title: ID3DX10Mesh::GetIndexBuffer method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.GetIndexBuffer
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::GetIndexBuffer method

Retrieves the data in an index buffer.

## Syntax


```C++
HRESULT GetIndexBuffer(
  [out] ID3DX10MeshBuffer **ppIndexBuffer
);
```



## Parameters

<dl> <dt>

*ppIndexBuffer* \[out\]
</dt> <dd>

Type: **[**ID3DX10MeshBuffer**](id3dx10meshbuffer.md)\*\***

Address of a pointer to a ID3DX10MeshBuffer interface, representing the index buffer associated with the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




