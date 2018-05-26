---
Description: A callback function that must be implemented by a user to set an array of vertex shader Boolean constants.
ms.assetid: 25fd0c68-11b5-4401-a2f8-86075ba3fa54
title: ID3DXEffectStateManagerSetVertexShaderConstantB method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXEffectStateManager::SetVertexShaderConstantB method

A callback function that must be implemented by a user to set an array of vertex shader Boolean constants.

## Syntax


```C++
HRESULT SetVertexShaderConstantB(
  [out]       UINT StartRegister,
  [out] const BOOL *pConstantData,
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

Type: **const [**BOOL**](winprog.windows_data_types)\***

An array of Boolean constants.

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
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShaderConstantB**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setvertexshaderconstantb?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




