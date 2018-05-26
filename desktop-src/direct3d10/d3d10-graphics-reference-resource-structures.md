---
Description: Structures used to create and use resources.
ms.assetid: d8fe2ebe-349a-456e-9a5a-16f2d3419800
title: Resource Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Structures

Structures used to create and use [resources](d3d10-graphics-programming-guide-resources-types.md).



| Structures                                                                 | Description                                                                                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D10\_BUFFER\_DESC**](/windows/win32/D3D10/ns-d3d10-cd3d10_buffer_desc?branch=master)                           | Description of a [buffer](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                     |
| [**D3D10\_BUFFER\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_buffer_rtv?branch=master)                             | Describes the elements in a [buffer](d3d10-graphics-programming-guide-resources-types.md) to be used in a render-target view.                                |
| [**D3D10\_BUFFER\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_buffer_srv?branch=master)                             | Describes the elements in a [buffer](d3d10-graphics-programming-guide-resources-types.md) resource to use in a shader-resource view.                         |
| [**D3D10\_DEPTH\_STENCIL\_VIEW\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_depth_stencil_view_desc?branch=master) | Describes a depth-stencil view.                                                                                                                               |
| [**D3D10\_MAPPED\_TEXTURE2D**](/windows/win32/D3D10/ns-d3d10-d3d10_mapped_texture2d?branch=master)                 | Provides access to subresource data in a [2D texture](d3d10-graphics-programming-guide-resources-types.md).                                                  |
| [**D3D10\_MAPPED\_TEXTURE3D**](/windows/win32/D3D10/ns-d3d10-d3d10_mapped_texture3d?branch=master)                 | Provides access to subresource data in a [3D texture](d3d10-graphics-programming-guide-resources-types.md).                                                  |
| [**D3D10\_RENDER\_TARGET\_VIEW\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_render_target_view_desc?branch=master) | Describes a render-target view.                                                                                                                               |
| [**D3D10\_SUBRESOURCE\_DATA**](/windows/win32/D3D10/ns-d3d10-d3d10_subresource_data?branch=master)                 | Specifies data for initializing a resource.                                                                                                                   |
| [**D3D10\_TEX1D\_ARRAY\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_array_dsv?branch=master)                  | Specifies which mipmap level and textures in a [1D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.       |
| [**D3D10\_TEX1D\_ARRAY\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_array_rtv?branch=master)                  | Specifies the subresource(s) from an array of [1D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.             |
| [**D3D10\_TEX1D\_ARRAY\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_array_srv?branch=master)                  | Specifies the mipmap levels and textures in a [1D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.      |
| [**D3D10\_TEX1D\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_dsv?branch=master)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.                        |
| [**D3D10\_TEX1D\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_rtv?branch=master)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX1D\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex1d_srv?branch=master)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEX2D\_ARRAY\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_array_dsv?branch=master)                  | Specifies which mipmap level and which textures in a [2D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view. |
| [**D3D10\_TEX2D\_ARRAY\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_array_rtv?branch=master)                  | Specifies which mipmap level and which textures in a [2D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view. |
| [**D3D10\_TEX2D\_ARRAY\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_array_srv?branch=master)                  | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.           |
| [**D3D10\_TEX2D\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_dsv?branch=master)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.                        |
| [**D3D10\_TEX2D\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_rtv?branch=master)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX2D\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2d_srv?branch=master)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEX2DMS\_ARRAY\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_array_dsv?branch=master)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.             |
| [**D3D10\_TEX2DMS\_ARRAY\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_array_rtv?branch=master)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.             |
| [**D3D10\_TEX2DMS\_ARRAY\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_array_srv?branch=master)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.           |
| [**D3D10\_TEX2DMS\_DSV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_dsv?branch=master)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.           |
| [**D3D10\_TEX2DMS\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_rtv?branch=master)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.           |
| [**D3D10\_TEX2DMS\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex2dms_srv?branch=master)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.         |
| [**D3D10\_TEX3D\_RTV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex3d_rtv?branch=master)                               | Specifies the subresource(s) from a [3D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX3D\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_tex3d_srv?branch=master)                               | Specifies the subresource(s) from a [3D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEXCUBE\_ARRAY\_SRV1**](/windows/win32/d3d10_1/ns-d3d10_1-d3d10_texcube_array_srv1?branch=master)            | Specifies the subresource(s) from a [cube texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                    |
| [**D3D10\_TEXCUBE\_SRV**](/windows/win32/D3D10/ns-d3d10-d3d10_texcube_srv?branch=master)                           | Specifies the subresource(s) from a [cube texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                    |
| [**D3D10\_TEXTURE1D\_DESC**](/windows/win32/D3D10/ns-d3d10-cd3d10_texture1d_desc?branch=master)                     | Describes a [1D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |
| [**D3D10\_TEXTURE2D\_DESC**](/windows/win32/D3D10/ns-d3d10-cd3d10_texture2d_desc?branch=master)                     | Describes a [2D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |
| [**D3D10\_TEXTURE3D\_DESC**](/windows/win32/D3D10/ns-d3d10-cd3d10_texture3d_desc?branch=master)                     | Describes a [3D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d10-graphics-reference-resource.md)
</dt> </dl>

 

 



