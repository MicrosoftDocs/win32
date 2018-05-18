---
Description: 'Specifies how the monitor being used to display a full-screen application is rotated.'
ms.assetid: '190aa10e-4bf0-45ec-9c07-2582c5536074'
title: D3DDISPLAYROTATION enumeration
---

# D3DDISPLAYROTATION enumeration

Specifies how the monitor being used to display a full-screen application is rotated.

## Syntax


```C++
typedef enum D3DDISPLAYROTATION { 
  D3DDISPLAYROTATION_IDENTITY  = 1,
  D3DDISPLAYROTATION_90        = 2,
  D3DDISPLAYROTATION_180       = 3,
  D3DDISPLAYROTATION_270       = 4
} D3DDISPLAYROTATION;
```



## Constants

<dl> <dt>

<span id="D3DDISPLAYROTATION_IDENTITY"></span><span id="d3ddisplayrotation_identity"></span>**D3DDISPLAYROTATION\_IDENTITY**
</dt> <dd>

Display is not rotated.

</dd> <dt>

<span id="D3DDISPLAYROTATION_90"></span><span id="d3ddisplayrotation_90"></span>**D3DDISPLAYROTATION\_90**
</dt> <dd>

Display is rotated 90 degrees.

</dd> <dt>

<span id="D3DDISPLAYROTATION_180"></span><span id="d3ddisplayrotation_180"></span>**D3DDISPLAYROTATION\_180**
</dt> <dd>

Display is rotated 180 degrees.

</dd> <dt>

<span id="D3DDISPLAYROTATION_270"></span><span id="d3ddisplayrotation_270"></span>**D3DDISPLAYROTATION\_270**
</dt> <dd>

Display is rotated 270 degrees.

</dd> </dl>

## Remarks

This enumeration is used in [**IDirect3D9Ex::GetAdapterDisplayModeEx**](idirect3d9ex-getadapterdisplaymodeex.md), [**IDirect3DDevice9Ex::GetDisplayModeEx**](idirect3ddevice9ex-getdisplaymodeex.md), and [**IDirect3DSwapChain9Ex::GetDisplayModeEx**](idirect3dswapchain9-getdisplaymodeex.md).

Applications may choose to handle monitor rotation themselves by using the [D3DPRESENTFLAG\_NOAUTOROTATE](d3dpresentflag.md), in which case, the application will need to know how the monitor is rotated so that it may adjust its rendering accordingly.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




