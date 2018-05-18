---
Description: 'Sets a floating-point number.'
ms.assetid: '69bb9b15-5d66-4b1a-9559-29bcb38a965f'
title: 'ID3DXTextureShader::SetFloat method'
---

# ID3DXTextureShader::SetFloat method

Sets a floating-point number.

## Syntax


```C++
HRESULT SetFloat(
  [in] D3DXHANDLE hConstant,
  [in] FLOAT      f
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the constant. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*f* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Floating-point number.

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

 

 




