---
Description: A callback function that must be implemented by a user to set a vertex shader.
ms.assetid: 8f3d3be3-c073-441d-a318-6d2cd5e7aca5
title: ID3DXEffectStateManager::SetVertexShader method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXEffectStateManager.SetVertexShader
api_type:
- COM
api_location:
- D3dx9.lib
- D3dx9.dll
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

Type: **[**LPDIRECT3DVERTEXSHADER9**](https://msdn.microsoft.com/library/Bb205922(v=VS.85).aspx)**

A pointer to a vertex shader object. See [**IDirect3DVertexShader9**](https://msdn.microsoft.com/library/Bb205922(v=VS.85).aspx).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShader**](https://msdn.microsoft.com/library/Bb174465(v=VS.85).aspx)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




