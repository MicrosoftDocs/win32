---
Description: 'Sets a BOOL value.'
ms.assetid: '0d3c1f3a-f497-4e92-81e9-8647006910e1'
title: 'ID3DXTextureShader::SetBool method'
---

# ID3DXTextureShader::SetBool method

Sets a BOOL value.

## Syntax


```C++
HRESULT SetBool(
  [in] D3DXHANDLE hConstant,
  [in] BOOL       b
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the constant. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*b* \[in\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

BOOL value.

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

 

 




