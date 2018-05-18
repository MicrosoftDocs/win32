---
Description: 'A callback function that must be implemented by a user to set an array of vertex shader integer constants.'
ms.assetid: '0035c97a-1b17-4665-9032-7b3b9a9d2cff'
title: 'ID3DXEffectStateManager::SetVertexShaderConstantI method'
---

# ID3DXEffectStateManager::SetVertexShaderConstantI method

A callback function that must be implemented by a user to set an array of vertex shader integer constants.

## Syntax


```C++
HRESULT SetVertexShaderConstantI(
  [out]       UINT StartRegister,
  [out] const INT  *pConstantData,
  [out]       UINT RegisterCount
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

Type: **const [**INT**](winprog.windows_data_types)\***

An array of integer constants.

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
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShaderConstantI**](idirect3ddevice9--setvertexshaderconstanti.md)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




