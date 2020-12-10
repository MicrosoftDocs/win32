---
title: Subresources (Direct3D 11 Graphics)
description: This topic describes texture subresources, or portions of a resource.
ms.assetid: 57444cb5-6c8b-4dac-8d6b-ca2b45eafac9
ms.topic: article
ms.date: 05/31/2018
---

# Subresources (Direct3D 11 Graphics)

This topic describes texture subresources, or portions of a resource.

Direct3D can reference an entire resource or it can reference subsets of a resource. The term subresource refers to a subset of a resource.

A buffer is defined as a single subresource. Textures are a little more complicated because there are several different texture types (1D, 2D, etc.) some of which support mipmap levels and/or texture arrays. Beginning with the simplest case, a 1D texture is defined as a single subresource, as shown in the following illustration.

![illustration of a 1d texture](images/d3d10-1d-texture.png)

This means that the array of texels that make up a 1D texture are contained in a single subresource.

If you expand a 1D texture with three mipmap levels, it can be visualized like the following illustration.

![illustration of a 1d texture with three mipmap levels](images/d3d10-resource-texture1d.png)

Think of this as a single texture that is made up of three subresources. A subresource can be indexed using the level-of-detail (LOD) for a single texture. When using an array of textures, accessing a particular subresource requires both the LOD and the particular texture. Alternately, the API combines these two pieces of information into a single zero-based subresource index, as shown in the following illustration.

![illustration of a zero-based subresource index](images/d3d10-resource-texture1darray-sub-indexing.png)

## Selecting Subresources

Some APIs access an entire resource (for example the [**ID3D11DeviceContext::CopyResource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copyresource) method), others access a portion of a resource (for example the [**ID3D11DeviceContext::UpdateSubresource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-updatesubresource) method or the [**ID3D11DeviceContext::CopySubresourceRegion**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copysubresourceregion) method). The methods that access a portion of a resource generally use a view description (such as the [**D3D11\_TEX2D\_ARRAY\_DSV**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_tex2d_array_dsv) structure) to specify the subresources to access.

The illustrations in the following sections show the terms used by a view description when accessing an array of textures.

### Array Slice

Given an array of textures, each texture with mipmaps, an *array slice* (represented by the white rectangle) includes one texture and all of its subresources, as shown in the following illustration.

![illustration of an array slice](images/d3d10-resource-array-slice.png)

### Mip Slice

A *mip slice* (represented by the white rectangle) includes one mipmap level for every texture in an array, as shown in the following illustration.

![illustration of a mip slice](images/d3d10-resource-mip-slice.png)

### Selecting a Single Subresource

You can use these two types of slices to choose a single subresource, as shown in the following illustration.

![illustration of choosing a subresource by using an array slice and a mip slice](images/d3d10-resource-subresources-1.png)

### Selecting Multiple Subresources

Or you can use these two types of slices with the number of mipmap levels and/or number of textures, to choose multiple subresources, as shown in the following illustration.

![illustration of choosing multiple subresource](images/d3d10-resource-subresources-2.png)

> [!Note]  
> A [**render-target view**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_render_target_view_desc) can only use a single subresource or mip slice and cannot include subresources from more than one mip slice. That is, every texture in a render-target view must be the same size. A [**shader-resource view**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_shader_resource_view_desc) can select any rectangular region of subresources, as shown in the figure.

 

## Related topics

<dl> <dt>

[Resources](overviews-direct3d-11-resources.md)
</dt> </dl>

 

 




