---
Description: Retrieves the device associated with the sprite object.
ms.assetid: 9ce18623-893e-4395-bdf7-8d16a641a557
title: ID3DXSpriteGetDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSprite::GetDevice method

Retrieves the device associated with the sprite object.

## Syntax


```C++
HRESULT GetDevice(
  [out, retval] LPDIRECT3DDEVICE9 *ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)\***

Address of a pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the Direct3D device object associated with the sprite object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

Calling this method will increase the internal reference count on the [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> </dl>

 

 




