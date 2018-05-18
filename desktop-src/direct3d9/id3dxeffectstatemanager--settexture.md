---
Description: 'A callback function that must be implemented by a user to set a texture.'
ms.assetid: '971802f4-ea7a-4906-83b8-0cd83111716e'
title: 'ID3DXEffectStateManager::SetTexture method'
---

# ID3DXEffectStateManager::SetTexture method

A callback function that must be implemented by a user to set a texture.

## Syntax


```C++
HRESULT SetTexture(
  [in] DWORD                  Stage,
  [in] LPDIRECT3DBASETEXTURE9 pTexture
);
```



## Parameters

<dl> <dt>

*Stage* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

The stage to which the texture is assigned. This is the index value in [**IDirect3DDevice9::SetTexture**](idirect3ddevice9--settexture.md) or [**IDirect3DDevice9::SetTextureStageState**](idirect3ddevice9--settexturestagestate.md).

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](idirect3dbasetexture9.md)**

A pointer to the texture object. This can be any of the Direct3D texture types (cube, volume, etc.). See [**IDirect3DBaseTexture9**](idirect3dbasetexture9.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTexture**](idirect3ddevice9--settexture.md)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




