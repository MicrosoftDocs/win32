---
description: This table contains a list of the minimum resources supported by Direct3D 10.
ms.assetid: 79c13aed-87bd-4875-9810-c3e078f58753
title: Resource Limits (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Resource Limits (Direct3D 10)

This table contains a list of the minimum resources supported by Direct3D 10.



| Resource                                                                                               | Limit                                                |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Number of elements in a constant buffer                                                                | 4096                                                 |
| Number of texels (independent of struct size) in a buffer                                              | 227 texels                                           |
| Texture1D U dimension                                                                                  | 8192                                                 |
| Texture1DArray dimension                                                                               | 512 Array Slices                                     |
| Texture2D U/V dimension                                                                                | 8192                                                 |
| Texture2DArray dimension                                                                               | 512 Array Slices                                     |
| Texture3D U/V/W dimension                                                                              | 2048                                                 |
| TextureCube dimension                                                                                  | 8192                                                 |
| Resource size (in MB)                                                                                  | 128 MB¹                                              |
| Anisotropic filtering maxanisotropy                                                                    | 16                                                   |
| Resource dimension addressable by filtering hardware                                                   | 8192 per dimension                                   |
| Resource size (in MB) addressable by IA (input or vertex data) or VS/GS/PS (point sample)              | 128 MB¹                                              |
| Total number of resource views per context (Each array counts as 1) (all view types have shared limit) | 220                                                  |
| Buffer structure size (multi-element)                                                                  | 2048 bytes                                           |
| Stream output size                                                                                     | Same as the number of texels in a buffer (see above) |
| Draw or DrawInstanced vertex count (including instancing)                                              | 232                                                  |
| DrawIndexed\[Instanced\]() vertex count (incl. instancing)                                             | 232                                                  |
| GS invocation output data (components \* vertices)                                                     | 1024                                                 |
| Total number of sampler objects per context                                                            | 4096                                                 |
| Total number of viewport/scissor objects per pipeline                                                  | 16                                                   |
| Total number of clip/cull distances per vertex                                                         | 8                                                    |
| Total number of blend objects per context                                                              | 4096                                                 |
| Total number of depth/stencil objects per context                                                      | 4096                                                 |
| Total number of rasterizer state objects per context                                                   | 4096                                                 |
| Maximum per-pixel sample count during multisampling                                                    | 32                                                   |
| Shader resource vertex-element count (four 32-bit components)                                          | 16                                                   |
| Common-shader core (four 32-bit components) temp-register count (r\# + indexable x\#\[n\])             | 4096                                                 |
| Common-shader core constant-buffer slots                                                               | 14                                                   |
| Common-shader core input-resource slots                                                                | 128                                                  |
| Common-shader core sampler slots                                                                       | 16                                                   |
| Common-shader core subroutine-nesting limit                                                            | 32                                                   |
| Common-shader core flow-control nesting limit                                                          | 64                                                   |
| Vertex shader input-register count (four 32-bit components)                                            | 16                                                   |
| Vertex shader output-register count (four 32-bit components)                                           | 16                                                   |
| Geometry shader input-register count (four 32-bit components)                                          | 16                                                   |
| Geometry shader output-register count (four 32-bit components)                                         | 32                                                   |
| Pixel shader input-register count (four 32-bit components)                                             | 32                                                   |
| Pixel shader output-register count (four 32-bit components)                                            | 8                                                    |
| Pixel shader output depth register count(32-bit\*1-component)                                          | 1                                                    |
| Input assembler index input resource slots                                                             | 1                                                    |
| Input assembler vertex input resource slots                                                            | 16                                                   |



 

¹Apps can create resources bigger than the maximum resource size on some graphics hardware. However, we recommend that apps keep resources smaller than the maximum resource size to get the maximum amount of compatibility across graphics vendors. The runtime only guarantees that allocations within the maximum resource size are supported by all Direct3D 10 hardware. If an app tries to allocate memory for a resource within the maximum resource size, the runtime fails the attempt only if the operating system runs out of resources. If an app tries to allocate memory for a resource above the maximum resource size, the runtime can fail the attempt because either the operating system is overextended or the hardware does not support allocations above the maximum resource size.

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 



