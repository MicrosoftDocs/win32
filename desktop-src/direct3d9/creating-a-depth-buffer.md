---
description: A depth buffer is a property of the device. To create a depth buffer that is managed by Direct3D, set the appropriate members of the D3DPRESENT\_PARAMETERS structure as shown in the following code example.
ms.assetid: 2b442cf7-2146-4dea-809a-ebb8bcfbec08
title: Creating a Depth Buffer (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Depth Buffer (Direct3D 9)

A depth buffer is a property of the device. To create a depth buffer that is managed by Direct3D, set the appropriate members of the [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) structure as shown in the following code example.


```
D3DPRESENT_PARAMETERS d3dpp; 
ZeroMemory( &d3dpp, sizeof(d3dpp) );
d3dpp.Windowed               = TRUE;
d3dpp.SwapEffect             = D3DSWAPEFFECT_COPY;
d3dpp.EnableAutoDepthStencil = TRUE;
d3dpp.AutoDepthStencilFormat = D3DFMT_D16;
```



By setting the EnableAutoDepthStencil member to **TRUE**, you instruct Direct3D to manage depth buffers for the application. Note that AutoDepthStencilFormat must be set to a valid depth buffer format. The D3DFMT\_D16 flag specifies a 16-bit depth buffer, if one is available.

The following call to the [**IDirect3D9::CreateDevice**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-createdevice) method creates a device that then creates a depth buffer.


```
if( FAILED( g_pD3D->CreateDevice( D3DADAPTER_DEFAULT, D3DDEVTYPE_HAL, hWnd,
                                D3DCREATE_SOFTWARE_VERTEXPROCESSING,
                                &d3dpp, &d3dDevice ) ) )
return E_FAIL;
```



The depth buffer is automatically set as the render target of the device. When the device is reset, the depth buffer is automatically destroyed and re-created in the new size.

To create a new depth buffer surface, use the [**IDirect3DDevice9::CreateDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createdepthstencilsurface) method.

To set a new depth-buffer surface for the device, use the [**IDirect3DDevice9::SetDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setdepthstencilsurface) method.

To use the depth buffer in your application, you need to enable the depth buffer. For details, see [Enabling Depth Buffering (Direct3D 9)](enabling-depth-buffering.md).

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
