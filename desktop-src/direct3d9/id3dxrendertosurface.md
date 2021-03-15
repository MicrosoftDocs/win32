---
description: The ID3DXRenderToSurface interface is used to generalize the process of rendering to surfaces.
ms.assetid: e9f2ca5e-faa3-45a8-94eb-16f354618e80
title: ID3DXRenderToSurface interface (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXRenderToSurface
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXRenderToSurface interface

The ID3DXRenderToSurface interface is used to generalize the process of rendering to surfaces.

## Members

The **ID3DXRenderToSurface** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXRenderToSurface** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXRenderToSurface** interface has these methods.



| Method                                                       | Description                                                                                                                                                                                     |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BeginScene**](id3dxrendertosurface--beginscene.md)       | Begins a scene.<br/>                                                                                                                                                                      |
| [**EndScene**](id3dxrendertosurface--endscene.md)           | Ends a scene.<br/>                                                                                                                                                                        |
| [**GetDesc**](id3dxrendertosurface--getdesc.md)             | Retrieves the parameters of the render surface.<br/>                                                                                                                                      |
| [**GetDevice**](id3dxrendertosurface--getdevice.md)         | Retrieves the Direct3D device associated with the render surface.<br/>                                                                                                                    |
| [**OnLostDevice**](id3dxrendertosurface--onlostdevice.md)   | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost or before resetting a device.<br/> |
| [**OnResetDevice**](id3dxrendertosurface--onresetdevice.md) | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                      |



 

## Remarks

Surfaces can be used in a variety of ways including render targets, off-screen rendering, or rendering to textures.

A surface can be configured using a separate viewport using the [**ID3DXRenderToSurface::BeginScene**](id3dxrendertosurface--beginscene.md) method, to provide a custom render view. If the surface is not a render target, a compatible render target is used, and the result is copied to the surface at the end of the scene.

The **ID3DXRenderToSurface** interface is obtained by calling the [**D3DXCreateRenderToSurface**](d3dxcreaterendertosurface.md) function.

The LPD3DXRENDERTOSURFACE type is defined as a pointer to the **ID3DXRenderToSurface** interface.


```
typedef interface ID3DXRenderToSurface ID3DXRenderToSurface;
typedef interface ID3DXRenderToSurface *LPD3DXRENDERTOSURFACE;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
