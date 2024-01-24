---
description: In addition to the swap chain that is owned and manipulated through the IDirect3DDevice9 interface, an application can create additional swap chains in order to present multiple views from the same device.
ms.assetid: 4fc09b9c-7adb-4f5d-80e0-2d39bc10420e
title: Presenting Multiple Views in Windowed Mode (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Presenting Multiple Views in Windowed Mode (Direct3D 9)

In addition to the swap chain that is owned and manipulated through the [**IDirect3DDevice9**](/windows/desktop/api) interface, an application can create additional swap chains in order to present multiple views from the same device. The application typically creates one swap chain per view by using the [**IDirect3DDevice9::CreateAdditionalSwapChain**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createadditionalswapchain) method, and associates each swap chain with a particular window. The application renders images into the back buffers of each swap chain, and then presents them individually.

Only one swap chain at a time can be full-screen on each adapter.

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
