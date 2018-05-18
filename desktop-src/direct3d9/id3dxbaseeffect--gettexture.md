---
Description: 'Gets a texture.'
ms.assetid: 'e009ccc2-4491-4976-9460-7478b2bd34c2'
title: 'ID3DXBaseEffect::GetTexture method'
---

# ID3DXBaseEffect::GetTexture method

Gets a texture.

## Syntax


```C++
HRESULT GetTexture(
  [in]  D3DXHANDLE             hParameter,
  [out] LPDIRECT3DBASETEXTURE9 *ppTexture
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](idirect3dbasetexture9.md)\***

Returns a texture object. See [**IDirect3DBaseTexture9**](idirect3dbasetexture9.md).

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
</dt> <dt>

[**SetTexture**](id3dxbaseeffect--settexture.md)
</dt> </dl>

 

 




