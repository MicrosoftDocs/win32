---
Description: In addition to the swap chain that is owned and manipulated through the Direct3DDevice object, an application can use the IDirect3DDevice9::CreateAdditionalSwapChain method to create additional swap chains to present multiple views from the same device.
ms.assetid: f0d01dfb-d1de-4d16-8c64-4ae56d7fed06
title: Multiple Views in Windowed Mode (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Views in Windowed Mode (Direct3D 9)

In addition to the swap chain that is owned and manipulated through the Direct3DDevice object, an application can use the [**IDirect3DDevice9::CreateAdditionalSwapChain**](https://msdn.microsoft.com/library/Bb174354(v=VS.85).aspx) method to create additional swap chains to present multiple views from the same device.

Typically, the application creates one swap chain per view, and it associates each swap chain with a particular view. The application renders images in the back buffers of each swap chain, and then uses the [**IDirect3DDevice9::Present**](https://msdn.microsoft.com/library/Bb174423(v=VS.85).aspx) method to present them individually. Note that only one swap chain at a time can be full-screen on each adapter.

## Related topics

<dl> <dt>

[Presenting a Scene](presenting-a-scene.md)
</dt> </dl>

 

 



