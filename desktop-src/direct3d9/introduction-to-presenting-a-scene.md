---
Description: 'The presentation APIs are a set of methods that control the state of the device that affects what the user sees on the monitor. These methods include setting display modes and once-per-frame methods that are used to present images to the user.'
ms.assetid: 'fb2ddc0d-50ac-48aa-8a5c-f232b0f8e7aa'
title: 'Introduction to Presenting a Scene (Direct3D 9)'
---

# Introduction to Presenting a Scene (Direct3D 9)

The presentation APIs are a set of methods that control the state of the device that affects what the user sees on the monitor. These methods include setting display modes and once-per-frame methods that are used to present images to the user.

-   [**IDirect3DDevice9::Present**](idirect3ddevice9--present.md)
-   [**IDirect3DDevice9::Reset**](idirect3ddevice9--reset.md)
-   [**IDirect3DDevice9::GetGammaRamp**](idirect3ddevice9--getgammaramp.md)
-   [**IDirect3DDevice9::SetGammaRamp**](idirect3ddevice9--setgammaramp.md)
-   [**IDirect3DDevice9::GetRasterStatus**](idirect3ddevice9--getrasterstatus.md)

Familiarity with the following terms is necessary to understand the presentation APIs.

-   front buffer. A rectangle of memory that is translated by the graphics adapter and displayed on the monitor or other output device.
-   back buffer. A surface whose contents can be promoted to the front buffer.
-   swap chain. A collection of back buffers that can be serially presented to the front buffer. Typically, a full-screen swap chain presents subsequent images with the flipping device driver interface (DDI), and a windowed swap chain presents images with the blitting DDI.

Because Direct3D 9 has one swap chain as a property of the device, there is always at least one swap chain per device. The [**IDirect3DDevice9**](idirect3ddevice9.md) interface has a set of methods that manipulate the implicit swap chain and are a copy of the swap chain's own interface. Applications can create additional swap chains; however, this is not necessary for the typical single window or full-screen application.

The front buffer is not directly exposed in Direct3D 9. As a result, applications cannot lock or render to the front buffer. For details, see [Accessing the Color Front Buffer (Direct3D 9)](accessing-the-color-front-buffer.md).

> [!Note]  
> DirectX 7 provided a number of presentation APIs that were called together. A good example of this is the IDirectDraw7::SetCooperativeLevel, IDirectDraw7::SetDisplayMode, and IDirectDraw7::CreateSurface sequence. Additionally, the IDirectDrawSurface7::Flip and IDirectDrawSurface7::Blt methods signaled the transport of rendered frames to the monitor. Direct3D 9 collapses these groups of APIs into two main methods, Reset and Present. Reset subsumes SetCooperativeLevel, SetDisplayMode, CreateSurface, and some of the parameters to flip. Present subsumes flip and the presentation uses of blit.

 

A call to [**IDirect3D9::CreateDevice**](idirect3d9--createdevice.md) represents an implicit reset of the device. The Direct3D 9 API has no notion of a primary surface; you cannot create an object that represents the primary surface. It is considered to be an internal property of the device.

Gamma ramps are associated with a swap chain and are manipulated with the [**IDirect3DDevice9::GetGammaRamp**](idirect3ddevice9--getgammaramp.md) and [**IDirect3DDevice9::SetGammaRamp**](idirect3ddevice9--setgammaramp.md) methods.

## Related topics

<dl> <dt>

[Presenting a Scene](presenting-a-scene.md)
</dt> </dl>

 

 



