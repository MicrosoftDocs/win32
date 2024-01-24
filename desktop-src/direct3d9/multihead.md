---
description: Multihead cards are those that have a common frame buffer and accelerator, independent digital-to-analog converters (DACs), and monitor outputs.
ms.assetid: f741cdb4-2eb6-42e9-81ea-a8c677e07582
title: Multihead (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multihead (Direct3D 9)

Multihead cards are those that have a common frame buffer and accelerator, independent digital-to-analog converters (DACs), and monitor outputs. Such devices can offer much more usable multiple monitor support than a similar number of heterogeneous display adapters.

Multihead cards are exposed in the API as a single API-level device that can drive several full-screen swap chains. Consequently, all resources are shared with all the heads, and each head has exactly the same capabilities. Each head can be set to independent display modes. You can use separate calls to [**IDirect3DSwapChain9::Present**](/windows/desktop/api) to refresh each head. You can also use one call to [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present) to refresh each head sequentially.

> [!Note]  
> The refresh of each head does not occur simultaneously with a single call to [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present). Present statistics in Direct3D 9Ex can use the [**D3DPRESENTSTATS**](d3dpresentstats.md) structure to keep the refreshes to each head close to each other to limit tearing effects across multiple heads of adapters. For information about synchronizing frames of Direct3D 9Ex flip model applications, see [Direct3D 9Ex Improvements](../direct3darticles/direct3d-9ex-improvements.md).

 

Each swap chain for a multihead device must be full screen. When a device has entered multihead mode, it must remain full screen. The transition back to windowed mode requires the destruction of the device (except for the normal ALT+TAB-to-minimize operation).

The old method of dividing video memory between the heads and treating each head as a fully independent accelerator will still be a common usage scenario. This proposal does not replace that mechanism unless the application has been specifically coded to function in the Direct3D 9 multihead mode.

Drivers are given adequate knowledge to switch between the two modes of operation.

One head will be called the master head, and all other heads on the same card be called subordinate heads. If more than one multihead adapter is present in a system, the master and its subordinates from one multihead adapter are called a group. Groups are denoted by the adapter ordinal of their master head.

The [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure has been updated to expose the following new hardware caps.


```
UINT NumberOfAdaptersInGroup; 
UINT MasterAdapterOrdinal; 
UINT AdapterOrdinalInGroup;
```



-   NumberOfAdaptersInGroup is 1 for conventional adapters, and greater than 1 for the master adapter of a multihead card. The value will be 0 for a subordinate adapter of a multihead card. Each card can have at most one master, but might have many subordinates.
-   MasterAdapterOrdinal indicates which device is the master for this subordinate.
-   AdapterOrdinalInGroup indicates the order in which heads are referenced by the API. The master adapter always has AdapterOrdinalInGroup 0. These values do not correspond to the adapter ordinals passed to the IDirect3D9 methods, but apply only to heads within a group.

This definition allows multihead cards to continue to present multiple adapters as if they were independent cards, just as they did in DirectX 8.

To create a multihead device, specify the behavior flag D3DCREATE\_ADAPTERGROUP\_DEVICE in [**IDirect3D9::CreateDevice**](/windows/desktop/api). The presentation parameters (an array of [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md)) should contain NumberOfAdaptersInGroup elements. The runtime will assign each element to each head in AdapterOrdinalInGroup numerical order. When D3DCREATE\_ADAPTERGROUP\_DEVICE is set, each presentation parameter must have:

-   The Windowed member set to **FALSE** (in other words, be full screen).
-   The same value for the EnableAutoDepthStencil member of [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md).

In addition, if EnableAutoDepthStencil is **TRUE**, then each of the following fields must have the same value for each [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md):

-   AutoDepthStencilFormat
-   BackBufferWidth
-   BackBufferHeight
-   BackBufferFormat

If DAC is set, additional calls to [**IDirect3DDevice9::CreateAdditionalSwapChain**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createadditionalswapchain) are illegal.

If the device was created with the DAC, [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) will expect an array of [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md).

Each [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) structure passed to [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) must be full screen. To switch back to windowed mode, the application must destroy the device and re-create a non-multihead device in windowed mode.

Here is a basic usage scenario:


```
1. Create multihead device 
2. For each swap chain of device:
   3. Call GetBackBuffer for the i-th swapchain
   4. Call SetRenderTarget 
   5. Call DrawPrimitive 
   6. Optionally call swapchain::Present (or wait until 
all swap chains are drawn and present outside of loop)
7. End the for loop
8. Optionally present all swap chains with device::Present
```



For more information, see [**IDirect3D9::CreateDevice**](/windows/desktop/api) and [**IDirect3DDevice9::GetNumberOfSwapChains**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getnumberofswapchains).

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
