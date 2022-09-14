---
description: Direct3D 9 supports paletted textures through a set of 256 entry palettes associated with the IDirect3DDevice9 object.
ms.assetid: dea4b4bc-7eba-40fa-9c2c-0851fe7e231b
title: Texture Palettes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Palettes (Direct3D 9)

Direct3D 9 supports paletted textures through a set of 256 entry palettes associated with the [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) object. A palette is made current by calling the [**IDirect3DDevice9::SetCurrentTexturePalette**](/windows/desktop/api) method. The current palette is used for translating all paletted textures for all active texture stages. [**IDirect3DDevice9::SetPaletteEntries**](/windows/desktop/api) updates all of a palette's 256 entries. Each entry is a [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry) structure of the format D3DFMT\_A8R8G8B8. All entries default to 0xFFFFFFFF.

The [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) palettes contain an alpha channel. This alpha channel can be used when the D3DPTEXTURECAPS\_ALPHAPALETTE device capability flag is set, indicating that the device supports alpha from the palette. The palette alpha channel is used when the texture format does not have an alpha channel. If the device does not support alpha from the palette and the texture format does not have an alpha channel, then a value of 0xFF is used for alpha.

There is a maximum of 65,536 (0x0000FFFF) palettes. Because memory resources associated with the set of palettes are proportional to the maximum palette number that an application references, use contiguous palette numbers starting at zero.

## Related topics

<dl> <dt>

[Basic Texturing Concepts](basic-texturing-concepts.md)
</dt> </dl>

 

 
