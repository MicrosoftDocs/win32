---
Description: A callback function that must be implemented by a user to set the number of subdivision segments for N-patches.
ms.assetid: f94910ee-3385-44d3-b4f1-a0e88c7afa39
title: ID3DXEffectStateManagerSetNPatchMode method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXEffectStateManager::SetNPatchMode method

A callback function that must be implemented by a user to set the number of subdivision segments for N-patches.

## Syntax


```C++
HRESULT SetNPatchMode(
  [in] FLOAT nSegments
);
```



## Parameters

<dl> <dt>

*nSegments* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Break the surface into this number of subdivisions. This is the same as the number used by [**IDirect3DDevice9::SetNPatchMode**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setnpatchmode?branch=master).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetNPatchMode**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setnpatchmode?branch=master)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




