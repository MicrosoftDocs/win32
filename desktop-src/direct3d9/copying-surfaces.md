---
Description: The term blit is shorthand for &\#0034;bit block transfer,&\#0034; which is the process of transferring blocks of data from one place in memory to another.
ms.assetid: 5f2aed2e-66d2-40e6-be35-92c3f92d17bd
title: Copying Surfaces (Direct3D 9)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Copying Surfaces (Direct3D 9)

The term blit is shorthand for "bit block transfer," which is the process of transferring blocks of data from one place in memory to another. The blitting device driver interface (DDI) continues to be used in Direct3D 9 as the primary mechanism for moving large rectangles of pixels on a per-frame basis, the mechanism behind the copy-oriented [**IDirect3DDevice9::Present**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-present?branch=master) method. The transportation of artwork in the blit operation is performed by the [**IDirect3DDevice9::UpdateTexture**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-updatetexture?branch=master) method. Artwork can also be copied in Direct3D 9 by using the [**IDirect3DDevice9::UpdateSurface**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-updatesurface?branch=master) method, which copies a rectangular subset of pixels.

> [!Note]  
> Direct3D 9 provides D3DX functions that enable you to load artwork from files, apply color conversion, and resize artwork. For more information about the available functions see [Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md).

 

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> <dt>

[**IDirect3DDevice9::StretchRect**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-stretchrect?branch=master)
</dt> <dt>

**IDirect3DDevice9::StretchRect**
</dt> </dl>

 

 



