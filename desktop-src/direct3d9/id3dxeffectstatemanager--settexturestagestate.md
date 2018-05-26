---
Description: A callback function that must be implemented by a user to set the texture stage state.
ms.assetid: cc86a483-ccf0-400d-b14d-ab55a3cf4b98
title: ID3DXEffectStateManagerSetTextureStageState method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**DWORD**](winprog.windows_data_types)**

The stage that the texture is assigned to. This is the index value in [**IDirect3DDevice9::SetTexture**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-settexture?branch=master) or [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-settexturestagestate?branch=master).

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type: **[**D3DTEXTURESTAGESTATETYPE**](direct3d9.d3dtexturestagestatetype)**

Defines the type of operation that a texture stage will perform. See [**D3DTEXTURESTAGESTATETYPE**](direct3d9.d3dtexturestagestatetype).

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Can be either an operation ([**D3DTEXTUREOP**](direct3d9.d3dtextureop)) or an argument value ([D3DTA](d3dta.md)), depending on what is chosen for Type.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-settexturestagestate?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




