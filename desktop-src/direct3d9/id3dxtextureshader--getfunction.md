---
Description: Gets a pointer to the function DWORD stream.
ms.assetid: a051b51a-185c-4a9e-a8b9-4096615e2634
title: ID3DXTextureShader::GetFunction method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXTextureShader::GetFunction method

Gets a pointer to the function DWORD stream.

## Syntax


```C++
HRESULT GetFunction(
  [in] LPD3DXBUFFER *ppFunction
);
```



## Parameters

<dl> <dt>

*ppFunction* \[in\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to the function DWORD stream. See [**ID3DXBuffer**](id3dxbuffer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




