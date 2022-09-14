---
title: Why are tiled resources needed
description: Tiled resources are needed so less graphics processing unit (GPU) memory is wasted storing regions of surfaces that the application knows will not be accessed, and the hardware can understand how to filter across adjacent tiles.
ms.assetid: E2179D65-56D3-481F-A5F3-B9C45A11A179
ms.topic: article
ms.date: 05/31/2018
---

# Why are tiled resources needed?

Tiled resources are needed so less graphics processing unit (GPU) memory is wasted storing regions of surfaces that the application knows will not be accessed, and the hardware can understand how to filter across adjacent tiles.

In a graphics system (that is, the operating system, display driver, and graphics hardware) without tiled resource support, the graphics system manages all Direct3D memory allocations at subresource granularity. For a [Buffer](overviews-direct3d-11-resources-buffers.md), the entire Buffer is the subresource. For a [Texture](overviews-direct3d-11-resources-textures.md) (for example, [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d)), each mip level is a subresource; for a texture array (for example, [**Texture2DArray**](/windows/desktop/direct3dhlsl/sm5-object-texture2darray)), each mip level at a given array slice is a subresource. The graphics system only exposes the ability to manage the mapping of allocations at this subresource granularity. In the context of tiled resources, "mapping" refers to making data visible to the GPU.

Suppose an application knows that a particular rendering operation only needs to access a small portion of an image mipmap chain (perhaps not even the full area of a given mipmap). Ideally, the app could inform the graphics system about this need. The graphics system would then only bother to ensure that the needed memory is mapped on the GPU without paging in too much memory. In reality, without tiled resource support, the graphics system can only be informed about the memory that needs to be mapped on the GPU at subresource granularity (for example, a range of full mipmap levels that could be accessed). There is no demand faulting in the graphics system either, so potentially a lot of excess GPU memory must be used to make full subresources mapped before a rendering command that references any part of the memory is executed. This is just one issue that makes the use of large memory allocations difficult in Direct3D without tiled resource support.

Direct3D 11 supports [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) surfaces with up to 16384 pixels on a given side. An image that is 16384 wide by 16384 tall and 4 bytes per pixel would consume 1GB of video memory (and adding mipmaps would double that amount). In practice, all 1GB would rarely need to be referenced in a single rendering operation.

Some game developers model terrain surfaces as large as 128K by 128K. The way they get this to work on existing GPUs is to break the surface into tiles that are small enough for hardware to handle. The application must figure out which tiles might be needed and load them into a cache of textures on the GPU - a software paging system. A significant downside to this approach comes from the hardware not knowing anything about the paging that is going on: When a part of an image needs to be shown on screen that straddles tiles, the hardware does not know how to perform fixed function (that is, efficient) filtering across tiles. This means the application managing its own software tiling must resort to manual texture filtering in shader code (which becomes very expensive if a good quality anisotropic filter is desired) and/or waste memory authoring gutters around tiles that contain data from neighboring tiles so that fixed function hardware filtering can continue to provide some assistance.

If a tiled representation of surface allocations could be a first class feature in the graphics system, the application could tell the hardware which tiles to make available. In this way, less GPU memory is wasted storing regions of surfaces that the application knows will not be accessed, and the hardware can understand how to filter across adjacent tiles, alleviating some of the pain experienced by developers who perform software tiling on their own.

But to provide a complete solution, something must be done to deal with the fact that, independent of whether tiling within a surface is supported, the maximum surface dimension is currently 16384 - nowhere near the 128K+ that applications already want. Just requiring the hardware to support larger texture sizes is one approach, however there are significant costs and/or tradeoffs to going this route. Direct3D 11's texture filter path and rendering path are already saturated in terms of precision in supporting 16K textures with the other requirements, such as supporting viewport extents falling off the surface during rendering, or supporting texture wrapping off the surface edge during filtering. A possibility is to define a tradeoff such that as the texture size increases beyond 16K, functionality/precision is given up in some manner. Even with this concession however, additional hardware costs might be required in terms of addressing capability throughout the hardware system to go to larger texture sizes.

One issue that comes into play as textures get very large is that single precision floating point texture coordinates (and the associated interpolators to support rasterization) run out of precision to specify locations on the surface accurately. Jittery texture filtering would ensue. One expensive option would be to require double precision interpolator support, though that could be overkill given a reasonable alternative.

An alternate name for tiled resources is "sparse texture." "Sparse" conveys both the tiled nature of the resources as well as perhaps the primary reason for tiling them - that not all of them are expected to be mapped at once. In fact, an application could conceivably author a tiled resource in which no data is authored for all regions+mips of the resource, intentionally. So, the content itself could be sparse, and the mapping of the content in GPU memory at a given time would be a subset of that (even more sparse).

Another scenario that could be served by tiled resources is enabling multiple resources of different dimensions/formats to share the same memory. Sometimes applications have exclusive sets of resources that are known not to be used at the same time, or resources that are created only for very brief use and then destroyed, followed by creation of other resources. A form of generality that can fall out of "tiled resources" is that it is possible to allow the user to point multiple different resources at the same (overlapping) memory. In other words, the creation and destruction of "resources" (which define a dimension/format and so on) can be decoupled from the management of the memory underlying the resources from the application's point of view.

## Related topics

<dl> <dt>

[Tiled resources](tiled-resources.md)
</dt> </dl>

 

 