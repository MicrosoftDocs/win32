---
description: The alpha value of a color controls its transparency. Enabling alpha blending allows colors, materials, and textures on a surface to be blended with transparency onto another surface.
ms.assetid: e8e925d5-262d-45c0-be9f-21c9a103d7b7
title: Alpha Blending State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Blending State (Direct3D 9)

The alpha value of a color controls its transparency. Enabling alpha blending allows colors, materials, and textures on a surface to be blended with transparency onto another surface.

For more information, see [Alpha Texture Blending (Direct3D 9)](alpha-texture-blending.md) and [Texture Blending (Direct3D 9)](texture-blending.md).

Applications written in C++ use the [**D3DRS\_ALPHABLENDENABLE**](./d3drenderstatetype.md) render state to enable alpha transparency blending. The Direct3D API allows many types of alpha blending. However, it is important to note the user's 3D hardware might not support all the blending states allowed by Direct3D.

The type of alpha blending that is done depends on the [**D3DRS\_SRCBLEND**](./d3drenderstatetype.md) And **D3DRS\_DESTBLEND** render states. Source and destination blend states are used in pairs. The following code example demonstrates how the source blend state is set to D3DBLEND\_SRCCOLOR and the destination blend state is set to D3DBLEND\_INVSRCCOLOR.


```
// This code example assumes that d3dDevice is a
// valid pointer to an IDirect3DDevice9 interface.

// Set the source blend state.
d3dDevice->SetRenderState(D3DRS_SRCBLEND, D3DBLEND_SRCCOLOR);

// Set the destination blend state.

d3dDevice->SetRenderState(D3DRS_DESTBLEND, D3DBLEND_INVSRCCOLOR);
```



Altering the source and destination blend states can give the appearance of emissive objects in a foggy or dusty atmosphere. For instance, if your application models flames, force fields, plasma beams, or similarly radiant objects in a foggy environment, set the source and destination blend states to D3DBLEND\_ONE.

Another application of alpha blending is to control the lighting in a 3D scene, also called light mapping. Setting the source blend state to D3DBLEND\_ZERO and the destination blend state to D3DBLEND\_SRCALPHA darkens a scene according to the source alpha information. The source primitive is used as a light map that scales the contents of the frame buffer to darken it when appropriate. This produces monochrome light mapping.

You can achieve color light mapping by setting the source alpha blending state to D3DBLEND\_ZERO and the destination blend state to D3DBLEND\_SRCCOLOR.

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
