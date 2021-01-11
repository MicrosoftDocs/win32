---
description: Your application will usually render 3D scenes more realistically if it uses colored light maps. A colored light map uses the RGB data in the light map for its lighting information.
ms.assetid: 47760884-7b9f-45de-9d4a-faf822da899f
title: Color Light Maps (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Color Light Maps (Direct3D 9)

Your application will usually render 3D scenes more realistically if it uses colored light maps. A colored light map uses the RGB data in the light map for its lighting information.

The following C++ code example demonstrates light mapping with RGB color data.


```
// This example assumes that d3dDevice is a valid pointer to an
// IDirect3DDevice9 interface and that lptexLightMap is a valid
// pointer to a texture that contains RGB light map data.

// Set the light map texture as the first texture.
d3dDevice->SetTexture(0, lptexLightMap);

d3dDevice->SetTextureStageState( 0,D3DTSS_COLOROP, D3DTOP_MODULATE );
d3dDevice->SetTextureStageState( 0,D3DTSS_COLORARG1, D3DTA_TEXTURE );
d3dDevice->SetTextureStageState( 0,D3DTSS_COLORARG2, D3DTA_DIFFUSE );
```



This example sets the light map as the first texture. It then sets the state of the first blending stage to modulate the incoming texture data. It uses the first texture and the current color of the primitive as the arguments to the modulate operation.

## Related topics

<dl> <dt>

[Light Mapping with Textures](light-mapping-with-textures.md)
</dt> </dl>

 

 



