---
title: Mipmap packing
description: Depending on the tier of tiled resources support, mipmaps with certain dimensions don't follow the standard tile shapes and are considered to all be packed together with one another in a manner that is opaque to the application.
ms.assetid: 3B416324-7656-495F-9BA9-8F5BE475ABC1
ms.topic: article
ms.date: 05/31/2018
---

# Mipmap packing

Depending on the [tier](tiled-resources-features-tiers.md) of tiled resources support, mipmaps with certain dimensions don't follow the standard tile shapes and are considered to all be packed together with one another in a manner that is opaque to the application. Higher tiers of support have broader guarantees about what types of surface dimensions fit in the standard tile shapes (and can therefore be individually mapped by applications).

What can vary between implementations is that—given a tiled resource's dimensions, format, number of mipmaps, and array slices—some number M of mips (per array slice) can be packed into some number N tiles. The [**ID3D11Device2::GetResourceTiling**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11device2-getresourcetiling) API exists to allow the driver to report to the application what M and N are (among other details about the surface that this API reports that are standard and don't vary by hardware vendor). The set of tiles for the packed mips are still 64KB and can be individually mapped into disparate locations in a tile pool. But the pixel shape of the tiles and how the mipmaps fit across the set of tiles is specific to a hardware vendor and too complex to expose. So, applications are required to either map all of the tiles that are designated as packed, or none of them, at a time. Otherwise, the behavior for accessing the tiled resource is undefined.

For arrayed surfaces, the set of packed mips and the number of packed tiles storing those mips (M and N described preceding) applies individually for each array slice.

Dedicated APIs for copying tiles ([**ID3D11DeviceContext2::CopyTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytiles) and [**ID3D11DeviceContext2::UpdateTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetiles)) can't access packed mips. Applications that want to copy data to and from packed mips can do so using all the non-tiled resource specific APIs for copying and rendering to surfaces.

## Related topics

<dl> <dt>

[How a tiled resource's area is tiled](how-a-tiled-resource-s-area-is-tiled.md)
</dt> </dl>

 

 




