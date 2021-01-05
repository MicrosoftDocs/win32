---
description: A blending stage is a set of texture operations and their arguments that define how textures are blended.
ms.assetid: 7f9e3041-a270-44a9-a8e1-bca5ea25a71e
title: Creating Blending Stages (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Creating Blending Stages (Direct3D 9)

A blending stage is a set of texture operations and their arguments that define how textures are blended. When making a blending stage, C++ applications invoke the [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate) method. The first call specifies the operation that is performed. Two additional invocations define the arguments to which the operation is applied. The following code example illustrates the creation of a blending stage.


```
// This example assumes that lpD3DDev is a valid pointer to an
// IDirect3DDevice9 interface.

// Set the operation for the first texture.
d3dDevice->SetTextureStageState(0, D3DTSS_COLOROP, D3DTOP_ADD);

// Set argument 1 to the texture color.
d3dDevice->SetTextureStageState(0, D3DTSS_COLORARG1, D3DTA_TEXTURE);

// Set argument 2 to the iterated diffuse color.
d3dDevice->SetTextureStageState(0, D3DTSS_COLORARG2, D3DTA_DIFFUSE);
```



Texel data in textures contain color and alpha values. Applications can define separate operations for both color and alpha values in a single blending stage. Each operation, color, and alpha, has its own arguments. For details, see [**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md).

Although not part of the Direct3D API, you can insert the following macros into your application to abbreviate the code required for creating texture blending stages.


```
#define SetTextureColorStage( dev, i, arg1, op, arg2 )     \
    dev->SetTextureStageState( i, D3DTSS_COLOROP, op);      \
    dev->SetTextureStageState( i, D3DTSS_COLORARG1, arg1 ); \
    dev->SetTextureStageState( i, D3DTSS_COLORARG2, arg2 );

#define SetTextureAlphaStage( dev, i, arg1, op, arg2 )     \
    dev->SetTextureStageState( i, D3DTSS_ALPHAOP, op);      \
    dev->SetTextureStageState( i, D3DTSS_ALPHAARG1, arg1 );  \
    dev->SetTextureStageState( i  D3DTSS_ALPHAARG2, arg2 );
```



## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> </dl>

 

 
