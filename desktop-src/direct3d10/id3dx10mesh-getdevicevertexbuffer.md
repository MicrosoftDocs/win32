---
Description: 'Access the mesh''s vertex buffer after it has been committed to the device with ID3DX10Mesh::CommitToDevice. This is different from ID3DX10Mesh::GetVertexBuffer, which returns the vertex buffer before it has been committed to the device.'
ms.assetid: '621d9105-e55d-47b8-8557-8adb7db19d66'
title: 'ID3DX10Mesh::GetDeviceVertexBuffer method'
---

# ID3DX10Mesh::GetDeviceVertexBuffer method

Access the mesh's vertex buffer after it has been committed to the device with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md). This is different from [**ID3DX10Mesh::GetVertexBuffer**](id3dx10mesh-getvertexbuffer.md), which returns the vertex buffer before it has been committed to the device.

## Syntax


```C++
HRESULT GetDeviceVertexBuffer(
  [in]  UINT         iBuffer,
  [out] ID3D10Buffer **ppVertexBuffer
);
```



## Parameters

<dl> <dt>

*iBuffer* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

An index identifying which vertex buffer to access.

</dd> <dt>

*ppVertexBuffer* \[out\]
</dt> <dd>

Type: **[**ID3D10Buffer**](id3d10buffer.md)\*\***

The vertex buffer after it has been committed to the device.

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

 

 




