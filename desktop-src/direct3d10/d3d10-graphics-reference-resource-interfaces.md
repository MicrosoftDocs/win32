---
Description: Direct3D 10 defines a number of interfaces for the two basic types of resources buffers and textures.
ms.assetid: e53ca7ab-6ca5-4774-8a52-825b10c1a2ce
title: Resource Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Interfaces

Direct3D 10 defines a number of interfaces for the two basic types of resources: [buffers](d3d10-graphics-programming-guide-resources-types.md) and textures.



| Interfaces                                           | Description                                          |
|------------------------------------------------------|------------------------------------------------------|
| [**ID3D10Buffer Interface**](/windows/win32/D3D10/nn-d3d10-id3d10buffer?branch=master)       | Accesses buffer data.                                |
| [**ID3D10Resource Interface**](/windows/win32/D3D10/nn-d3d10-id3d10resource?branch=master)   | Base class for a resource.                           |
| [**ID3D10Texture1D Interface**](/windows/win32/D3D10/nn-d3d10-id3d10texture1d?branch=master) | Accesses data in a 1D texture or a 1D texture array. |
| [**ID3D10Texture2D Interface**](/windows/win32/D3D10/nn-d3d10-id3d10texture2d?branch=master) | Accesses data in a 2D texture or a 2D texture array  |
| [**ID3D10Texture3D Interface**](/windows/win32/D3D10/nn-d3d10-id3d10texture3d?branch=master) | Accesses data in a 3D texture or a 3D texture array. |



 

An application uses a view to bind a resource to a [pipeline stage](d3d10-graphics-programming-guide-pipeline-stages.md). The [view](d3d10-graphics-programming-guide-resources-access-views.md) defines how the resource can be accessed during rendering. The API contains these view interfaces.



| Interfaces                                                               | Description                                                                                                  |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ID3D10DepthStencilView Interface**](/windows/win32/D3D10/nn-d3d10-id3d10depthstencilview?branch=master)       | Accesses data in a [depth-stencil](direct3d10.d3d10_graphics_programming_guide_output_merger_stage) texture. |
| [**ID3D10RenderTargetView Interface**](/windows/win32/D3D10/nn-d3d10-id3d10rendertargetview?branch=master)       | Accesses data in a [render target](d3d10-graphics-programming-guide-resources-creating-textures.md).        |
| [**ID3D10ShaderResourceView Interface**](/windows/win32/d3d10/nn-d3d10-id3d10shaderresourceview?branch=master)   | Accesses data in a shader-resource in Direct3D 10.0.                                                         |
| [**ID3D10ShaderResourceView1 Interface**](/windows/win32/d3d10_1/nn-d3d10_1-id3d10shaderresourceview1?branch=master) | Accesses data in a shader-resource in Direct3D 10.1.                                                         |
| [**ID3D10View Interface**](/windows/win32/D3D10/nn-d3d10-id3d10view?branch=master)                               | Base class for a view.                                                                                       |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d10-graphics-reference-resource.md)
</dt> </dl>

 

 



