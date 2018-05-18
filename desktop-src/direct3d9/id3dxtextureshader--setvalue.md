---
Description: 'Sets the constant table with the data in the buffer.'
ms.assetid: '55cf5456-8f23-405d-9329-8ff737c5c139'
title: 'ID3DXTextureShader::SetValue method'
---

# ID3DXTextureShader::SetValue method

Sets the constant table with the data in the buffer.

## Syntax


```C++
HRESULT SetValue(
  [in] D3DXHANDLE hConstant,
  [in] LPCVOID    pData,
  [in] UINT       Bytes
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to a constant. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

A pointer to a buffer containing the constant data.

</dd> <dt>

*Bytes* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Size of the buffer, in bytes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




