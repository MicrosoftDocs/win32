---
title: How to Create a Texture
description: This topic shows how to create a texture.
ms.assetid: 'dfe88635-b2c2-48f8-a21e-cce845b518fc'
---

# How to: Create a Texture

The simplest way to create a texture is to describe its properties and call the texture creation API. This topic shows how to create a texture.

**To create a texture**

1.  Fill in a [**D3D11\_TEXTURE2D\_DESC**](d3d11-texture2d-desc.md) structure with a description of the texture parameters.
2.  Create the texture by calling [**ID3D11Device::CreateTexture2D**](id3d11device-createtexture2d.md) with the texture description.

This example creates a 256 x 256 texture, with [**dynamic usage**](d3d11-usage.md), for use as a [**shader resource**](d3d11-bind-flag.md) with [**cpu write access**](d3d11-cpu-access-flag.md).


```
D3D11_TEXTURE2D_DESC desc;
desc.Width = 256;
desc.Height = 256;
desc.MipLevels = desc.ArraySize = 1;
desc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
desc.SampleDesc.Count = 1;
desc.Usage = D3D11_USAGE_DYNAMIC;
desc.BindFlags = D3D11_BIND_SHADER_RESOURCE;
desc.CPUAccessFlags = D3D11_CPU_ACCESS_WRITE;
desc.MiscFlags = 0;

ID3D11Device *pd3dDevice; // Don't forget to initialize this
ID3D11Texture2D *pTexture = NULL;
pd3dDevice->CreateTexture2D( &amp;desc, NULL, &amp;pTexture );
```



## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Textures](overviews-direct3d-11-resources-textures.md)
</dt> </dl>

 

 




