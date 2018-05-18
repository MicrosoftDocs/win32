---
Description: 'Structures used to create and use resources.'
ms.assetid: 'd8fe2ebe-349a-456e-9a5a-16f2d3419800'
title: Resource Structures
---

# Resource Structures

Structures used to create and use [resources](d3d10-graphics-programming-guide-resources-types.md).



| Structures                                                                 | Description                                                                                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D10\_BUFFER\_DESC**](d3d10-buffer-desc.md)                           | Description of a [buffer](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                     |
| [**D3D10\_BUFFER\_RTV**](d3d10-buffer-rtv.md)                             | Describes the elements in a [buffer](d3d10-graphics-programming-guide-resources-types.md) to be used in a render-target view.                                |
| [**D3D10\_BUFFER\_SRV**](d3d10-buffer-srv.md)                             | Describes the elements in a [buffer](d3d10-graphics-programming-guide-resources-types.md) resource to use in a shader-resource view.                         |
| [**D3D10\_DEPTH\_STENCIL\_VIEW\_DESC**](d3d10-depth-stencil-view-desc.md) | Describes a depth-stencil view.                                                                                                                               |
| [**D3D10\_MAPPED\_TEXTURE2D**](d3d10-mapped-texture2d.md)                 | Provides access to subresource data in a [2D texture](d3d10-graphics-programming-guide-resources-types.md).                                                  |
| [**D3D10\_MAPPED\_TEXTURE3D**](d3d10-mapped-texture3d.md)                 | Provides access to subresource data in a [3D texture](d3d10-graphics-programming-guide-resources-types.md).                                                  |
| [**D3D10\_RENDER\_TARGET\_VIEW\_DESC**](d3d10-render-target-view-desc.md) | Describes a render-target view.                                                                                                                               |
| [**D3D10\_SUBRESOURCE\_DATA**](d3d10-subresource-data.md)                 | Specifies data for initializing a resource.                                                                                                                   |
| [**D3D10\_TEX1D\_ARRAY\_DSV**](d3d10-tex1d-array-dsv.md)                  | Specifies which mipmap level and textures in a [1D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.       |
| [**D3D10\_TEX1D\_ARRAY\_RTV**](d3d10-tex1d-array-rtv.md)                  | Specifies the subresource(s) from an array of [1D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.             |
| [**D3D10\_TEX1D\_ARRAY\_SRV**](d3d10-tex1d-array-srv.md)                  | Specifies the mipmap levels and textures in a [1D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.      |
| [**D3D10\_TEX1D\_DSV**](d3d10-tex1d-dsv.md)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.                        |
| [**D3D10\_TEX1D\_RTV**](d3d10-tex1d-rtv.md)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX1D\_SRV**](d3d10-tex1d-srv.md)                               | Specifies the subresource(s) from a [1D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEX2D\_ARRAY\_DSV**](d3d10-tex2d-array-dsv.md)                  | Specifies which mipmap level and which textures in a [2D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view. |
| [**D3D10\_TEX2D\_ARRAY\_RTV**](d3d10-tex2d-array-rtv.md)                  | Specifies which mipmap level and which textures in a [2D-texture array](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view. |
| [**D3D10\_TEX2D\_ARRAY\_SRV**](d3d10-tex2d-array-srv.md)                  | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.           |
| [**D3D10\_TEX2D\_DSV**](d3d10-tex2d-dsv.md)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.                        |
| [**D3D10\_TEX2D\_RTV**](d3d10-tex2d-rtv.md)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX2D\_SRV**](d3d10-tex2d-srv.md)                               | Specifies the subresource(s) from a [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEX2DMS\_ARRAY\_DSV**](d3d10-tex2dms-array-dsv.md)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.             |
| [**D3D10\_TEX2DMS\_ARRAY\_RTV**](d3d10-tex2dms-array-rtv.md)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.             |
| [**D3D10\_TEX2DMS\_ARRAY\_SRV**](d3d10-tex2dms-array-srv.md)              | Specifies the subresource(s) from an array of [2D textures](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.           |
| [**D3D10\_TEX2DMS\_DSV**](d3d10-tex2dms-dsv.md)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a depth-stencil view.           |
| [**D3D10\_TEX2DMS\_RTV**](d3d10-tex2dms-rtv.md)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.           |
| [**D3D10\_TEX2DMS\_SRV**](d3d10-tex2dms-srv.md)                           | Specifies the subresource(s) from a multisampled [2D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.         |
| [**D3D10\_TEX3D\_RTV**](d3d10-tex3d-rtv.md)                               | Specifies the subresource(s) from a [3D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a render-target view.                        |
| [**D3D10\_TEX3D\_SRV**](d3d10-tex3d-srv.md)                               | Specifies the subresource(s) from a [3D texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                      |
| [**D3D10\_TEXCUBE\_ARRAY\_SRV1**](d3d10-texcube-array-srv1.md)            | Specifies the subresource(s) from a [cube texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                    |
| [**D3D10\_TEXCUBE\_SRV**](d3d10-texcube-srv.md)                           | Specifies the subresource(s) from a [cube texture](d3d10-graphics-programming-guide-resources-types.md) to use in a shader-resource view.                    |
| [**D3D10\_TEXTURE1D\_DESC**](d3d10-texture1d-desc.md)                     | Describes a [1D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |
| [**D3D10\_TEXTURE2D\_DESC**](d3d10-texture2d-desc.md)                     | Describes a [2D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |
| [**D3D10\_TEXTURE3D\_DESC**](d3d10-texture3d-desc.md)                     | Describes a [3D texture](d3d10-graphics-programming-guide-resources-types.md) resource.                                                                      |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d10-graphics-reference-resource.md)
</dt> </dl>

 

 



