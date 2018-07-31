---
Description: Your application manipulates resources in order to render a scene.
ms.assetid: 4f0eea7d-b1e4-4d53-a136-f40df7a0fbb1
title: Manipulating Resources (Direct3D 9)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Manipulating Resources (Direct3D 9)

Your application manipulates resources in order to render a scene. First, an application needs to create a texture resource with one of the following methods:

-   [**IDirect3DDevice9::CreateCubeTexture**](https://msdn.microsoft.com/library/Bb174355(v=VS.85).aspx)
-   [**IDirect3DDevice9::CreateTexture**](https://msdn.microsoft.com/library/Bb174363(v=VS.85).aspx)
-   [**IDirect3DDevice9::CreateVolumeTexture**](https://msdn.microsoft.com/library/Bb174367(v=VS.85).aspx)

A texture resource can instead be created with one of the D3DXCreatexxx texturing functions.

The texture objects returned by the texture creation methods are containers for surfaces or volumes; these containers are generically known as buffers. The buffers owned by the resource inherit the usages, format, and pool of the resource but have their own type. For more information, see [Resource Properties (Direct3D 9)](resource-properties.md).

The application gains access to the contained surfaces, for the purpose of loading artwork, by calling the following methods. For details, see [Locking Resources (Direct3D 9)](locking-resources.md).

-   [**IDirect3DCubeTexture9::LockRect**](https://msdn.microsoft.com/library/Bb174334(v=VS.85).aspx)
-   [**IDirect3DTexture9::LockRect**](https://msdn.microsoft.com/library/Bb205913(v=VS.85).aspx)
-   [**IDirect3DVolumeTexture9::LockBox**](https://msdn.microsoft.com/library/Bb205945(v=VS.85).aspx)

The lock methods take arguments denoting the contained surface - for example, the mipmap sub-level or cube face of the texture - and return pointers to the pixels. The typical application never uses a surface object directly.

Create geometry-oriented resources by calling [**IDirect3DDevice9::CreateIndexBuffer**](/windows/desktop/api) or [**IDirect3DDevice9::CreateVertexBuffer**](https://msdn.microsoft.com/library/Bb174364(v=VS.85).aspx).

Lock and fill the buffer resources by calling either [**IDirect3DIndexBuffer9::Lock**](/windows/desktop/api) or [**IDirect3DVertexBuffer9::Lock**](https://msdn.microsoft.com/library/Bb205917(v=VS.85).aspx), depending upon the resource.

For managed texture resources, the resource creation process ends here. For non-managed texture resources, an application promotes system memory resources to device-accessible resources (for hardware acceleration) by calling [**IDirect3DDevice9::UpdateTexture**](https://msdn.microsoft.com/library/Bb205858(v=VS.85).aspx).

To present images rendered from resources, the application also needs color and depth-stencil buffers. For typical applications, the color buffer is owned by the device's swap chain, which is a collection of back-buffer surfaces, and is implicitly created with the device. Depth-stencil surfaces can be implicitly created, or explicitly created by using the [**IDirect3DDevice9::CreateDepthStencilSurface**](/windows/desktop/api) method. The application associates a device and its depth and color buffer with a call to [**IDirect3DDevice9::SetRenderTarget**](/windows/desktop/api) or [**IDirect3DDevice9::SetDepthStencilSurface**](https://msdn.microsoft.com/library/Bb174431(v=VS.85).aspx).

For details on presenting the final image, see [Presenting a Scene (Direct3D 9)](presenting-a-scene.md).

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> </dl>

 

 



