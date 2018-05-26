---
Description: Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.
ms.assetid: f56925d8-17f7-44c5-a371-3cde41804613
title: ID3DXEffectOnLostDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXEffect::OnLostDevice method

Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.

## Syntax


```C++
HRESULT OnLostDevice();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method should be called whenever the device is lost or before the user calls [**IDirect3DDevice9::Reset**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-reset?branch=master). Even if the device was not actually lost, **ID3DXEffect::OnLostDevice** is responsible for freeing stateblocks and other resources that may need to be released before resetting the device. As a result, the font object cannot be used again before calling **IDirect3DDevice9::Reset** and then [**ID3DXEffect::OnResetDevice**](id3dxeffect--onresetdevice.md).

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 




