---
description: A callback function that must be implemented by a user to set an array of vertex shader Boolean constants.
ms.assetid: 25fd0c68-11b5-4401-a2f8-86075ba3fa54
title: ID3DXEffectStateManager::SetVertexShaderConstantB method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXEffectStateManager.SetVertexShaderConstantB
api_type:
- COM
api_location:
- D3dx9.lib
- D3dx9.dll
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

Type: **[**UINT**](../winprog/windows-data-types.md)**

The zero-based index of the first constant register.

</dd> <dt>

*pConstantData* \[out\]
</dt> <dd>

Type: **const [**BOOL**](../winprog/windows-data-types.md)\***

An array of Boolean constants.

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
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetVertexShaderConstantB**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstantb)) will fail.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 
