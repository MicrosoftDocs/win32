---
Description: 'A surface represents a linear area of display memory and usually resides in the display memory of the display card, although surfaces can exist in system memory. Surfaces are managed by the IDirect3DSurface9 interface.'
ms.assetid: '17add726-3d95-46bc-8e15-3be0e570c49c'
title: 'Direct3D Surfaces (Direct3D 9)'
---

# Direct3D Surfaces (Direct3D 9)

A surface represents a linear area of display memory and usually resides in the display memory of the display card, although surfaces can exist in system memory. Surfaces are managed by the [**IDirect3DSurface9**](idirect3dsurface9.md) interface.

-   Front Buffer. A rectangle of memory that is translated by the graphics adapter and displayed on the monitor. In Direct3D an application never writes directly to the front buffer.
-   Back Buffer. A rectangle of memory that an application can directly write to. The back buffer is never directly displayed on the monitor.
-   Flipping surfaces. The process of moving the back buffer to the front buffer.
-   Swap chain. A collection of one or more back buffers that can be serially presented to the front buffer.

## Getting a Surface

Create a surface by calling any of these methods:

-   [**CreateDepthStencilSurface**](idirect3ddevice9--createdepthstencilsurface.md)
-   [**CreateOffscreenPlainSurface**](idirect3ddevice9--createoffscreenplainsurface.md)
-   [**CreateRenderTarget**](idirect3ddevice9--createrendertarget.md)

Surface formats determine how data for each pixel in surface memory is interpreted. Direct3D uses the [D3DFORMAT](d3dformat.md) member of the [**D3DSURFACE\_DESC**](d3dsurface-desc.md) structure to describe the surface format. You can retrieve the format of an existing surface by calling the [**GetDesc**](idirect3dsurface9--getdesc.md) method.

Once a surface is created, you can get a pointer to it by calling any of these methods:

-   [**GetCubeMapSurface**](idirect3dcubetexture9--getcubemapsurface.md)
-   [**GetBackBuffer**](idirect3ddevice9--getbackbuffer.md)
-   [**GetDepthStencilSurface**](idirect3ddevice9--getdepthstencilsurface.md)
-   [**GetFrontBufferData**](idirect3ddevice9--getfrontbufferdata.md)
-   [**GetRenderTarget**](idirect3ddevice9--getrendertarget.md)
-   [**GetBackBuffer**](idirect3dswapchain9--getbackbuffer.md)
-   [**GetSurfaceLevel**](idirect3dtexture9--getsurfacelevel.md)

The [**IDirect3DSurface9**](idirect3dsurface9.md) interface enables you to indirectly access memory through the [**UpdateSurface**](idirect3ddevice9--updatesurface.md) method. This method allows you to copy a rectangular region of pixels from one **IDirect3DSurface9** interface to another **IDirect3DSurface9** interface. The surface interface also has methods to directly access display memory. For example, you can use the [**LockRect**](idirect3dsurface9--lockrect.md) method to lock a rectangular region of display memory. It is important to call [**UnlockRect**](idirect3dsurface9--unlockrect.md) after you are done working with the locked rectangular region on the surface.

## Additional Surface Topics

Find out more about how to use surfaces with any of these topics:

-   [Surface Formats (Direct3D 9)](surface-formats.md)
-   [What Is a Swap Chain? (Direct3D 9)](what-is-a-swap-chain-.md)
-   [Width vs. Pitch (Direct3D 9)](width-vs--pitch.md)
-   [Flipping Surfaces (Direct3D 9)](flipping-surfaces.md)
-   [Page Flipping and Back Buffering (Direct3D 9)](page-flipping-and-back-buffering.md)
-   [Copying to Surfaces (Direct3D 9)](copying-to-surfaces.md)
-   [Copying Surfaces (Direct3D 9)](copying-surfaces.md)
-   [Accessing Surface Memory Directly (Direct3D 9)](accessing-surface-memory-directly.md)
-   [Private Surface Data (Direct3D 9)](private-surface-data.md)
-   [Gamma Controls (Direct3D 9)](gamma-controls.md)

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> </dl>

 

 



