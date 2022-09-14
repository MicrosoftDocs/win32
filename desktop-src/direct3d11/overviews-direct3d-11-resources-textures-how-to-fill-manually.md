---
title: How to Initialize a Texture Programmatically
description: This topic has several examples showing how to initialize textures that are created with different types of usages.
ms.assetid: 65e8ae82-50aa-4303-853e-3457da18f44f
ms.topic: article
ms.date: 05/31/2018
---

# How to: Initialize a Texture Programmatically

You can initialize a texture during object creation, or you can fill the object programmatically after it is created. This topic has several examples showing how to initialize textures that are created with different types of usages. This example assumes you already know how to [Create a Texture](overviews-direct3d-11-resources-textures-create.md).

-   [Default Usage](#default-usage)
-   [Dynamic Usage](#dynamic-usage)
-   [Staging Usage](#staging-usage)
-   [Related topics](#related-topics)

## Default Usage

The most common type of usage is default usage. To fill a default texture (one created with **D3D11\_USAGE\_DEFAULT**) you can either:

-   Call [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d) and initialize *pInitialData* to point to data provided from an application.

    or

-   After calling [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d), use [**ID3D11DeviceContext::UpdateSubresource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-updatesubresource) to fill the default texture with data from a pointer provided by the application.

## Dynamic Usage

To fill a dynamic texture (one created with **D3D11\_USAGE\_DYNAMIC**):

1.  Get a pointer to the texture memory by passing in **D3D11\_MAP\_WRITE\_DISCARD** when calling [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map).
2.  Write data to the memory.
3.  Call [**ID3D11DeviceContext::Unmap**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-unmap) when you are finished writing data.

## Staging Usage

To fill a staging texture (one created with **D3D11\_USAGE\_STAGING**):

1.  Get a pointer to the texture memory by passing in **D3D11\_MAP\_WRITE** when calling [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map).
2.  Write data to the memory.
3.  Call [**ID3D11DeviceContext::Unmap**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-unmap) when you are finished writing data.

A staging texture can then be used as the source parameter to [**ID3D11DeviceContext::CopyResource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copyresource) or [**ID3D11DeviceContext::CopySubresourceRegion**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copysubresourceregion) to fill a default or dynamic resource.

## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Textures](overviews-direct3d-11-resources-textures.md)
</dt> </dl>

 

 




