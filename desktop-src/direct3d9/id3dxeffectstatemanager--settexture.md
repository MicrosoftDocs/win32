---
Description: A callback function that must be implemented by a user to set a texture.
ms.assetid: 971802f4-ea7a-4906-83b8-0cd83111716e
title: ID3DXEffectStateManager::SetTexture method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXEffectStateManager.SetTexture
api_type:
- COM
api_location:
- D3dx9.lib
- D3dx9.dll
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

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

The stage to which the texture is assigned. This is the index value in [**IDirect3DDevice9::SetTexture**](https://msdn.microsoft.com/library/Bb174461(v=VS.85).aspx) or [**IDirect3DDevice9::SetTextureStageState**](https://msdn.microsoft.com/library/Bb174462(v=VS.85).aspx).

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](https://msdn.microsoft.com/library/Bb174322(v=VS.85).aspx)**

A pointer to the texture object. This can be any of the Direct3D texture types (cube, volume, etc.). See [**IDirect3DBaseTexture9**](https://msdn.microsoft.com/library/Bb174322(v=VS.85).aspx).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTexture**](https://msdn.microsoft.com/library/Bb174461(v=VS.85).aspx)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




