---
description: The ID3DXRenderToEnvMap interface is used to generalize the process of rendering to environment maps.
ms.assetid: d72db260-5493-4381-9269-521ad333f0b2
title: ID3DXRenderToEnvMap interface (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXRenderToEnvMap
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXRenderToEnvMap interface

The ID3DXRenderToEnvMap interface is used to generalize the process of rendering to environment maps.

## Members

The **ID3DXRenderToEnvMap** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXRenderToEnvMap** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXRenderToEnvMap** interface has these methods.



| Method                                                          | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BeginCube**](id3dxrendertoenvmap--begincube.md)             | Initiate the rendering of a cubic environment map.<br/>                                                                                                                                    |
| [**BeginHemisphere**](id3dxrendertoenvmap--beginhemisphere.md) | Initiate the rendering of a hemispheric environment map.<br/>                                                                                                                              |
| [**BeginParabolic**](id3dxrendertoenvmap--beginparabolic.md)   | Initiate the rendering of a parabolic environment map.<br/>                                                                                                                                |
| [**BeginSphere**](id3dxrendertoenvmap--beginsphere.md)         | Initiate the rendering of a spherical environment map.<br/>                                                                                                                                |
| [**End**](id3dxrendertoenvmap--end.md)                         | Restore all render targets and, if needed, compose all the rendered faces into the environment map surface.<br/>                                                                           |
| [**Face**](id3dxrendertoenvmap--face.md)                       | Initiate the drawing of each face of an environment map.<br/>                                                                                                                              |
| [**GetDesc**](id3dxrendertoenvmap--getdesc.md)                 | Retrieves the description of the render surface.<br/>                                                                                                                                      |
| [**GetDevice**](id3dxrendertoenvmap--getdevice.md)             | Retrieves the Direct3D device associated with the environment map.<br/>                                                                                                                    |
| [**OnLostDevice**](id3dxrendertoenvmap--onlostdevice.md)       | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.<br/> |
| [**OnResetDevice**](id3dxrendertoenvmap--onresetdevice.md)     | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                       |



 

## Remarks

An environment map is used to texture-map scene geometry to provide a more sophisticated scene without using complex geometry. This interface supports creating surfaces for the following kinds of geometry: cube, half sphere or hemispheric, parabolic, or sphere.

The **ID3DXRenderToEnvMap** interface is obtained by calling the [**D3DXCreateRenderToEnvMap**](d3dxcreaterendertoenvmap.md) function.

The LPD3DXRenderToEnvMap type is defined as a pointer to the **ID3DXRenderToEnvMap** interface.


```
typedef interface ID3DXRenderToEnvMap ID3DXRenderToEnvMap;
typedef interface ID3DXRenderToEnvMap *LPD3DXRenderToEnvMap;
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

 

 
