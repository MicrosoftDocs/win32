---
title: Resource Enumerations
description: Enumerations are used to specify information about how resources are created and accessed during rendering.
ms.assetid: b547819b-7006-40b5-84a4-adf198048051
keywords:
- enumerations, Direct3D 11 Resource
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Enumerations

Enumerations are used to specify information about how resources are created and accessed during rendering.

## 

## In this section



| Topic                                                                                                               | Description                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D11\_BIND\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_bind_flag?branch=master)<br/>                                                             | Identifies how to bind a resource to the pipeline.<br/>                                                                                                                                 |
| [**D3D11\_BUFFEREX\_SRV\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_bufferex_srv_flag?branch=master)<br/>                                            | Identifies how to view a buffer resource.<br/>                                                                                                                                          |
| [**D3D11\_BUFFER\_UAV\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_buffer_uav_flag?branch=master)<br/>                                                | Identifies unordered-access view options for a buffer resource.<br/>                                                                                                                    |
| [**D3D11\_CHECK\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](/windows/win32/D3D11_2/ne-d3d11_2-d3d11_check_multisample_quality_levels_flag?branch=master)<br/> | Identifies how to check multisample quality levels.<br/>                                                                                                                                |
| [**D3D11\_CPU\_ACCESS\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_cpu_access_flag?branch=master)<br/>                                                | Specifies the types of CPU access allowed for a resource.<br/>                                                                                                                          |
| [**D3D11\_DSV\_DIMENSION**](/windows/win32/D3D11/ne-d3d11-d3d11_dsv_dimension?branch=master)<br/>                                                     | Specifies how to access a resource used in a depth-stencil view.<br/>                                                                                                                   |
| [**D3D11\_DSV\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_dsv_flag?branch=master)<br/>                                                               | Depth-stencil view options.<br/>                                                                                                                                                        |
| [**D3D11\_MAP**](/windows/win32/D3D11/ne-d3d11-d3d11_map?branch=master)<br/>                                                                          | Identifies a resource to be accessed for reading and writing by the CPU. Applications may combine one or more of these flags.<br/>                                                      |
| [**D3D11\_MAP\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_map_flag?branch=master)<br/>                                                               | Specifies how the CPU should respond when an application calls the [**ID3D11DeviceContext::Map**](/windows/win32/D3D11/nf-d3d11-id3d11devicecontext-map?branch=master) method on a resource that is being used by the GPU.<br/> |
| [**D3D11\_RESOURCE\_DIMENSION**](/windows/win32/D3D11/ne-d3d11-d3d11_resource_dimension?branch=master)<br/>                                           | Identifies the type of resource being used.<br/>                                                                                                                                        |
| [**D3D11\_RESOURCE\_MISC\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_resource_misc_flag?branch=master)<br/>                                          | Identifies options for resources.<br/>                                                                                                                                                  |
| [**D3D11\_RTV\_DIMENSION**](/windows/win32/D3D11/ne-d3d11-d3d11_rtv_dimension?branch=master)<br/>                                                     | These flags identify the type of resource that will be viewed as a render target.<br/>                                                                                                  |
| [**D3D11\_SRV\_DIMENSION**](/windows/win32/D3D11/?branch=master)<br/>                                                     | These flags identify the type of resource that will be viewed as a shader resource.<br/>                                                                                                |
| [**D3D11\_STANDARD\_MULTISAMPLE\_QUALITY\_LEVELS**](/windows/win32/D3D11/ne-d3d11-d3d11_standard_multisample_quality_levels?branch=master)<br/>       | Specifies a multi-sample pattern type.<br/>                                                                                                                                             |
| [**D3D11\_TEXTURE\_LAYOUT**](/windows/win32/D3D11_3/ne-d3d11_3-d3d11_texture_layout?branch=master)<br/>                                                   | Specifies texture layout options.<br/>                                                                                                                                                  |
| [**D3D11\_TILE\_COPY\_FLAG**](/windows/win32/D3D11_2/ne-d3d11_2-d3d11_tile_copy_flag?branch=master)<br/>                                                 | Identifies how to copy a tile.<br/>                                                                                                                                                     |
| [**D3D11\_TILE\_MAPPING\_FLAG**](/windows/win32/D3D11_2/ne-d3d11_2-d3d11_tile_mapping_flag?branch=master)<br/>                                           | Identifies how to perform a tile-mapping operation.<br/>                                                                                                                                |
| [**D3D11\_TILE\_RANGE\_FLAG**](/windows/win32/d3d11_2/ne-d3d11_2-d3d11_tile_range_flag?branch=master)<br/>                                                | Specifies a range of tile mappings to use with [**ID3D11DeviceContext2::UpdateTiles**](/windows/win32/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetiles?branch=master).<br/>                                                      |
| [**D3D11\_UAV\_DIMENSION**](/windows/win32/D3D11/ne-d3d11-d3d11_uav_dimension?branch=master)<br/>                                                     | Unordered-access view options.<br/>                                                                                                                                                     |
| [**D3D11\_USAGE**](/windows/win32/D3D11/ne-d3d11-d3d11_usage?branch=master)<br/>                                                                      | Identifies expected resource use during rendering. The usage directly reflects whether a resource is accessible by the CPU and/or the graphics processing unit (GPU).<br/>              |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d11-graphics-reference-resource.md)
</dt> </dl>

 

 





