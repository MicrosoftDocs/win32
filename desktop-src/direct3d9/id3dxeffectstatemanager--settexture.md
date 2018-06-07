---
Description: A callback function that must be implemented by a user to set a texture.
ms.assetid: 971802f4-ea7a-4906-83b8-0cd83111716e
title: ID3DXEffectStateManager::SetTexture method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The stage to which the texture is assigned. This is the index value in [**IDirect3DDevice9::SetTexture**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexture) or [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexturestagestate).

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dbasetexture9)**

A pointer to the texture object. This can be any of the Direct3D texture types (cube, volume, etc.). See [**IDirect3DBaseTexture9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dbasetexture9).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTexture**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexture)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




