---
Description: 'Gets a pixel shader.'
ms.assetid: '173a20a5-dda0-493f-a161-2dc2881e71f2'
title: 'ID3DXBaseEffect::GetPixelShader method'
---

# ID3DXBaseEffect::GetPixelShader method

Gets a pixel shader.

## Syntax


```C++
HRESULT GetPixelShader(
  [in]  D3DXHANDLE             hParameter,
  [out] LPDIRECT3DPIXELSHADER9 *ppPShader
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*ppPShader* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DPIXELSHADER9**](idirect3dpixelshader9.md)\***

Returns a pixel shader object. See [**IDirect3DPixelShader9**](idirect3dpixelshader9.md) object.

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

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




