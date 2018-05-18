---
Description: 'Creates a buffer object.'
ms.assetid: '6f44fe84-3e0b-4fb8-821a-c997944fed37'
title: D3DXCreateBuffer function
---

# D3DXCreateBuffer function

Creates a buffer object.

## Syntax


```C++
HRESULT D3DXCreateBuffer(
  _In_  DWORD        NumBytes,
  _Out_ LPD3DXBUFFER *ppBuffer
);
```



## Parameters

<dl> <dt>

*NumBytes* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Size of the buffer to create, in bytes.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface, representing the created buffer object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](dx9-graphics-reference-d3dx-functions-general-purpose.md)
</dt> </dl>

 

 




