---
Description: A callback function that must be implemented by a user to set the texture stage state.
ms.assetid: cc86a483-ccf0-400d-b14d-ab55a3cf4b98
title: ID3DXEffectStateManager::SetTextureStageState method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXEffectStateManager::SetTextureStageState method

A callback function that must be implemented by a user to set the texture stage state.

## Syntax


```C++
HRESULT SetTextureStageState(
  [in] DWORD                    Stage,
  [in] D3DTEXTURESTAGESTATETYPE Type,
  [in] DWORD                    Value
);
```



## Parameters

<dl> <dt>

*Stage* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The stage that the texture is assigned to. This is the index value in [**IDirect3DDevice9::SetTexture**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexture) or [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexturestagestate).

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type: **[**D3DTEXTURESTAGESTATETYPE**](https://msdn.microsoft.com/windows/desktop/87a5a1bb-e748-4c72-8320-ea82250dcc0e)**

Defines the type of operation that a texture stage will perform. See [**D3DTEXTURESTAGESTATETYPE**](https://msdn.microsoft.com/windows/desktop/87a5a1bb-e748-4c72-8320-ea82250dcc0e).

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Can be either an operation ([**D3DTEXTUREOP**](https://msdn.microsoft.com/windows/desktop/7bfdcb15-c3c3-4e7e-b924-6ecfa350e2f3)) or an argument value ([D3DTA](d3dta.md)), depending on what is chosen for Type.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settexturestagestate)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




