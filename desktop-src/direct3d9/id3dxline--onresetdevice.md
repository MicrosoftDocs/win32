---
Description: 'Use this method to re-acquire resources and save initial state.'
ms.assetid: 'beca7a51-e799-4e03-81a3-218552231428'
title: 'ID3DXLine::OnResetDevice method'
---

# ID3DXLine::OnResetDevice method

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

**ID3DXLine::OnResetDevice** should be called each time the device is reset (using [**IDirect3DDevice9::Reset**](idirect3ddevice9--reset.md)), before any other methods are called. This is a good place to re-acquire video-memory resources and capture state blocks.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




