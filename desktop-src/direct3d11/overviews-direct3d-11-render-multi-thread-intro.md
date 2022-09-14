---
title: Introduction to Multithreading in Direct3D 11
description: Multithreading is designed to improve performance by performing work using one or more threads at the same time.
ms.assetid: b4bef1e4-8d34-455c-8aed-01af974c66c8
ms.topic: article
ms.date: 05/31/2018
---

# Introduction to Multithreading in Direct3D 11

Multithreading is designed to improve performance by performing work using one or more threads at the same time.

In the past, this has often been done by generating a single main thread for rendering and one or more threads for doing preparation work such as object creation, loading, processing, and so on. However, with the built in synchronization in Direct3D 11, the goal behind multithreading is to utilize every CPU and GPU cycle without making a processor wait for another processor (particularly not making the GPU wait because it directly impacts frame rate). By doing so, you can generate the most amount of work while maintaining the best frame rate. The concept of a single frame for rendering is no longer as necessary since the API implements synchronization.

Multithreading requires some form of synchronization. For example, if multiple threads that run in an application must access a single device context ([**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)), that application must use some synchronization mechanism, such as critical sections, to synchronize access to that device context. This is because processing of the render commands (generally done on the GPU) and generating the render commands (generally done on the CPU through object creation, data loading, state changing, data processing) often use the same resources (textures, shaders, pipeline state, and so on). Organizing the work across multiple threads requires synchronization to prevent one thread from modifying or reading data that is being modified by another thread.

While the use of a device context ([**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)) is not thread-safe, the use of a Direct3D 11 device ([**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device)) is thread-safe. Because each **ID3D11DeviceContext** is single threaded, only one thread can call a **ID3D11DeviceContext** at a time. If multiple threads must access a single **ID3D11DeviceContext**, they must use some synchronization mechanism, such as critical sections, to synchronize access to that **ID3D11DeviceContext**. However, multiple threads are not required to use critical sections or synchronization primitives to access a single **ID3D11Device**. Therefore, if an application uses **ID3D11Device** to create resource objects, that application is not required to use synchronization to create multiple resource objects at the same time.

Multithreading support divides the API into two distinct functional areas:

-   [Object Creation with Multithreading](overviews-direct3d-11-render-multi-thread-create.md)
-   [Immediate and Deferred Rendering](overviews-direct3d-11-render-multi-thread-render.md)

Multithreading performance depends on the driver support. [How To: Check for Driver Support](overviews-direct3d-11-render-multi-thread-support.md) provides more information about querying the driver and what the results mean.

Direct3D 11 has been designed from the ground up to support multithreading. Direct3D 10 implements limited support for multithreading using the [thread-safe layer](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-api-features-layers). This page lists the behavior differences between the two versions of DirectX: [Threading Differences between Direct3D Versions](overviews-direct3d-11-render-multi-thread-differences.md).

## Multithreading and DXGI

Only one thread at a time should use the immediate context. However, your application should also use that same thread for Microsoft DirectX Graphics Infrastructure (DXGI) operations, especially when the application makes calls to the [**IDXGISwapChain::Present**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-present) method.

> [!Note]  
> It is invalid to use an immediate context concurrently with most of the DXGI interface functions. For the March 2009 and later DirectX SDKs, the only DXGI functions that are safe are [**AddRef**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref), [**Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release), and [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)).

 

For more info about using DXGI with multiple threads, see [Multithread Considerations](/windows/desktop/direct3ddxgi/d3d10-graphics-programming-guide-dxgi).

## Related topics

<dl> <dt>

[Multithreading](overviews-direct3d-11-render-multi-thread.md)
</dt> </dl>

 

 