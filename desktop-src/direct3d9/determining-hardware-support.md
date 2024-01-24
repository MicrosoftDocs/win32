---
description: Direct3D provides the following functions to determine hardware support.
ms.assetid: 63afa799-2c2c-432c-993e-dca8f7433d59
title: Determining Hardware Support (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Determining Hardware Support (Direct3D 9)

Direct3D provides the following functions to determine hardware support.

-   [**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat)

    Used to verify whether a surface format can be used as a texture, whether a surface format can be used as a texture and a render target, or whether a surface format can be used as a depth-stencil buffer. In addition, this method is used to verify depth buffer format support and depth-stencil buffer format support.

-   [**IDirect3D9::CheckDeviceType**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdevicetype)

    Used to verify a device's ability to perform hardware acceleration, a device's ability to build a swap chain for presentation, or a device's ability to render to the current display format.

-   [**IDirect3D9::CheckDepthStencilMatch**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdepthstencilmatch)

    Used to verify whether a depth-stencil buffer format is compatible with a render-target format. Note that before calling this method, the application should call [**IDirect3D9::CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) on both the depth-stencil and render-target formats.

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 
