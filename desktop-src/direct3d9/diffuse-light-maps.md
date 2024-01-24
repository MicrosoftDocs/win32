---
description: When illuminated by a light source, matte surfaces display diffuse light reflection.
ms.assetid: a6ed351a-7889-4993-96bf-b03352a815da
title: Diffuse Light Maps (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Diffuse Light Maps (Direct3D 9)

When illuminated by a light source, matte surfaces display diffuse light reflection. The brightness of diffuse light depends on the distance from the light source and the angle between the surface normal and the light source direction vector. The diffuse lighting effects simulated by lighting calculations produce only general effects.

Your application can simulate more complex diffuse lighting with texture light maps. Do this by adding the diffuse light map to the base texture, as shown in the following C++ code example.


```
// This example assumes that d3dDevice is a valid pointer to an
// IDirect3DDevice9 interface.
// lptexBaseTexture is a valid pointer to a texture.
// lptexDiffuseLightMap is a valid pointer to a texture that contains 
// RGB diffuse light map data.

// Set the base texture.
d3dDevice->SetTexture(0,lptexBaseTexture );

// Set the base texture operation and args.
d3dDevice->SetTextureStageState(0,D3DTSS_COLOROP,
                                D3DTOP_MODULATE );
d3dDevice->SetTextureStageState(0,D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState(0,D3DTSS_COLORARG2, D3DTA_DIFFUSE );

// Set the diffuse light map.
d3dDevice->SetTexture(1,lptexDiffuseLightMap );

// Set the blend stage.
d3dDevice->SetTextureStageState(1, D3DTSS_COLOROP, D3DTOP_MODULATE );
d3dDevice->SetTextureStageState(1, D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState(1, D3DTSS_COLORARG2, D3DTA_CURRENT );
```



## Related topics

<dl> <dt>

[Light Mapping with Textures](light-mapping-with-textures.md)
</dt> </dl>

 

 



