---
title: Object Creation with Multithreading
description: Use the ID3D11Device interface to create resources and objects, use the ID3D11DeviceContext for rendering.
ms.assetid: e1765192-865c-4a62-9be7-6e95280ee8ad
ms.topic: article
ms.date: 05/31/2018
---

# Object Creation with Multithreading

Use the [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) interface to create resources and objects, use the [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) for [rendering](overviews-direct3d-11-render-multi-thread-render.md).

Here are some examples of how to create resources:

-   [How to: Create a Vertex Buffer](overviews-direct3d-11-resources-buffers-vertex-how-to.md)
-   [How to: Create an Index Buffer](overviews-direct3d-11-resources-buffers-index-how-to.md)
-   [How to: Create a Constant Buffer](overviews-direct3d-11-resources-buffers-constant-how-to.md)
-   [How to: Initialize a Texture From a File](overviews-direct3d-11-resources-textures-how-to.md)

## Multithreading Considerations

The amount of concurrency of resource creation and rendering that your application can achieve depends on the level of multithreading support that the driver implements. If the driver supports concurrent creates, then the application should have much less concurrency concerns. However, if the driver does not support concurrent object creation, the amount of concurrency is extremely limited. To understand the amount of support available in a driver, query the driver for the value of the **DriverConcurrentCreates** member of the [**D3D11\_FEATURE\_DATA\_THREADING**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_threading) structure. For more information about checking for driver support of multithreading, see [How To: Check for Driver Support](overviews-direct3d-11-render-multi-thread-support.md).

Concurrent operations do not necessarily lead to better performance. For example, creating and loading a texture is typically limited by memory bandwidth. Attempting to create and load multiple textures might be no faster than doing one texture at a time, even if this leaves multiple CPU cores idle. However, creating multiple shaders using multiple threads can increase performance as this operation is less dependent on system resources such as memory bandwidth.

When the driver and graphics hardware support multithreading, you can typically initialize newly created resources more efficiently by passing a pointer to initial data in the *pInitialData* parameter (for example, in a call to the [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d) method).

## Related topics

<dl> <dt>

[MultiThreading](overviews-direct3d-11-render-multi-thread.md)
</dt> </dl>

 

 




