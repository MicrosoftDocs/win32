---
description: When using IDirect3DDevice9::UpdateSurface, pass a rectangle on the source surface, or use NULL to specify the entire surface.
ms.assetid: 2219d037-8480-4c36-b04e-0c23406a2e7e
title: Copying to Surfaces (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Copying to Surfaces (Direct3D 9)

When using [**IDirect3DDevice9::UpdateSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatesurface), pass a rectangle on the source surface, or use **NULL** to specify the entire surface. You also pass a point on the destination surface to which the upper left position of the rectangle on the source image is copied. This method does not support clipping. The operation will fail unless the source rectangle and the corresponding destination rectangle are completely contained within the source and destination surfaces respectively. This method does not support alpha blending, color keys, or format conversion. Note that the destination and source surfaces must be distinct.

For other restrictions when using UpdateSurface, see [**IDirect3DDevice9::UpdateSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatesurface).

The following methods are also available in C++/C for copying images to a Direct3D surface.

-   [**D3DXLoadSurfaceFromFile**](d3dxloadsurfacefromfile.md)
-   [**D3DXLoadSurfaceFromFileInMemory**](d3dxloadsurfacefromfileinmemory.md)
-   [**D3DXLoadSurfaceFromMemory**](d3dxloadsurfacefrommemory.md)
-   [**D3DXLoadSurfaceFromResource**](d3dxloadsurfacefromresource.md)
-   [**D3DXLoadSurfaceFromSurface**](d3dxloadsurfacefromsurface.md)
-   [**IDirect3DDevice9::UpdateSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-updatesurface)

## UpdateSurface Example

The following example copies two rectangles from the source surface to a destination surface. The first rectangle is copied from (0, 0, 50, 50) on the source surface to the same location on the destination surface, and the second rectangle is copied from (50, 50, 100, 100) on the source surface to (150, 150, 200, 200) on the destination surface.


```
//The following assumptions are made:
// -d3dDevice is a valid Direct3DDevice9 object.
// -pSource and pDest are valid IDirect3DSurface9 pointers.

RECT  rcSource[] = {  0,  0,  50,  50,
                     50, 50, 100, 100 };
POINT ptDest[]   = {  0,  0, 150, 150 };

d3dDevice->UpdateSurface( pSource, rcSource, 2, pDest, ptDest);
```



## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> <dt>

[**IDirect3DDevice9::StretchRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-stretchrect)
</dt> </dl>

 

 
