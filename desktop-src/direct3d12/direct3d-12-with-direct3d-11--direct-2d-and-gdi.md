---
title: Direct3D 12 interop
description: D3D12 can be used to write componentized applications.
ms.assetid: 51F7E715-82B6-48D8-A06A-CBBEDF6968F5
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 interop

D3D12 can be used to write componentized applications.

-   [Interop overview](#interop-overview)
-   [Reasons for using interop](#reasons-for-using-interop)
    -   [Sharing a command list](#sharing-a-command-list)
    -   [Sharing a command queue](#sharing-a-command-queue)
    -   [Sharing sync primitives](#sharing-sync-primitives)
    -   [Sharing resources](#sharing-resources)
    -   [Choosing an interop model](#choosing-an-interop-model)
-   [Interop APIs](#interop-apis)
-   [Related topics](#related-topics)

## Interop overview

D3D12 can be very powerful, and allow applications to write graphics code with console-like efficiency, but not every application needs to reinvent the wheel and write the entirety of their rendering engine from scratch. In some cases, another component or library has already done it better, or in other cases, the performance of a portion of code is not as critical as its correctness and readability.

This section covers the following interop techniques:

-   D3D12 and D3D12, on the same device
-   D3D12 and D3D12, on different devices
-   D3D12 and any combination of D3D11, D3D10, or D2D, on the same device
-   D3D12 and any combination of D3D11, D3D10, or D2D, on different devices
-   D3D12 and GDI, or D3D12 and D3D11 and GDI

## Reasons for using interop

There are several reasons an application would want D3D12 interop with other APIs. Some examples:

-   Incremental porting: wanting to port an entire application from D3D10 or D3D11 to D3D12, while having it functional at intermediate stages of the porting process (to enable testing and debugging).
-   Black box code: wanting to leave a particular portion of an application as-is while porting the rest of the code. For example, there might be no need to port UI elements of a game.
-   Unchangeable components: needing to use components which are not owned by the application, which are not written to target D3D12.
-   A new component: not wanting to port the entire application, but wanting to use a new component which is written using D3D12.

There are four main techniques for interop in D3D12:

-   An app can choose to provide an open command list to a component, which records some additional rendering commands to an already-bound render target. This is equivalent to providing a prepared device context to another component in D3D11, and is great for things like adding UI/text to an already bound back buffer.
-   An app can choose to provide a command queue to a component, along with a desired destination resource. This is equivalent to using [**ClearState**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-clearstate) or [**DeviceContextState**](/windows/desktop/api/d3d11_1/nn-d3d11_1-id3ddevicecontextstate) APIs in D3D11 to provide a clean device context to another component. This is how components like D2D operate.
-   A component may opt for a model where it produces a command list, potentially in parallel, which the app is responsible for submission at a later time. At least one resource must be provided across component boundaries. This same technique is available in D3D11 using deferred contexts, though the performance in D3D12 is more desirable.
-   Each component has its own queue(s) and/or device(s), and the app and components need to share resources and synchronization information across component boundaries. This is similar to the legacy `ISurfaceQueue`, and the more modern [**IDXGIKeyedMutex**](/windows/desktop/api/dxgi/nn-dxgi-idxgikeyedmutex).

The differences between these scenarios is what exactly is shared between the component boundaries. The device is assumed to be shared, but since it is basically stateless, it is not really relevant. The key objects are the command list, the command queue, the sync objects, and the resources. Each of these have their own complications when sharing them.

### Sharing a command list

The simplest method of interop requires sharing only a command list with a portion of the engine. Once the rendering operations have completed, the command list ownership goes back to the caller. The ownership of the command list can be traced through the stack. Since command lists are single threaded, there’s no way for an app to do something unique or innovative using this technique.

### Sharing a command queue

Probably the most common technique for multiple components sharing a device in the same process.

When the command queue is the unit of sharing, there needs to be a call to the component to let it know that all outstanding command lists need to be submitted to the command queue immediately (and any internal command queues need to be synchronized). This is equivalent to the D3D11 [**Flush**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-flush) API, and is the only way that the application can submit its own command lists or sync primitives.

### Sharing sync primitives

The expected pattern for a component which operates on its own devices and/or command queues will be to accept an [**ID3D12Fence**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence) or shared handle, and UINT64 pair upon beginning its work, which it will wait on, and then a second ID3D12Fence or shared handle, and UINT64 pair which it will signal when all work is complete. This pattern matches the current implementation of both [**IDXGIKeyedMutex**](/windows/desktop/api/dxgi/nn-dxgi-idxgikeyedmutex) and the DWM/DXGI flip model synchronization design.

### Sharing resources

By far the most complicated part of writing a D3D12 app which leverages multiple components is how to deal with the resources which are shared across component boundaries. This is mostly due to the concept of resource states. While some aspects of the resource state design are meant to deal with intra-command-list synchronization, others do have impact between command lists, affecting resource layout and either valid sets of operations or performance characteristics of accessing the resource data.

There are two patterns of dealing with this complication, both of which involve essentially a contract between components.

-   The contract can be defined by the component developer and documented. This could be as simple as “the resource must be in the default state when work is started, and will be put back in the default state when work is done” or could have more complicated rules to allow things like sharing a depth buffer without forcing intermediate depth resolves.
-   The contract can be defined by the application at runtime, at the time when the resource is shared across component boundaries. It consists of the same two pieces of information – the state the resource will be in when the component starts using it, and the state the component should leave it in when it finishes.

### Choosing an interop model

For most D3D12 applications, sharing a command queue is probably the ideal model. It allows complete ownership of work creation and submission, without the additional memory overhead from having redundant queues, and without the perf impact of dealing with the GPU sync primitives.

Sharing sync primitives is required once the components need to deal with different queue properties, such as type or priority, or once the sharing needs to span process boundaries.

Sharing or producing command lists are not widely used externally by third party components, but might be widely used in components which are internal to a game engine.

## Interop APIs

The [Direct3D 11 on 12](./direct3d-11-on-12.md) topic walks you through the usage of much of the API surface related to the kinds of interoperation described in this topic.

Also see the [ID3D12Device::CreateSharedHandle](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createsharedhandle) method, which you can use to share surfaces between Windows graphics APIs.

## Related topics

* [Understanding Direct3D 12](directx-12-getting-started.md)
* [Working with Direct3D 11, Direct3D 10 and Direct2D](direct3d-12-interop.md)
* [Direct3D 11 on 12](./direct3d-11-on-12.md)
