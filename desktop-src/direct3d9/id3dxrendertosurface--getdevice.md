---
Description: Retrieves the Direct3D device associated with the render surface.
ms.assetid: 579cf7da-b8e0-4d9f-93b8-b1f47c3d5654
title: ID3DXRenderToSurfaceGetDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXRenderToSurface::GetDevice method

Retrieves the Direct3D device associated with the render surface.

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

Address of a pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the Direct3D device object associated with the render surface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL. Calling this method will increase the internal reference count on the [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface. Be sure to call [**IUnknown**](com.iunknown) when you are done using this **IDirect3DDevice9** interface or you will have a memory leak.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToSurface](id3dxrendertosurface.md)
</dt> </dl>

 

 




