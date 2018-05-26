---
Description: Calls ID3DXSpriteFlush and restores the device state to how it was before ID3DXSpriteBegin was called.
ms.assetid: 603c69f7-13a8-4646-b367-6f2d21b1a2a0
title: ID3DXSpriteEnd method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSprite::End method

Calls [**ID3DXSprite::Flush**](id3dxsprite--flush.md) and restores the device state to how it was before [**ID3DXSprite::Begin**](id3dxsprite--begin.md) was called.

## Syntax


```C++
HRESULT End();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

**ID3DXSprite::End** cannot be used as a substitute for either [**IDirect3DDevice9::EndScene**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-endscene?branch=master) or [**ID3DXRenderToSurface::EndScene**](id3dxrendertosurface--endscene.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> <dt>

[**ID3DXSprite::Begin**](id3dxsprite--begin.md)
</dt> </dl>

 

 




