---
title: Resource Enumerations
description: Enumerations are used to specify information about how resources are created and accessed during rendering.
ms.assetid: 'b547819b-7006-40b5-84a4-adf198048051'
keywords: ["enumerations, Direct3D 11 Resource"]
---

# Resource Enumerations

Enumerations are used to specify information about how resources are created and accessed during rendering.

## 

## In this section



| Topic                                                                                                               | Description                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D11\_BIND\_FLAG**](d3d11-bind-flag.md)<br/>                                                             | Identifies how to bind a resource to the pipeline.<br/>                                                                                                                                 |
| [**D3D11\_BUFFEREX\_SRV\_FLAG**](d3d11-bufferex-srv-flag.md)<br/>                                            | Identifies how to view a buffer resource.<br/>                                                                                                                                          |
| [**D3D11\_BUFFER\_UAV\_FLAG**](d3d11-buffer-uav-flag.md)<br/>                                                | Identifies unordered-access view options for a buffer resource.<br/>                                                                                                                    |
| [**D3D11\_CHECK\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](d3d11-check-multisample-quality-levels-flags.md)<br/> | Identifies how to check multisample quality levels.<br/>                                                                                                                                |
| [**D3D11\_CPU\_ACCESS\_FLAG**](d3d11-cpu-access-flag.md)<br/>                                                | Specifies the types of CPU access allowed for a resource.<br/>                                                                                                                          |
| [**D3D11\_DSV\_DIMENSION**](d3d11-dsv-dimension.md)<br/>                                                     | Specifies how to access a resource used in a depth-stencil view.<br/>                                                                                                                   |
| [**D3D11\_DSV\_FLAG**](d3d11-dsv-flag.md)<br/>                                                               | Depth-stencil view options.<br/>                                                                                                                                                        |
| [**D3D11\_MAP**](d3d11-map.md)<br/>                                                                          | Identifies a resource to be accessed for reading and writing by the CPU. Applications may combine one or more of these flags.<br/>                                                      |
| [**D3D11\_MAP\_FLAG**](d3d11-map-flag.md)<br/>                                                               | Specifies how the CPU should respond when an application calls the [**ID3D11DeviceContext::Map**](id3d11devicecontext-map.md) method on a resource that is being used by the GPU.<br/> |
| [**D3D11\_RESOURCE\_DIMENSION**](d3d11-resource-dimension.md)<br/>                                           | Identifies the type of resource being used.<br/>                                                                                                                                        |
| [**D3D11\_RESOURCE\_MISC\_FLAG**](d3d11-resource-misc-flag.md)<br/>                                          | Identifies options for resources.<br/>                                                                                                                                                  |
| [**D3D11\_RTV\_DIMENSION**](d3d11-rtv-dimension.md)<br/>                                                     | These flags identify the type of resource that will be viewed as a render target.<br/>                                                                                                  |
| [**D3D11\_SRV\_DIMENSION**](d3d11-srv-dimension.md)<br/>                                                     | These flags identify the type of resource that will be viewed as a shader resource.<br/>                                                                                                |
| [**D3D11\_STANDARD\_MULTISAMPLE\_QUALITY\_LEVELS**](d3d11-standard-multisample-quality-levels.md)<br/>       | Specifies a multi-sample pattern type.<br/>                                                                                                                                             |
| [**D3D11\_TEXTURE\_LAYOUT**](d3d11-texture-layout.md)<br/>                                                   | Specifies texture layout options.<br/>                                                                                                                                                  |
| [**D3D11\_TILE\_COPY\_FLAG**](d3d11-tile-copy-flags.md)<br/>                                                 | Identifies how to copy a tile.<br/>                                                                                                                                                     |
| [**D3D11\_TILE\_MAPPING\_FLAG**](d3d11-tile-mapping-flags.md)<br/>                                           | Identifies how to perform a tile-mapping operation.<br/>                                                                                                                                |
| [**D3D11\_TILE\_RANGE\_FLAG**](d3d11-tile-range-flag.md)<br/>                                                | Specifies a range of tile mappings to use with [**ID3D11DeviceContext2::UpdateTiles**](id3d11devicecontext2-updatetiles.md).<br/>                                                      |
| [**D3D11\_UAV\_DIMENSION**](d3d11-uav-dimension.md)<br/>                                                     | Unordered-access view options.<br/>                                                                                                                                                     |
| [**D3D11\_USAGE**](d3d11-usage.md)<br/>                                                                      | Identifies expected resource use during rendering. The usage directly reflects whether a resource is accessible by the CPU and/or the graphics processing unit (GPU).<br/>              |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d11-graphics-reference-resource.md)
</dt> </dl>

 

 





