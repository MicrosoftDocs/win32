---
Description: Use this method to re-acquire resources and save initial state.
ms.assetid: 74f8616e-c3ed-4231-b701-009213ea48c0
title: ID3DXSpriteOnResetDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSprite::OnResetDevice method

Use this method to re-acquire resources and save initial state.

## Syntax


```C++
HRESULT OnResetDevice();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

**ID3DXSprite::OnResetDevice** should be called each time the device is reset (using [**IDirect3DDevice9::Reset**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-reset?branch=master)), before any other methods are called. This is a good place to re-acquire video-memory resources and capture state blocks.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> </dl>

 

 




