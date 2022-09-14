---
description: Gets a pointer to the function DWORD stream.
ms.assetid: a051b51a-185c-4a9e-a8b9-4096615e2634
title: ID3DXTextureShader::GetFunction method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureShader.GetFunction
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
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

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




