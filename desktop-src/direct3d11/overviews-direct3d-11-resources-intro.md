---
title: Introduction to a Resource in Direct3D 11
description: This topic introduces Direct3D resources such as buffers and textures.
ms.assetid: 9e991ab0-9648-484a-9a2c-5391ee5abf20
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Introduction to a Resource in Direct3D 11

Resources are the building blocks of your scene. They contain most of the data that Direct3D uses to interpret and render your scene. Resources are areas in memory that can be accessed by the Direct3D pipeline. Resources contain the following types of data: geometry, textures, shader data. This topic introduces Direct3D resources such as buffers and textures.

You can create resources that are strongly typed or typeless; you can control whether resources have both read and write access; you can make resources accessible to only the CPU, GPU, or both. Up to 128 resources can be active for each pipeline stage.

Direct3D guarantees to return zero for any resource that is accessed out of bounds.

The lifecycle of a Direct3D resource is:

-   Create a resource using one of the create methods of the [**ID3D11Device**](/windows/win32/D3D11/nn-d3d11-id3d11device?branch=master) interface.
-   Bind a resource to the pipeline using a context and one of the set methods of the [**ID3D11DeviceContext**](/windows/win32/D3D11/nn-d3d11-id3d11devicecontext?branch=master) interface.
-   Deallocate a resource by calling the [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) method of the resource interface.

This section contains the following topics:

