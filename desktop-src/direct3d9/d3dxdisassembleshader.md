---
Description: 'Disassemble a shader.'
ms.assetid: '30159223-8f88-4929-8ef1-7a6acc13f485'
title: D3DXDisassembleShader function
---

# D3DXDisassembleShader function

Disassemble a shader.

> [!Note]  
> Instead of using this legacy function, we recommend that you use the [**D3DDisassemble**](direct3dhlsl.d3ddisassemble) API.

 

## Syntax


```C++
HRESULT D3DXDisassembleShader(
  _In_  const DWORD        *pShader,
  _In_        BOOL         EnableColorCode,
  _In_        LPCSTR       pComments,
  _Out_       LPD3DXBUFFER *ppDisassembly
);
```



## Parameters

<dl> <dt>

*pShader* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to a memory buffer that contains the shader data.

</dd> <dt>

*EnableColorCode* \[in\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

Enable color code to make it easier to read the disassembly.

</dd> <dt>

*pComments* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

An optional NULL-terminated comment string. This value may be **NULL**.

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing the disassembled shader. See [**ID3DXBuffer**](id3dxbuffer.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 




