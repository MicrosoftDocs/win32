---
title: Direct3D 11 on 12
description: D3D11On12 is a mechanism by which developers can use D3D11 interfaces and objects to drive the D3D12 API.
ms.assetid: 8412D8BB-B6DD-471E-AAB2-A81121FB0FFA
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 on 12

D3D11On12 is a mechanism by which developers can use D3D11 interfaces and objects to drive the D3D12 API. D3D11on12 enables components written using D3D11 (for example, D2D text and UI) to work together with components written targeting the D3D12 API. D3D11on12 also enables incremental porting of an application from D3D11 to D3D12, by enabling portions of the app to continue targeting D3D11 for simplicity while others target D3D12 for performance, while always having complete and correct rendering. D3D11On12 makes it simpler than using interop techniques to share resources and synchronize work between the two APIs.

-   [Initializing D3D11On12](#initializing-d3d11on12)
-   [Example Usage](#example-usage)
-   [Background](#background)
-   [Cleaning up](#cleaning-up)
-   [Limitations](#limitations)
-   [APIs](#apis)
-   [Related topics](#related-topics)

## Initializing D3D11On12

To begin using D3D11On12, the first step is to create a D3D12 device and command queue. These objects are provided as input to the initialization method [**D3D11On12CreateDevice**](/windows/desktop/api/d3d11on12/nf-d3d11on12-d3d11on12createdevice). You can think of this method as creating a D3D11 device with the imaginary driver type D3D\_DRIVER\_TYPE\_11ON12, where the D3D11 driver is responsible for creating objects and submitting command lists to the D3D12 API.

After you have a D3D11 device and immediate context, you can `QueryInterface` off of the device for the [**ID3D11On12Device**](/windows/desktop/api/d3d11on12/nn-d3d11on12-id3d11on12device) interface. This is the primary interface that is used for interop between D3D11 and D3D12. In order to have both the D3D11 device context and the D3D12 command lists operate on the same resources, it is necessary to create “wrapped resources” using the [**CreateWrappedResource**](/windows/desktop/api/d3d11on12/nf-d3d11on12-id3d11on12device-createwrappedresource) API. This method “promotes” a D3D12 resource to be understandable in D3D11. A wrapped resource starts out in the “acquired” state, a property which is manipulated by the [**AcquireWrappedResources**](/windows/desktop/api/d3d11on12/nf-d3d11on12-id3d11on12device-acquirewrappedresources) and [**ReleaseWrappedResources**](/windows/desktop/api/d3d11on12/nf-d3d11on12-id3d11on12device-releasewrappedresources) methods.

## Example Usage

Typical usage of D3D11On12 would be to use D2D to render text or images on top of a D3D12 back buffer. See the D3D11On12 sample for example code. Here is a rough outline of the steps to take to do so:

-   Create a D3D12 device ([**D3D12CreateDevice**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createdevice)) and a D3D12 swap chain ([**CreateSwapChain**](/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-createswapchain) with an [**ID3D12CommandQueue**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandqueue) as an input).
-   Create a D3D11On12 device using the D3D12 device and the same command queue as input.
-   Retrieve the swap chain back buffers, and create D3D11 wrapped resources for each of them. The input state used should be the last way that D3D12 used it (e.g. RENDER\_TARGET) and the output state should be the way that D3D12 will use it after D3D11 has finished (e.g. PRESENT).
-   Initialize D2D, and provide the D3D11 wrapped resources to D2D to prepare for rendering.

Then, on each frame, do the following:

-   Render into the current swap chain back buffer using a D3D12 command list, and execute it.
-   Acquire the current back buffer’s wrapped resource ([**AcquireWrappedResources**](/windows/desktop/api/d3d11on12/nf-d3d11on12-id3d11on12device-acquirewrappedresources)).
-   Issue D2D rendering commands.
-   Release the wrapped resource ([**ReleaseWrappedResources**](/windows/desktop/api/d3d11on12/nf-d3d11on12-id3d11on12device-releasewrappedresources)).
-   Flush the D3D11 immediate context.
-   Present ([**IDXGISwapChain1::Present1**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-present1)).

## Background

D3D11On12 works systematically. Each D3D11 API call goes through the typical runtime validation and makes its way to the driver. At the driver layer, the special 11on12 driver records state and issues render operations to D3D12 command lists. These command lists are submitted as necessary (for example, a query `GetData` or resource `Map` might require commands to be flushed) or as requested by Flush. Creating a D3D11 object typically results in the corresponding D3D12 object being created. Some fixed function render operations in D3D11 such as `GenerateMips` or `DrawAuto` are not supported in D3D12, and so D3D11On12 emulates them using shaders and additional resources.

For interop, it’s important to understand how D3D11On12 interacts with the D3D12 objects that the app has created and provided. In order to ensure that work happens in the correct order, the D3D11 immediate context must be flushed before additional D3D12 work can be submitted to that queue. It’s also important to ensure that the queue given to D3D11On12 must be drainable at all times. That means that any waits on the queue must eventually be satisfied, even if the D3D11 render thread blocks indefinitely. Be wary not to take a dependency on when D3D11On12 inserts flushes or waits, as this may change with future releases. Additionally, D3D11On12 tracks and manipulates resource states on its own. The only way to ensure coherency of state transitions is to make use of the acquire/release APIs to manipulate the state tracking to match the app’s needs.

## Cleaning up

In order to release a D3D11On12 wrapped resource, two things need to happen in this order:

-   All references to the resource, including any views of the resource, need to be released.
-   Deferred destruction processing must take place. The simplest way to ensure this happens is to invoke the immediate context `Flush` API.

After both of those steps are completed, any references taken by the wrapped resource should be released, and the D3D12 resource becomes exclusively owned by the D3D12 component. Be aware that D3D12 still requires waiting for GPU completion before completely releasing a resource, so be sure to hold a reference on the resource before doing the two steps above, unless you’ve already confirmed that the GPU is no longer using the resource.

All other resources or objects created by D3D11On12 will be cleaned up at the appropriate time, when the GPU has finished using them, using D3D11’s deferred destruction mechanism. However if you attempt to release the D3D11On12 device itself while the GPU is still executing, the destruction may block until the GPU completes.

## Limitations

The D3D11On12 layer implements a very large subset of the D3D11 API, but there are some known gaps (in addition to bugs in the implementation that can cause incorrect rendering).

As of Windows 10, version 1809 (10.0; Build 17763), as long as D3D11On12 is running on a driver that supports Shader Model 6.0 or later, then it can run shaders that use interfaces. In earlier versions of Windows, the shader interfaces feature is not implemented in D3D11On12, and attempting to use the feature will cause errors and debug messages.

As of Windows 10, version 1803 (10.0; Build 17134), swap chains are supported on D3D11On12 devices. In earlier versions of Windows, they are not.

D3D11On12 has not been optimized for performance. There will likely be moderate CPU overhead compared to a standard D3D11 driver, minimal GPU overhead, and there is known to be significant memory overhead. Therefore it is not recommended to use D3D11On12 for complicated 3D scenes, and it is instead recommended for simple scenes, or 2D rendering.

## APIs

APIs that make up the 11on12 layer are described in [11on12 Reference](direct3d-11on12-reference.md).

## Related topics

<dl> <dt>

[D2D using D3D11on12 walk-through](d2d-using-d3d11on12.md)
</dt> <dt>

[Understanding Direct3D 12](directx-12-getting-started.md)
</dt> <dt>

[Working with Direct3D 11, Direct3D 10 and Direct2D](direct3d-12-interop.md)
</dt> </dl>

 

 
