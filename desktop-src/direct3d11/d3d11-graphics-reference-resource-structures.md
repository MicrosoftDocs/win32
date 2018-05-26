---
title: Resource Structures
description: Structures are used to create and use resources.
ms.assetid: a29e01ac-8aa1-4a40-ad4d-3b738e129436
keywords:
- structures, Direct3D 11 Resource
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Structures

Structures are used to create and use resources.

## 

## In this section



| Topic                                                                                         | Description                                                                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**D3D11\_BUFFER\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_desc?branch=master)<br/>                                   | Describes a buffer resource.<br/>                                                                           |
| [**D3D11\_BUFFER\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_rtv?branch=master)<br/>                                     | Specifies the elements in a buffer resource to use in a render-target view.<br/>                            |
| [**D3D11\_BUFFER\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_srv?branch=master)<br/>                                     | Specifies the elements in a buffer resource to use in a shader-resource view.<br/>                          |
| [**D3D11\_BUFFER\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_uav?branch=master)<br/>                                     | Describes the elements in a buffer to use in a unordered-access view.<br/>                                  |
| [**D3D11\_BUFFEREX\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_bufferex_srv?branch=master)<br/>                                 | Describes the elements in a raw buffer resource to use in a shader-resource view.<br/>                      |
| [**D3D11\_DEPTH\_STENCIL\_VIEW\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_depth_stencil_view_desc?branch=master)<br/>         | Specifies the subresources of a texture that are accessible from a depth-stencil view.<br/>                 |
| [**D3D11\_MAPPED\_SUBRESOURCE**](/windows/win32/D3D11/ns-d3d11-d3d11_mapped_subresource?branch=master)<br/>                     | Provides access to subresource data.<br/>                                                                   |
| [**D3D11\_PACKED\_MIP\_DESC**](/windows/win32/d3d11_2/ns-d3d11_2-d3d11_packed_mip_desc?branch=master)<br/>                          | Describes the tile structure of a tiled resource with mipmaps. <br/>                                        |
| [**D3D11\_RENDER\_TARGET\_VIEW\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_render_target_view_desc?branch=master)<br/>         | Specifies the subresources from a resource that are accessible using a render-target view.<br/>             |
| [**D3D11\_RENDER\_TARGET\_VIEW\_DESC1**](/windows/win32/D3D11_3/ns-d3d11_3-cd3d11_render_target_view_desc1?branch=master)<br/>       | Describes the subresources from a resource that are accessible using a render-target view.<br/>             |
| [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC**](/windows/win32/d3d11/ns-d3d11-d3d11_shader_resource_view_desc?branch=master)<br/>     | Describes a shader-resource view.<br/>                                                                      |
| [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC1**](/windows/win32/D3D11_3/ns-d3d11_3-cd3d11_shader_resource_view_desc1?branch=master)<br/>   | Describes a shader-resource view.<br/>                                                                      |
| [**D3D11\_SUBRESOURCE\_DATA**](/windows/win32/D3D11/ns-d3d11-d3d11_subresource_data?branch=master)<br/>                         | Specifies data for initializing a subresource.<br/>                                                         |
| [**D3D11\_SUBRESOURCE\_TILING**](/windows/win32/D3D11_2/ns-d3d11_2-d3d11_subresource_tiling?branch=master)<br/>                     | Describes a tiled subresource volume.<br/>                                                                  |
| [**D3D11\_TEX1D\_ARRAY\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_array_dsv?branch=master)<br/>                          | Specifies the subresources from an array of 1D textures to use in a depth-stencil view.<br/>                |
| [**D3D11\_TEX1D\_ARRAY\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_array_rtv?branch=master)<br/>                          | Specifies the subresources from an array of 1D textures to use in a render-target view.<br/>                |
| [**D3D11\_TEX1D\_ARRAY\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_array_srv?branch=master)<br/>                          | Specifies the subresources from an array of 1D textures to use in a shader-resource view.<br/>              |
| [**D3D11\_TEX1D\_ARRAY\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_array_uav?branch=master)<br/>                          | Describes an array of unordered-access 1D texture resources.<br/>                                           |
| [**D3D11\_TEX1D\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_dsv?branch=master)<br/>                                       | Specifies the subresource from a 1D texture that is accessible to a depth-stencil view.<br/>                |
| [**D3D11\_TEX1D\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_rtv?branch=master)<br/>                                       | Specifies the subresource from a 1D texture to use in a render-target view.<br/>                            |
| [**D3D11\_TEX1D\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_srv?branch=master)<br/>                                       | Specifies the subresource from a 1D texture to use in a shader-resource view.<br/>                          |
| [**D3D11\_TEX1D\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex1d_uav?branch=master)<br/>                                       | Describes a unordered-access 1D texture resource.<br/>                                                      |
| [**D3D11\_TEX2D\_ARRAY\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_array_dsv?branch=master)<br/>                          | Specifies the subresources from an array 2D textures that are accessible to a depth-stencil view.<br/>      |
| [**D3D11\_TEX2D\_ARRAY\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_array_rtv?branch=master)<br/>                          | Specifies the subresources from an array of 2D textures to use in a render-target view.<br/>                |
| [**D3D11\_TEX2D\_ARRAY\_RTV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_array_rtv1?branch=master)<br/>                        | Describes the subresources from an array of 2D textures to use in a render-target view.<br/>                |
| [**D3D11\_TEX2D\_ARRAY\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_array_srv?branch=master)<br/>                          | Specifies the subresources from an array of 2D textures to use in a shader-resource view.<br/>              |
| [**D3D11\_TEX2D\_ARRAY\_SRV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_array_srv1?branch=master)<br/>                        | Describes the subresources from an array of 2D textures to use in a shader-resource view.<br/>              |
| [**D3D11\_TEX2D\_ARRAY\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_array_uav?branch=master)<br/>                          | Describes an array of unordered-access 2D texture resources.<br/>                                           |
| [**D3D11\_TEX2D\_ARRAY\_UAV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_array_uav1?branch=master)<br/>                        | Describes an array of unordered-access 2D texture resources.<br/>                                           |
| [**D3D11\_TEX2D\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_dsv?branch=master)<br/>                                       | Specifies the subresource from a 2D texture that is accessible to a depth-stencil view.<br/>                |
| [**D3D11\_TEX2D\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_rtv?branch=master)<br/>                                       | Specifies the subresource from a 2D texture to use in a render-target view.<br/>                            |
| [**D3D11\_TEX2D\_RTV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_rtv1?branch=master)<br/>                                     | Describes the subresource from a 2D texture to use in a render-target view.<br/>                            |
| [**D3D11\_TEX2D\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_srv?branch=master)<br/>                                       | Specifies the subresource from a 2D texture to use in a shader-resource view.<br/>                          |
| [**D3D11\_TEX2D\_SRV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_srv1?branch=master)<br/>                                     | Describes the subresource from a 2D texture to use in a shader-resource view.<br/>                          |
| [**D3D11\_TEX2D\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2d_uav?branch=master)<br/>                                       | Describes a unordered-access 2D texture resource.<br/>                                                      |
| [**D3D11\_TEX2D\_UAV1**](/windows/win32/D3D11_3/ns-d3d11_3-d3d11_tex2d_uav1?branch=master)<br/>                                     | Describes a unordered-access 2D texture resource.<br/>                                                      |
| [**D3D11\_TEX2DMS\_ARRAY\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_array_dsv?branch=master)<br/>                      | Specifies the subresources from an array of multisampled 2D textures for a depth-stencil view.<br/>         |
| [**D3D11\_TEX2DMS\_ARRAY\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_array_rtv?branch=master)<br/>                      | Specifies the subresources from a an array of multisampled 2D textures to use in a render-target view.<br/> |
| [**D3D11\_TEX2DMS\_ARRAY\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_array_srv?branch=master)<br/>                      | Specifies the subresources from an array of multisampled 2D textures to use in a shader-resource view.<br/> |
| [**D3D11\_TEX2DMS\_DSV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_dsv?branch=master)<br/>                                   | Specifies the subresource from a multisampled 2D texture that is accessible to a depth-stencil view.<br/>   |
| [**D3D11\_TEX2DMS\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_rtv?branch=master)<br/>                                   | Specifies the subresource from a multisampled 2D texture to use in a render-target view.<br/>               |
| [**D3D11\_TEX2DMS\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex2dms_srv?branch=master)<br/>                                   | Specifies the subresources from a multisampled 2D texture to use in a shader-resource view.<br/>            |
| [**D3D11\_TEX3D\_RTV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex3d_rtv?branch=master)<br/>                                       | Specifies the subresources from a 3D texture to use in a render-target view.<br/>                           |
| [**D3D11\_TEX3D\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex3d_srv?branch=master)<br/>                                       | Specifies the subresources from a 3D texture to use in a shader-resource view.<br/>                         |
| [**D3D11\_TEX3D\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_tex3d_uav?branch=master)<br/>                                       | Describes a unordered-access 3D texture resource.<br/>                                                      |
| [**D3D11\_TEXCUBE\_ARRAY\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_texcube_array_srv?branch=master)<br/>                      | Specifies the subresources from an array of cube textures to use in a shader-resource view.<br/>            |
| [**D3D11\_TEXCUBE\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_texcube_srv?branch=master)<br/>                                   | Specifies the subresource from a cube texture to use in a shader-resource view.<br/>                        |
| [**D3D11\_TEXTURE1D\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_texture1d_desc?branch=master)<br/>                             | Describes a 1D texture.<br/>                                                                                |
| [**D3D11\_TEXTURE2D\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_texture2d_desc?branch=master)<br/>                             | Describes a 2D texture.<br/>                                                                                |
| [**D3D11\_TEXTURE2D\_DESC1**](/windows/win32/D3D11_3/ns-d3d11_3-cd3d11_texture2d_desc1?branch=master)<br/>                           | Describes a 2D texture.<br/>                                                                                |
| [**D3D11\_TEXTURE3D\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_texture3d_desc?branch=master)<br/>                             | Describes a 3D texture.<br/>                                                                                |
| [**D3D11\_TEXTURE3D\_DESC1**](/windows/win32/D3D11_3/ns-d3d11_3-cd3d11_texture3d_desc1?branch=master)<br/>                           | Describes a 3D texture.<br/>                                                                                |
| [**D3D11\_TILE\_REGION\_SIZE**](/windows/win32/D3D11_2/ns-d3d11_2-d3d11_tile_region_size?branch=master)<br/>                        | Describes the size of a tiled region.<br/>                                                                  |
| [**D3D11\_TILED\_RESOURCE\_COORDINATE**](/windows/win32/D3D11_2/ns-d3d11_2-d3d11_tiled_resource_coordinate?branch=master)<br/>      | Describes the coordinates of a tiled resource.<br/>                                                         |
| [**D3D11\_TILE\_SHAPE**](/windows/win32/D3D11_2/ns-d3d11_2-d3d11_tile_shape?branch=master)<br/>                                     | Describes the shape of a tile by specifying its dimensions.<br/>                                            |
| [**D3D11\_UNORDERED\_ACCESS\_VIEW\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_unordered_access_view_desc?branch=master)<br/>   | Specifies the subresources from a resource that are accessible using an unordered-access view.<br/>         |
| [**D3D11\_UNORDERED\_ACCESS\_VIEW\_DESC1**](/windows/win32/D3D11_3/ns-d3d11_3-cd3d11_unordered_access_view_desc1?branch=master)<br/> | Describes the subresources from a resource that are accessible using an unordered-access view.<br/>         |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d11-graphics-reference-resource.md)
</dt> </dl>

 

 





