---
title: Textures
description: This section describes textures that are used in Direct3D 11 and links to task-based documentation for common scenarios.
ms.assetid: ec833431-a7b4-4aea-91c8-e99b718de2c6
ms.topic: article
ms.date: 05/31/2018
---

# Textures

A texture stores texel information. This section describes textures that are used in Direct3D 11 and links to task-based documentation for common scenarios.

## In this section



| Topic                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Introduction To Textures in Direct3D 11](overviews-direct3d-11-resources-textures-intro.md)<br/> | A texture resource is a structured collection of data designed to store texels. A texel represents the smallest unit of a texture that can be read or written to by the pipeline. Unlike buffers, textures can be filtered by texture samplers as they are read by shader units. The type of texture impacts how the texture is filtered. Each texel contains 1 to 4 components, arranged in one of the DXGI formats defined by the DXGI\_FORMAT enumeration.<br/> |
| [Texture Block Compression in Direct3D 11](texture-block-compression-in-direct3d-11.md)<br/>      | Block Compression (BC) support for textures has been extended in Direct3D 11 to include the BC6H and BC7 algorithms. BC6H supports high-dynamic range color source data, and BC7 provides better-than-average quality compression with less artifacts for standard RGB source data.<br/>                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[How to: Create a Texture](overviews-direct3d-11-resources-textures-create.md)
</dt> <dt>

[How to: Initialize a Texture Programmatically](overviews-direct3d-11-resources-textures-how-to-fill-manually.md)
</dt> <dt>

[How to: Initialize a Texture From a File](overviews-direct3d-11-resources-textures-how-to.md)
</dt> <dt>

[Resources](overviews-direct3d-11-resources.md)
</dt> </dl>

 

 





