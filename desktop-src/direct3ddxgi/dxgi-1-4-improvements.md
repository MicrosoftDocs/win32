---
Description: The following functionality has been added or changed in Microsoft DirectX Graphics Infrastructure (DXGI) 1.4, largely to support Direct3D 12.
ms.assetid: DEA901EA-B0F9-41D9-802C-ED1D6A7888E0
title: DXGI 1.4 Improvements
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DXGI 1.4 Improvements

The following functionality has been added or changed in Microsoft DirectX Graphics Infrastructure (DXGI) 1.4, largely to support Direct3D 12.

-   [Cheaper adapter enumeration](#cheaper-adapter-enumeration)
-   [Video memory budget tracking](#video-memory-budget-tracking)
-   [Direct3D 12 Swapchain Changes](#direct3d-12-swapchain-changes)
-   [Related topics](#related-topics)

## Cheaper adapter enumeration

For Direct3D 12, it’s no longer possible to backtrack from a device to the [**IDXGIAdapter**](/windows/desktop/api/DXGI/nn-dxgi-idxgiadapter) that was used to create it. It’s also no longer possible to provide D3D\_DRIVER\_TYPE\_WARP into [**D3D12CreateDevice**](https://msdn.microsoft.com/windows/desktop/F403D730-CBD4-4AE0-86F6-8CE122E82CB4). To make development easier, you can use [**IDXGIFactory4**](/windows/desktop/api/DXGI1_4/nn-dxgi1_4-idxgifactory4) to deal with both of these. [**IDXGIFactory4::EnumAdapterByLuid**](/windows/desktop/api/DXGI1_4/nf-dxgi1_4-idxgifactory4-enumadapterbyluid) (designed to be paired with [**ID3D12Device::GetAdapterLuid**](https://msdn.microsoft.com/windows/desktop/006E72E0-AE09-4834-9ACB-D48698050BF2)) enables an app to retrieve information about the adapter where a Direct3D 12 device was created. [**IDXGIFactory4::EnumWarpAdapter**](/windows/desktop/api/DXGI1_4/nf-dxgi1_4-idxgifactory4-enumwarpadapter) provides an adapter which can be provided to **D3D12CreateDevice** to use the WARP renderer.

## Video memory budget tracking

Application developers are encouraged to use a video memory reservation system, to inform the OS of the amount of physical video memory the app cannot go without.

The amount of physical memory available for a process is known as the "video memory budget". The budget can fluctuate noticeably as background processes wake-up and sleep; and fluctuate dramatically when the user switches away to another application. The application can be notified when the budget changes and poll both the current budget and the currently consumed amount of memory. If an application doesn’t stay within its budget, the process will be intermittently frozen to allow other applications to run and/or the creation APIs will return failure. The [**IDXGIAdapter3**](/windows/desktop/api/dxgi1_4/nn-dxgi1_4-idxgiadapter3) interface provides the methods pertaining to this functionality, in particular [**QueryVideoMemoryInfo**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-queryvideomemoryinfo) and [**RegisterVideoMemoryBudgetChangeNotificationEvent**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registervideomemorybudgetchangenotificationevent).

For more information, refer to the Direct3D 12 topic on [Residency](https://msdn.microsoft.com/windows/desktop/956F80D7-EEC8-4D88-B251-EE325614F31E).

## Direct3D 12 Swapchain Changes

Some of the existing Direct3D 11 swapchain functionality was deprecated to achieve the overhead reductions in Direct3D 12. While other changes were made to either align to Direct3D 12 concepts or provide better support for Direct3D 12 features.

**Invariant Backbuffer Identity**

In Direct3D 11, applications could call [**GetBuffer**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-getbuffer)( 0, … ) only once. Every call to [**Present**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-present) implicitly changed the resource identity of the returned interface. Direct3D 12 no longer supports that implicit resource identity change, due to the CPU overhead required and the flexible resource descriptor design. As a result, the application must manually call **GetBuffer** for every each buffer created with the swapchain. The application must manually render to the next buffer in the sequence after calling **Present**. Applications are encouraged to create a cache of descriptors for each buffer, instead of re-creating many objects each **Present**.

**Multi-Adapter Support**

When a swapchain is created on a multi-GPU adapter, the backbuffers are all created on node 1 and only a single command queue is supported. [**ResizeBuffers1**](/windows/desktop/api/DXGI1_4/nf-dxgi1_4-idxgiswapchain3-resizebuffers1) enables applications to create backbuffers on different nodes, allowing a different command queue to be used with each. These capabilities enable Alternate Frame Rendering (AFR) techniques to be used with the swapchain. Refer to [Direct3D 12 Multi-Adapters](https://www.bing.com/search?q=Direct3D 12 Multi-Adapters).

**Miscellaneous**

-   A command queue object must be passed to [**CreateSwapChain**](/windows/desktop/api/DXGI/nf-dxgi-idxgifactory-createswapchain) methods instead of the Direct3D 12 device object.
-   Only the following two flip model swap effects are supported: <dl> DXGI\_SWAP\_EFFECT\_FLIP\_DISCARD should be preferred when applications fully render over the backbuffer before presenting it or are interested in supporting multi-adapter scenarios easily.  
    DXGI\_SWAP\_EFFECT\_FLIP\_SEQUENTIAL should be used by applications that rely on partial presentation optimizations or regularly read from previously presented backbuffers.  
    </dl>
-   [**SetFullscreenState**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-setfullscreenstate) no longer exclusively owns the display, so user-initiated operating system elements can seamlessly appear in front of application output. Volume settings is an example of this.

## Related topics

<dl> <dt>

[Direct3D 12 Hardware Feature Levels](https://msdn.microsoft.com/windows/desktop/B8304E29-A532-464E-8FAF-075228D8FB73)
</dt> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 



