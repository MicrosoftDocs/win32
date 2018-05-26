---
Description: Restores the device state to how it was when ID3DXLineBegin was called.
ms.assetid: 06243c30-2d1d-4101-a373-46fd9a0d88d3
title: ID3DXLineEnd method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXLine::End method

Restores the device state to how it was when [**ID3DXLine::Begin**](id3dxline--begin.md) was called.

## Syntax


```C++
HRESULT End();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

**ID3DXLine::End** cannot be used as a substitute for either [**IDirect3DDevice9::EndScene**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-endscene?branch=master) or [**ID3DXRenderToSurface::EndScene**](id3dxrendertosurface--endscene.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> <dt>

[**ID3DXLine::Begin**](id3dxline--begin.md)
</dt> </dl>

 

 




