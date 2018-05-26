---
Description: Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.
ms.assetid: a5c82a58-10f9-44bd-a42f-555867b2c857
title: ID3DXLineOnLostDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXLine::OnLostDevice method

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

This method should be called whenever the device is lost or before the user calls [**IDirect3DDevice9::Reset**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-reset?branch=master). Even if the device was not actually lost, **ID3DXLine::OnLostDevice** is responsible for freeing stateblocks and other resources that may need to be released before resetting the device. As a result, the font object cannot be used again before calling **IDirect3DDevice9::Reset** and then [**ID3DXLine::OnResetDevice**](id3dxline--onresetdevice.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




