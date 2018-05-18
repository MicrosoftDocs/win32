---
Description: 'A callback function that must be implemented by a user to set an array of vertex shader floating-point constants.'
ms.assetid: 'db87ca8c-2539-4d80-854c-25b114a7e7e0'
title: 'ID3DXEffectStateManager::SetPixelShaderConstantF method'
---

# ID3DXEffectStateManager::SetPixelShaderConstantF method

A callback function that must be implemented by a user to set an array of vertex shader floating-point constants.

## Syntax


```C++
HRESULT SetPixelShaderConstantF(
  [out]       UINT  StartRegister,
  [out] const FLOAT *pConstantData,
  [out]       UINT  RegisterCount
);
```



## Parameters

<dl> <dt>

*StartRegister* \[out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The zero-based index of the first constant register.

</dd> <dt>

*pConstantData* \[out\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

An array of floating-point constants.

</dd> <dt>

*RegisterCount* \[out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of registers in pConstantData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetPixelShaderConstantF**](idirect3ddevice9--setpixelshaderconstantf.md)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




