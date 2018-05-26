---
Description: A callback function that must be implemented by a user to set a FVF code.
ms.assetid: 701a4333-a71e-4d84-a06c-1c86312ee4ff
title: ID3DXEffectStateManagerSetFVF method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXEffectStateManager::SetFVF method

A callback function that must be implemented by a user to set a FVF code.

## Syntax


```C++
HRESULT SetFVF(
  [in] DWORD FVF
);
```



## Parameters

<dl> <dt>

*FVF* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

The FVF constant, that determines how to interpret vertex data. See [D3DFVF](d3dfvf.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetFVF**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setfvf?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




