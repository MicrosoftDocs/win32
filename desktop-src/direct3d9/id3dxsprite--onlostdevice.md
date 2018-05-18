---
Description: 'Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost or before resetting a device.'
ms.assetid: '60028f18-21fe-428b-9bee-d5359671da81'
title: 'ID3DXSprite::OnLostDevice method'
---

# ID3DXSprite::OnLostDevice method

Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost or before resetting a device.

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

This method should be called whenever the device is lost or before the user calls [**IDirect3DDevice9::Reset**](idirect3ddevice9--reset.md). Even if the device was not actually lost, **ID3DXSprite::OnLostDevice** is responsible for freeing stateblocks and other resources that may need to be released before resetting the device. As a result, the font object cannot be used again before calling **IDirect3DDevice9::Reset** and then [**ID3DXSprite::OnResetDevice**](id3dxsprite--onresetdevice.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> </dl>

 

 




