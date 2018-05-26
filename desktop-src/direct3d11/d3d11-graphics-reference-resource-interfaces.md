---
title: Resource Interfaces
description: There are a number of interfaces for the two basic types of resources buffers and textures.
ms.assetid: 8e40573a-b186-41ec-b2ff-81279d77bd3a
keywords:
- interfaces, Direct3D 11 Resource
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Interfaces

There are a number of interfaces for the two basic types of resources: buffers and textures. There are also interfaces for views of resources.

An application uses a view to bind a resource to a pipeline stage. The view defines how the resource can be accessed during rendering. This section describes the view interfaces.

## 

## In this section



| Topic                                                                       | Description                                                                                                                                                                                            |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D11Buffer**](/windows/win32/D3D11/nn-d3d11-id3d11buffer?branch=master)<br/>                             | A buffer interface accesses a buffer resource, which is unstructured memory. Buffers typically store vertex or index data.<br/>                                                                  |
| [**ID3D11DepthStencilView**](/windows/win32/D3D11/nn-d3d11-id3d11depthstencilview?branch=master)<br/>         | A depth-stencil-view interface accesses a texture resource during depth-stencil testing.<br/>                                                                                                    |
| [**ID3D11RenderTargetView**](/windows/win32/D3D11/nn-d3d11-id3d11rendertargetview?branch=master)<br/>         | A render-target-view interface identifies the render-target subresources that can be accessed during rendering.<br/>                                                                             |
| [**ID3D11RenderTargetView1**](/windows/win32/D3D11_3/nn-d3d11_3-id3d11rendertargetview1?branch=master)<br/>       | A render-target-view interface represents the render-target subresources that can be accessed during rendering.<br/>                                                                             |
| [**ID3D11Resource**](/windows/win32/D3D11/nn-d3d11-id3d11resource?branch=master)<br/>                         | A resource interface provides common actions on all resources.<br/>                                                                                                                              |
| [**ID3D11ShaderResourceView**](/windows/win32/D3D11/nn-d3d11-id3d11shaderresourceview?branch=master)<br/>     | A shader-resource-view interface specifies the subresources a shader can access during rendering. Examples of shader resources include a constant buffer, a texture buffer, and a texture.<br/>  |
| [**ID3D11ShaderResourceView1**](/windows/win32/D3D11_3/nn-d3d11_3-id3d11shaderresourceview1?branch=master)<br/>   | A shader-resource-view interface represents the subresources a shader can access during rendering. Examples of shader resources include a constant buffer, a texture buffer, and a texture.<br/> |
| [**ID3D11Texture1D**](/windows/win32/D3D11/nn-d3d11-id3d11texture1d?branch=master)<br/>                       | A 1D texture interface accesses texel data, which is structured memory.<br/>                                                                                                                     |
| [**ID3D11Texture2D**](/windows/win32/D3D11/nn-d3d11-id3d11texture2d?branch=master)<br/>                       | A 2D texture interface manages texel data, which is structured memory.<br/>                                                                                                                      |
| [**ID3D11Texture2D1**](/windows/win32/D3D11_3/nn-d3d11_3-id3d11texture2d1?branch=master)<br/>                     | A 2D texture interface represents texel data, which is structured memory.<br/>                                                                                                                   |
| [**ID3D11Texture3D**](/windows/win32/D3D11/nn-d3d11-id3d11texture3d?branch=master)<br/>                       | A 3D texture interface accesses texel data, which is structured memory.<br/>                                                                                                                     |
| [**ID3D11Texture3D1**](/windows/win32/D3D11_3/nn-d3d11_3-id3d11texture3d1?branch=master)<br/>                     | A 3D texture interface represents texel data, which is structured memory.<br/>                                                                                                                   |
| [**ID3D11UnorderedAccessView**](/windows/win32/D3D11/nn-d3d11-id3d11unorderedaccessview?branch=master)<br/>   | A view interface specifies the parts of a resource the pipeline can access during rendering.<br/>                                                                                                |
| [**ID3D11UnorderedAccessView1**](/windows/win32/D3D11_3/nn-d3d11_3-id3d11unorderedaccessview1?branch=master)<br/> | An unordered-access-view interface represents the parts of a resource the pipeline can access during rendering.<br/>                                                                             |
| [**ID3D11View**](/windows/win32/D3D11/nn-d3d11-id3d11view?branch=master)<br/>                                 | A view interface specifies the parts of a resource the pipeline can access during rendering.<br/>                                                                                                |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d11-graphics-reference-resource.md)
</dt> </dl>

 

 





