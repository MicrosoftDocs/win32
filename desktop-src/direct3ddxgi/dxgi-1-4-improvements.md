---
Description: 'The following functionality has been added or changed in Microsoft DirectX Graphics Infrastructure (DXGI) 1.4, largely to support Direct3D 12.'
ms.assetid: 'DEA901EA-B0F9-41D9-802C-ED1D6A7888E0'
title: 'DXGI 1.4 Improvements'
---

# DXGI 1.4 Improvements

The following functionality has been added or changed in Microsoft DirectX Graphics Infrastructure (DXGI) 1.4, largely to support Direct3D 12.

-   [Cheaper adapter enumeration](#cheaper-adapter-enumeration)
-   [Video memory budget tracking](#video-memory-budget-tracking)
-   [Direct3D 12 Swapchain Changes](#direct3d-12-swapchain-changes)
-   [Related topics](#related-topics)

## Cheaper adapter enumeration

For Direct3D 12, it’s no longer possible to backtrack from a device to the [**IDXGIAdapter**](idxgiadapter.md) that was used to create it. It’s also no longer possible to provide D3D\_DRIVER\_TYPE\_WARP into [**D3D12CreateDevice**](direct3d12.d3d12createdevice). To make development easier, you can use [**IDXGIFactory4**](idxgifactory4.md) to deal with both of these. [**IDXGIFactory4::EnumAdapterByLuid**](idxgifactory4-enumadapterbyluid.md) (designed to be paired with [**ID3D12Device::GetAdapterLuid**](direct3d12.id3d12device_getadapterluid)) enables an app to retrieve information about the adapter where a Direct3D 12 device was created. [**IDXGIFactory4::EnumWarpAdapter**](idxgifactory4-enumwarpadapter.md) provides an adapter which can be provided to **D3D12CreateDevice** to use the WARP renderer.

## Video memory budget tracking

Application developers are encouraged to use a video memory reservation system, to inform the OS of the amount of physical video memory the app cannot go without.

The amount of physical memory available for a process is known as the "video memory budget". The budget can fluctuate noticeably as background processes wake-up and sleep; and fluctuate dramatically when the user switches away to another application. The application can be notified when the budget changes and poll both the current budget and the currently consumed amount of memory. If an application doesn’t stay within its budget, the process will be intermittently frozen to allow other applications to run and/or the creation APIs will return failure. The [**IDXGIAdapter3**](idxgiadapter3.md) interface provides the methods pertaining to this functionality, in particular [**QueryVideoMemoryInfo**](idxgiadapter3-queryvideomemoryinfo.md) and [**RegisterVideoMemoryBudgetChangeNotificationEvent**](idxgiadapter3-registervideomemorybudgetchangenotificationevent.md).

For more information, refer to the Direct3D 12 topic on [Residency](direct3d12.residency).

## Direct3D 12 Swapchain Changes

Some of the existing Direct3D 11 swapchain functionality was deprecated to achieve the overhead reductions in Direct3D 12. While other changes were made to either align to Direct3D 12 concepts or provide better support for Direct3D 12 features.

**Invariant Backbuffer Identity**

In Direct3D 11, applications could call [**GetBuffer**](idxgiswapchain-getbuffer.md)( 0, … ) only once. Every call to [**Present**](idxgiswapchain-present.md) implicitly changed the resource identity of the returned interface. Direct3D 12 no longer supports that implicit resource identity change, due to the CPU overhead required and the flexible resource descriptor design. As a result, the application must manually call **GetBuffer** for every each buffer created with the swapchain. The application must manually render to the next buffer in the sequence after calling **Present**. Applications are encouraged to create a cache of descriptors for each buffer, instead of re-creating many objects each **Present**.

**Multi-Adapter Support**

When a swapchain is created on a multi-GPU adapter, the backbuffers are all created on node 1 and only a single command queue is supported. [**ResizeBuffers1**](idxgiswapchain3-resizebuffers1.md) enables applications to create backbuffers on different nodes, allowing a different command queue to be used with each. These capabilities enable Alternate Frame Rendering (AFR) techniques to be used with the swapchain. Refer to [Direct3D 12 Multi-Adapters](direct3d12.mulit-engine).

**Miscellaneous**

-   A command queue object must be passed to [**CreateSwapChain**](idxgifactory-createswapchain.md) methods instead of the Direct3D 12 device object.
-   Only the following two flip model swap effects are supported: <dl> DXGI\_SWAP\_EFFECT\_FLIP\_DISCARD should be preferred when applications fully render over the backbuffer before presenting it or are interested in supporting multi-adapter scenarios easily.  
    DXGI\_SWAP\_EFFECT\_FLIP\_SEQUENTIAL should be used by applications that rely on partial presentation optimizations or regularly read from previously presented backbuffers.  
    </dl>
-   [**SetFullscreenState**](idxgiswapchain-setfullscreenstate.md) no longer exclusively owns the display, so user-initiated operating system elements can seamlessly appear in front of application output. Volume settings is an example of this.

## Related topics

<dl> <dt>

[Direct3D 12 Hardware Feature Levels](direct3d12.hardware_feature_levels)
</dt> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 



