---
title: Pipeline access to tiled resources
description: Tiled resources can be used in shader resource views (SRV), render target views (RTV), depth stencil views (DSV) and unordered access views (UAV), as well as some bind points where views aren't used, such as vertex buffer bindings.
ms.assetid: D0BC0B6C-2325-4EAF-9E80-E748F58045B1
ms.topic: article
ms.date: 05/31/2018
---

# Pipeline access to tiled resources

Tiled resources can be used in shader resource views (SRV), render target views (RTV), depth stencil views (DSV) and unordered access views (UAV), as well as some bind points where views aren't used, such as vertex buffer bindings. For the list of supported bindings, see [Tiled resource creation parameters](tiled-resource-creation-parameters.md). Copy\* operations also work on tiled resources.

If multiple tile coordinates in one or more views is bound to the same memory location, reads and writes from different paths to the same memory will occur in a non-deterministic and non-repeatable order of memory accesses.

If all tiles behind a memory access footprint from a shader are mapped to unique tiles, behavior is identical on all implementations to the surface having the same memory contents in a non-tiled fashion.

This section provides more info about pipeline access to tiled resources.

## In this section



| Topic                                                                                                              | Description                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SRV behavior with non-mapped tiles](srv-behavior-with-non-mapped-tiles.md)<br/>                            | Behavior of shader resource view (SRV) reads that involve non-mapped tiles depends on the level of hardware support. <br/>                                          |
| [UAV behavior with non-mapped tiles](uav-behavior-with-non-mapped-tiles.md)<br/>                            | Behavior of unordered access view (UAV) reads and writes depends on the level of hardware support. <br/>                                                            |
| [Rasterizer behavior with non-mapped tiles](rasterizer-behavior-with-non-mapped-tiles.md)<br/>              | This section describes rasterizer behavior with non-mapped tiles.<br/>                                                                                              |
| [Tile access limitations with duplicate mappings](tile-access-limitations-with-duplicate-mappings-.md)<br/> | This section describes tile access limitations with duplicate mappings.<br/>                                                                                        |
| [Tiled resources texture sampling features](tiled-resources-texture-sampling-features.md)<br/>              | This section describes tiled resources texture sampling features.<br/>                                                                                              |
| [HLSL tiled resources exposure](hlsl-tiled-resources-exposure.md)<br/>                                      | New Microsoft High Level Shader Language (HLSL) syntax is required to support tiled resources in [Shader Model 5](/windows/desktop/direct3dhlsl/d3d11-graphics-reference-sm5). <br/> |



 

## Related topics

<dl> <dt>

[Tiled resources](tiled-resources.md)
</dt> </dl>

 

