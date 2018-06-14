---
Description: A callback function that must be implemented by a user to set a pixel shader.
ms.assetid: 4124eff2-1d88-429c-b7ed-8d87155b5ddc
title: ID3DXEffectStateManager::SetPixelShader method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**LPDIRECT3DPIXELSHADER9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dpixelshader9)**

A pointer to a pixel shader object. See [**IDirect3DPixelShader9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dpixelshader9).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetPixelShader**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-setpixelshader)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




