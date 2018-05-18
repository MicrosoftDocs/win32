---
title: Resource Interfaces
description: There are a number of interfaces for the two basic types of resources buffers and textures.
ms.assetid: '8e40573a-b186-41ec-b2ff-81279d77bd3a'
keywords: ["interfaces, Direct3D 11 Resource"]
---

# Resource Interfaces

There are a number of interfaces for the two basic types of resources: buffers and textures. There are also interfaces for views of resources.

An application uses a view to bind a resource to a pipeline stage. The view defines how the resource can be accessed during rendering. This section describes the view interfaces.

## 

## In this section



| Topic                                                                       | Description                                                                                                                                                                                            |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D11Buffer**](id3d11buffer.md)<br/>                             | A buffer interface accesses a buffer resource, which is unstructured memory. Buffers typically store vertex or index data.<br/>                                                                  |
| [**ID3D11DepthStencilView**](id3d11depthstencilview.md)<br/>         | A depth-stencil-view interface accesses a texture resource during depth-stencil testing.<br/>                                                                                                    |
| [**ID3D11RenderTargetView**](id3d11rendertargetview.md)<br/>         | A render-target-view interface identifies the render-target subresources that can be accessed during rendering.<br/>                                                                             |
| [**ID3D11RenderTargetView1**](id3d11rendertargetview1.md)<br/>       | A render-target-view interface represents the render-target subresources that can be accessed during rendering.<br/>                                                                             |
| [**ID3D11Resource**](id3d11resource.md)<br/>                         | A resource interface provides common actions on all resources.<br/>                                                                                                                              |
| [**ID3D11ShaderResourceView**](id3d11shaderresourceview.md)<br/>     | A shader-resource-view interface specifies the subresources a shader can access during rendering. Examples of shader resources include a constant buffer, a texture buffer, and a texture.<br/>  |
| [**ID3D11ShaderResourceView1**](id3d11shaderresourceview1.md)<br/>   | A shader-resource-view interface represents the subresources a shader can access during rendering. Examples of shader resources include a constant buffer, a texture buffer, and a texture.<br/> |
| [**ID3D11Texture1D**](id3d11texture1d.md)<br/>                       | A 1D texture interface accesses texel data, which is structured memory.<br/>                                                                                                                     |
| [**ID3D11Texture2D**](id3d11texture2d.md)<br/>                       | A 2D texture interface manages texel data, which is structured memory.<br/>                                                                                                                      |
| [**ID3D11Texture2D1**](id3d11texture2d1.md)<br/>                     | A 2D texture interface represents texel data, which is structured memory.<br/>                                                                                                                   |
| [**ID3D11Texture3D**](id3d11texture3d.md)<br/>                       | A 3D texture interface accesses texel data, which is structured memory.<br/>                                                                                                                     |
| [**ID3D11Texture3D1**](id3d11texture3d1.md)<br/>                     | A 3D texture interface represents texel data, which is structured memory.<br/>                                                                                                                   |
| [**ID3D11UnorderedAccessView**](id3d11unorderedaccessview.md)<br/>   | A view interface specifies the parts of a resource the pipeline can access during rendering.<br/>                                                                                                |
| [**ID3D11UnorderedAccessView1**](id3d11unorderedaccessview1.md)<br/> | An unordered-access-view interface represents the parts of a resource the pipeline can access during rendering.<br/>                                                                             |
| [**ID3D11View**](id3d11view.md)<br/>                                 | A view interface specifies the parts of a resource the pipeline can access during rendering.<br/>                                                                                                |



 

## Related topics

<dl> <dt>

[Resource Reference](d3d11-graphics-reference-resource.md)
</dt> </dl>

 

 





