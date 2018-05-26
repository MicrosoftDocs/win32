---
Description: Changes the number of samples contained in the buffer.
ms.assetid: c3cceba8-0bbc-46e5-95d9-cdf58d8a2510
title: ID3DXPRTBufferResize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTBuffer::Resize method

Changes the number of samples contained in the buffer.

## Syntax


```C++
HRESULT Resize(
  [in] UINT NewSize
);
```



## Parameters

<dl> <dt>

*NewSize* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of samples to be contained in the buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the following value will be returned, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 




