---
Description: 'Prepares a device for drawing lines.'
ms.assetid: 'c597703d-6466-4b55-b1a6-a4e7c667e50c'
title: 'ID3DXLine::Begin method'
---

# ID3DXLine::Begin method

Prepares a device for drawing lines.

## Syntax


```C++
HRESULT Begin();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

Calling **ID3DXLine::Begin** is optional. If called outside of a ID3DXLine::Begin/ID3DXLine::End sequence, the draw functions will internally call ID3DXLine::Begin and ID3DXLine::End. To avoid extra overhead, this method should be used if more than one draw function will be called successively.

This method must be called from inside an [**IDirect3DDevice9::BeginScene**](idirect3ddevice9--beginscene.md) and [**IDirect3DDevice9::EndScene**](idirect3ddevice9--endscene.md) sequence.

ID3DXLine::Begin cannot be used as a substitute for either [**IDirect3DDevice9::BeginScene**](idirect3ddevice9--beginscene.md) or [**ID3DXRenderToSurface::BeginScene**](id3dxrendertosurface--beginscene.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




