---
Description: 'A callback function that must be implemented by a user to set render state.'
ms.assetid: 'a5a27e30-c141-44a4-b8d4-38c1d6076b2a'
title: 'ID3DXEffectStateManager::SetRenderState method'
---

# ID3DXEffectStateManager::SetRenderState method

A callback function that must be implemented by a user to set render state.

## Syntax


```C++
HRESULT SetRenderState(
  [in] D3DRENDERSTATETYPE State,
  [in] DWORD              Value
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Type: **[**D3DRENDERSTATETYPE**](direct3d9.d3drenderstatetype)**

The render state to set. [**D3DRENDERSTATETYPE**](direct3d9.d3drenderstatetype)

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

The render state value. See [Effect States (Direct3D 9)](effect-states.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetRenderState**](idirect3ddevice9--setrenderstate.md)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




