---
description: When illuminated by a light source, shiny objects - those that use highly reflective materials - receive specular highlights.
ms.assetid: cea53131-1e2e-4389-80fd-ef5a0d068703
title: Specular Light Maps (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Specular Light Maps (Direct3D 9)

When illuminated by a light source, shiny objects - those that use highly reflective materials - receive specular highlights. In some cases, the specular highlights produced by the lighting module is not accurate. To produce a more appealing highlight, many Direct3D applications apply specular light maps to primitives.

To perform specular light mapping, add the specular light map to the primitive's texture, then modulate (multiply the result by) the RGB light map.

The following code example illustrates this process in C++.


```
// This example assumes that d3dDevice is a valid pointer to an
// IDirect3DDevice9 interface.
// lptexBaseTexture is a valid pointer to a texture.
// lptexSpecLightMap is a valid pointer to a texture that contains RGB
// specular light map data.
// lptexLightMap is a valid pointer to a texture that contains RGB
// light map data.

// Set the base texture.
d3dDevice->SetTexture(0, lptexBaseTexture );

// Set the base texture operation and arguments.
d3dDevice->SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_MODULATE );
d3dDevice->SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE );

// Set the specular light map.
d3dDevice->SetTexture(1, lptexSpecLightMap);

// Set the specular light map operation and args.
d3dDevice->SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_ADD );
d3dDevice->SetTextureStageState(1, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState(1, D3DTSS_COLORARG2, D3DTA_CURRENT );

// Set the RGB light map.
d3dDevice->SetTexture(2, lptexLightMap);

// Set the RGB light map operation and arguments.
d3dDevice->SetTextureStageState(2,D3DTSS_COLOROP, D3DTOP_MODULATE);
d3dDevice->SetTextureStageState(2,D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState(2,D3DTSS_COLORARG2, D3DTA_CURRENT );
```



## Related topics

<dl> <dt>

[Light Mapping with Textures](light-mapping-with-textures.md)
</dt> </dl>

 

 



