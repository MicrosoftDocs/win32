---
Description: Adds another buffer to the ID3DXPRTBuffer and stores the results in ID3DXPRTBuffer.
ms.assetid: 345412f4-30c5-4c1d-b0ef-6e3e18c4e5ab
title: ID3DXPRTBufferAddBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTBuffer::AddBuffer method

Adds another buffer to the [**ID3DXPRTBuffer**](id3dxprtbuffer.md) and stores the results in **ID3DXPRTBuffer**.

## Syntax


```C++
HRESULT AddBuffer(
  [in] LPD3DXPRTBUFFER pBuffer
);
```



## Parameters

<dl> <dt>

*pBuffer* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to a buffer that contains members to be added to the respective members of the [**ID3DXPRTBuffer**](id3dxprtbuffer.md) buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Remarks

pBuffer and [**ID3DXPRTBuffer**](id3dxprtbuffer.md) must have the same number of samples, coefficients, and color channels; the method will fail otherwise.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 




