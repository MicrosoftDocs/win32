---
Description: 'Calls ID3DXSprite::Flush and restores the device state to how it was before ID3DXSprite::Begin was called.'
ms.assetid: '603c69f7-13a8-4646-b367-6f2d21b1a2a0'
title: 'ID3DXSprite::End method'
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

**ID3DXSprite::End** cannot be used as a substitute for either [**IDirect3DDevice9::EndScene**](idirect3ddevice9--endscene.md) or [**ID3DXRenderToSurface::EndScene**](id3dxrendertosurface--endscene.md).

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

 

 