-   [Strong vs Weak Typing](#strong-vs-weak-typing)
-   [Resource Views](#resource-views)
-   [Raw Views of Buffers](#raw-views-of-buffers)
-   [Related topics](#related-topics)

## Strong vs Weak Typing

There are two ways to fully specify the layout (or memory footprint) of a resource:

-   Typed - fully specify the type when the resource is created.
-   Typeless - fully specify the type when the resource is bound to the pipeline.

Creating a fully-typed resource restricts the resource to the format it was created with. This enables the runtime to optimize access, especially if the resource is created with flags indicating that it cannot be mapped by the application. Resources created with a specific type cannot be reinterpreted using the view mechanism unless the resource was created with the D3D10\_DDI\_BIND\_PRESENT flag. If D3D10\_DDI\_BIND\_PRESENT is set render-target or shader resource views can be created on these resources using any of the fully typed members of the appropriate family, even if the original resource was created as fully typed.

In a type less resource, the data type is unknown when the resource is first created. The application must choose from the available type less formats (see [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)). You must specify the size of the memory to allocate and whether the runtime will need to generate the subtextures in a mipmap. However, the exact data format (whether the memory will be interpreted as integers, floating point values, unsigned integers etc.) is not determined until the resource is bound to the pipeline with a [resource view](#resource-views). As the texture format remains flexible until the texture is bound to the pipeline, the resource is referred to as weakly typed storage. Weakly typed storage has the advantage that it can be reused or reinterpreted in another format as long as the number of components and the bit count of each component are the same in both formats.

A single resource can be bound to multiple pipeline stages as long as each has a unique view, which fully qualifies the formats at each location. For example, a resource created with the format DXGI\_FORMAT\_R32G32B32A32\_TYPELESS could be used as a DXGI\_FORMAT\_R32G32B32A32\_FLOAT and a DXGI\_FORMAT\_R32G32B32A32\_UINT at different locations in the pipeline simultaneously.

## Resource Views

Resources can be stored in general purpose memory formats so that they can be shared by multiple pipeline stages. A pipeline stage interprets resource data using a view. A resource view is conceptually similar to casting the resource data so that it can be used in a particular context.

A view can be used with a typeless resource. That is, you can create a resource at compile time and declare the data type when the resource is bound to the pipeline. A view created for a typeless resource always has the same number of bits per component; the way the data is interpreted is dependent on the format specified. The format specified must be from the same family as the typeless format used when creating the resource. For example, a resource created with the R8G8B8A8\_TYPELESS format cannot be viewed as a R32\_FLOAT resource even though both formats may be the same size in memory.

A view also exposes other capabilities such as the ability to read back depth/stencil surfaces in a shader, generating a dynamic cubemap in a single pass, and rendering simultaneously to multiple slices of a volume.



| Resource Interface                                             | Description                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**ID3D11DepthStencilView**](/windows/win32/D3D11/nn-d3d11-id3d11depthstencilview?branch=master)       | Access a texture resource during depth-stencil testing.                                       |
| [**ID3D11RenderTargetView**](/windows/win32/D3D11/nn-d3d11-id3d11rendertargetview?branch=master)       | Access a texture resource that is used as a render-target.                                    |
| [**ID3D11ShaderResourceView**](/windows/win32/D3D11/nn-d3d11-id3d11shaderresourceview?branch=master)   | Access a shader resource such as a constant buffer, a texture buffer, a texture or a sampler. |
| [**ID3D11UnorderedAccessView**](/windows/win32/D3D11/nn-d3d11-id3d11unorderedaccessview?branch=master) | Access an unordered resource using a pixel shader or a compute shader.                        |



 

## Raw Views of Buffers

You can think of a raw buffer, which can also be called a [byte address buffer](direct3d-11-advanced-stages-cs-resources.md#byte-address-buffer), as a bag of bits to which you want raw access, that is, a buffer that you can conveniently access through chunks of one to four 32-bit typeless address values. You indicate that you want raw access to a buffer (or, a raw view of a buffer) when you call one of the following methods to create a view to the buffer:

-   To create a shader resource view (SRV) to the buffer, call [**ID3D11Device::CreateShaderResourceView**](/windows/win32/D3D11/nf-d3d11-id3d11device-createshaderresourceview?branch=master) with the flag [**D3D11\_BUFFEREX\_SRV\_FLAG\_RAW**](d3d11-bufferex-srv-flag.md#d3d11-bufferex-srv-flag-raw). You specify this flag in the **Flags** member of the [**D3D11\_BUFFEREX\_SRV**](/windows/win32/D3D11/ns-d3d11-d3d11_bufferex_srv?branch=master) structure. You set **D3D11\_BUFFEREX\_SRV** in the **BufferEx** member of the [**D3D11\_SHADER\_RESOURCE\_VIEW\_DESC**](/windows/win32/d3d11/ns-d3d11-d3d11_shader_resource_view_desc?branch=master) structure to which the *pDesc* parameter of **ID3D11Device::CreateShaderResourceView** points. You also set the [**D3D11\_SRV\_DIMENSION\_BUFFEREX**](d3d11-srv-dimension.md#d3d11-srv-dimension-bufferex) value in the **ViewDimension** member of **D3D11\_SHADER\_RESOURCE\_VIEW\_DESC** to indicate that the SRV is a raw view.
-   To create an unordered access view (UAV) to the buffer, call [**ID3D11Device::CreateUnorderedAccessView**](/windows/win32/D3D11/nf-d3d11-id3d11device-createunorderedaccessview?branch=master) with the flag [**D3D11\_BUFFER\_UAV\_FLAG\_RAW**](d3d11-buffer-uav-flag.md#d3d11-buffer-uav-flag-raw). You specify this flag in the **Flags** member of the [**D3D11\_BUFFER\_UAV**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_uav?branch=master) structure. You set **D3D11\_BUFFER\_UAV** in the **Buffer** member of the [**D3D11\_UNORDERED\_ACCESS\_VIEW\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_unordered_access_view_desc?branch=master) structure to which the *pDesc* parameter of **ID3D11Device::CreateUnorderedAccessView** points. You also set the [**D3D11\_UAV\_DIMENSION\_BUFFER**](d3d11-uav-dimension.md#d3d11-uav-dimension-buffer) value in the **ViewDimension** member of **D3D11\_UNORDERED\_ACCESS\_VIEW\_DESC** to indicate that the UAV is a raw view.

You can use the HLSL [**ByteAddressBuffer**](https://msdn.microsoft.com/library/windows/desktop/ff471453) and [**RWByteAddressBuffer**](https://msdn.microsoft.com/library/windows/desktop/ff471475) object types when you work with raw buffers.

To create a raw view to a buffer, you must first call [**ID3D11Device::CreateBuffer**](/windows/win32/D3D11/nf-d3d11-id3d11device-createbuffer?branch=master) with the [**D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS**](d3d11-resource-misc-flag.md#d3d11-resource-misc-buffer-allow-raw-views) flag to create the underlying buffer resource. You specify this flag in the **MiscFlags** member of the [**D3D11\_BUFFER\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_buffer_desc?branch=master) structure to which the *pDesc* parameter of **ID3D11Device::CreateBuffer** points. You can't combine the **D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS** flag with [**D3D11\_RESOURCE\_MISC\_BUFFER\_STRUCTURED**](d3d11-resource-misc-flag.md#d3d11-resource-misc-buffer-structured). Also, if you specify [**D3D11\_BIND\_CONSTANT\_BUFFER**](d3d11-bind-flag.md#d3d11-bind-constant-buffer) in **BindFlags** of **D3D11\_BUFFER\_DESC**, you can't also specify **D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS** in **MiscFlags**. This is not a limitation of just raw views because constant buffers already have a constraint that they can't be combined with any other view.

Other than the preceding invalid cases, when you create a buffer with [**D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS**](d3d11-resource-misc-flag.md#d3d11-resource-misc-buffer-allow-raw-views), you aren't limited in functionality versus not setting **D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS**. That is, you can use such a buffer for non-raw access in any number of ways that are possible with Direct3D. If you specify the **D3D11\_RESOURCE\_MISC\_BUFFER\_ALLOW\_RAW\_VIEWS** flag, you only increase the available functionality.

## Related topics

<dl> <dt>

[Resources](overviews-direct3d-11-resources.md)
</dt> <dt>

[New Resource Types](direct3d-11-advanced-stages-cs-resources.md)
</dt> </dl>

 

 




