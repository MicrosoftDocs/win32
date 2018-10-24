---
Description: Set vertex data into one of the mesh's vertex buffers.
ms.assetid: 930cbc49-4202-431f-ac72-386c31acd87e
title: ID3DX10Mesh::SetVertexData method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.SetVertexData
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
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

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

The vertex buffer to be filled with pData.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **const void\***

The vertex data to set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




