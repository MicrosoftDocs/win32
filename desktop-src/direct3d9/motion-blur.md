---
description: You can enhance the perceived speed of an object in a 3D scene by blurring the object and leaving a blurred trail of object images behind the object. Direct3D applications accomplish this by rendering the object multiple times per frame.
ms.assetid: 8b1a1f0d-5857-4ab4-828c-8ca7c17a4890
title: Motion Blur (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Motion Blur (Direct3D 9)

You can enhance the perceived speed of an object in a 3D scene by blurring the object and leaving a blurred trail of object images behind the object. Direct3D applications accomplish this by rendering the object multiple times per frame.

Recall that Direct3D applications typically render scenes into an off-screen buffer. The contents of the buffer are displayed on the screen when the application calls the [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present) method. Your Direct3D application can render the object multiple times into a scene before it displays the frame on the screen.

Programmatically, your application makes multiple calls to a DrawPrimitive method, repeatedly passing the same 3D object. Before each call, the position of the object is updated slightly, producing a series of blurred object images on the target rendering surface. If the object has one or more textures, your application can enhance the motion blur effect by rendering the first image of the object with all its textures nearly transparent. Each time the object renders, the transparency of the object's texture decreases. When your application renders the object in its final position, it should render the object's textures without transparency. The exception is if you're adding motion blur to another effect that requires texture transparency. In any case, the initial image of the object in the frame should be the most transparent. The final image should be the least transparent.

After your application renders the series of object images onto the target rendering surface and renders the rest of the scene, it should call the [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present) method to display the frame on the screen.

If your application is simulating the effect of the user moving through a scene at high speed, it can add motion blur to the entire scene. In this case, your application renders the entire scene multiple times per frame. Each time the scene renders, your application must move the viewpoint slightly. If the scene is highly complex, the user may see a visible performance degradation as acceleration is increased because of the increasing number of scene renderings per frame.

## Related topics

<dl> <dt>

[Antialiasing](antialiasing.md)
</dt> </dl>

 

 
