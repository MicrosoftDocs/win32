---
description: A callback function that must be implemented by a user to set an array of vertex shader integer constants.
ms.assetid: 55f5747d-b7f8-4d13-ac2c-df2dcb160091
title: ID3DXEffectStateManager::SetPixelShaderConstantI method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXEffectStateManager.SetPixelShaderConstantI
api_type:
- COM
api_location:
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectStateManager::SetPixelShaderConstantI method

A callback function that must be implemented by a user to set an array of vertex shader integer constants.

## Syntax


```C++
HRESULT SetPixelShaderConstantI(
  [out]       UINT StartRegister,
  [out] const INT  *pConstantData,
  [out]       UINT RegisterCount
);
```



## Parameters

<dl> <dt>

*StartRegister* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The zero-based index of the first constant register.

</dd> <dt>

*pConstantData* \[out\]
</dt> <dd>

Type: **const [**INT**](../winprog/windows-data-types.md)\***

An array of integer constants.

</dd> <dt>

*RegisterCount* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of registers in pConstantData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetPixelShaderConstantI**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstanti)) will fail.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 
