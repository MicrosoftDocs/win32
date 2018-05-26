---
Description: A callback function that must be implemented by a user to set a vertex shader.
ms.assetid: 8f3d3be3-c073-441d-a318-6d2cd5e7aca5
title: ID3DXEffectStateManagerSetVertexShader method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**LPDIRECT3DVERTEXSHADER9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexshader9?branch=master)**

A pointer to a vertex shader object. See [**IDirect3DVertexShader9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexshader9?branch=master).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShader**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setvertexshader?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




