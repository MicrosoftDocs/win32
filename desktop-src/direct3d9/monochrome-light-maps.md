---
description: Some older 3D accelerator boards do not support texture blending using the alpha value of the destination pixel.
ms.assetid: 77d3b9fd-3232-4955-9df2-d4763d3eed6f
title: Monochrome Light Maps (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Monochrome Light Maps (Direct3D 9)

Some older 3D accelerator boards do not support texture blending using the alpha value of the destination pixel. See [Alpha Texture Blending (Direct3D 9)](alpha-texture-blending.md) for more information. These adapters also generally do not support multiple texture blending. If your application is running on an adapter such as this, it can use multipass texture blending to perform monochrome light mapping.

To perform monochrome light mapping, an application stores the lighting information in the alpha data of its light map textures. The application uses the texture filtering capabilities of Direct3D to perform a mapping from each pixel in the primitive's image to a corresponding texel in the light map. It sets the source blending factor to the alpha value of the corresponding texel.

The following example illustrates how an application can use a texture as a monochrome light map:


```
// This example assumes that d3dDevice is a valid pointer to an
// IDirect3DDevice9 interface and that lptexLightMap is a valid
// pointer to a texture that contains monochrome light map data.

// Set the light map texture as the current texture.
d3dDevice->SetTexture(0, lptexLightMap);

// Set the color operation.
d3dDevice->SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_SELECTARG1);

// Set argument 1 to the color operation.
d3dDevice->SetTextureStageState(0, D3DTSS_COLORARG1,
                                D3DTA_TEXTURE | D3DTA_ALPHAREPLICATE);
```



Because display adapters that do not support destination alpha blending usually do not support multiple texture blending, this example sets the light map as the first texture, which is available on all 3D accelerator cards. The sample code sets the color operation for the texture's blending stage to blend the texture data with the primitive's existing color. It then selects the first texture and the primitive's existing color as the input data.

## Related topics

<dl> <dt>

[Light Mapping with Textures](light-mapping-with-textures.md)
</dt> </dl>

 

 



