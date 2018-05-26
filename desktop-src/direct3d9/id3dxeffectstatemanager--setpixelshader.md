---
Description: A callback function that must be implemented by a user to set a pixel shader.
ms.assetid: 4124eff2-1d88-429c-b7ed-8d87155b5ddc
title: ID3DXEffectStateManagerSetPixelShader method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXEffectStateManager::SetPixelShader method

A callback function that must be implemented by a user to set a pixel shader.

## Syntax


```C++
HRESULT SetPixelShader(
  [in] LPDIRECT3DPIXELSHADER9 pShader
);
```



## Parameters

<dl> <dt>

*pShader* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DPIXELSHADER9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dpixelshader9?branch=master)**

A pointer to a pixel shader object. See [**IDirect3DPixelShader9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dpixelshader9?branch=master).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetPixelShader**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setpixelshader?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




