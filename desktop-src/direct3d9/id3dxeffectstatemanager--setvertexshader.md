---
Description: 'A callback function that must be implemented by a user to set a vertex shader.'
ms.assetid: '8f3d3be3-c073-441d-a318-6d2cd5e7aca5'
title: 'ID3DXEffectStateManager::SetVertexShader method'
---

# ID3DXEffectStateManager::SetVertexShader method

A callback function that must be implemented by a user to set a vertex shader.

## Syntax


```C++
HRESULT SetVertexShader(
  [in] LPDIRECT3DVERTEXSHADER9 pShader
);
```



## Parameters

<dl> <dt>

*pShader* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVERTEXSHADER9**](idirect3dvertexshader9.md)**

A pointer to a vertex shader object. See [**IDirect3DVertexShader9**](idirect3dvertexshader9.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShader**](idirect3ddevice9--setvertexshader.md)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




