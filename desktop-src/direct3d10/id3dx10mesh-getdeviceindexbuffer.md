---
Description: 'Access the mesh''s index buffer after it has been committed to the device with ID3DX10Mesh::CommitToDevice. This is different from ID3DX10Mesh::GetIndexBuffer, which returns the index buffer before it has been committed to the device.'
ms.assetid: '94d21f50-91b5-4f8d-ac73-7a851bba8685'
title: 'ID3DX10Mesh::GetDeviceIndexBuffer method'
---

# ID3DX10Mesh::GetDeviceIndexBuffer method

Access the mesh's index buffer after it has been committed to the device with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md). This is different from [**ID3DX10Mesh::GetIndexBuffer**](id3dx10mesh-getindexbuffer.md), which returns the index buffer before it has been committed to the device.

## Syntax


```C++
HRESULT GetDeviceIndexBuffer(
  [out] ID3D10Buffer **ppIndexBuffer
);
```



## Parameters

<dl> <dt>

*ppIndexBuffer* \[out\]
</dt> <dd>

Type: **[**ID3D10Buffer**](id3d10buffer.md)\*\***

The index buffer after it has been committed to the device.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

If the mesh's index buffer has not already been committed to the device, this API will automatically commit the index buffer before it returns a pointer to the buffer.

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

 

 




