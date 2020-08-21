---
title: Swap Chains
description: Swap chains control the back buffer rotation, forming the basis of graphics animation.
ms.assetid: AABF5FDE-DB49-4B29-BC0E-032E0C7DF9EB
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Swap Chains

Swap chains control the back buffer rotation, forming the basis of graphics animation.

-   [Overview](#overview)
    -   [Buffer lifetime](#buffer-lifetime)
    -   [Swap effects](#swap-effects)
    -   [Transitioning between windowed and full-screen modes](#transitioning-between-windowed-and-full-screen-modes)
    -   [Example](#example)
    -   [Creating swap chains](#creating-swap-chains)
-   [Related topics](#related-topics)

## Overview

The programming model for swap chains in D3D12 is not identical to that in earlier versions of D3D. The programming convenience, for example, of supporting automatic resource rotation that was present in D3D10 and D3D11 is not now supported. Automatic resource rotation enabled apps to render the same API object while the actual surface being rendered changes each frame. The behavior of swap chains is changed with D3D12 to enable other features of D3D12 to have low CPU overhead.

### Buffer lifetime

Apps are allowed to store pre-created descriptors which reference back buffers This is enabled by ensuring that the set of buffers owned by a swap chain never changes for the lifetime of the swap chain. The set of buffers returned by [**IDXGISwapChain::GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) does not change until certain APIs are called:

-   [**IDXGISwapChain::ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget)
-   [**IDXGISwapChain::ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers)

The order of buffers returned by [**GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) never changes.

[**IDXGISwapChain3::GetCurrentBackBufferIndex**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiswapchain3-getcurrentbackbufferindex) returns the index of the current back buffer to the app.

### Swap effects

The only supported swap effect is FLIP\_SEQUENTIAL, which requires the buffer count to be greater than one.

### Transitioning between windowed and full-screen modes

D3D12 maintains the restriction that applications must call [**ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) after transitioning between windowed and full-screen modes (D3D11 flip-model swap chains have the same restrictions).

The [**IDXGISwapChain::SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate) transitions do not change the set of app-visible buffers in the swap chain. Only the [**ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) and [**ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget) calls create or destroy app-visible buffers.

When [**IDXGISwapChain1::Present1**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-present1) is called, the back buffer to be presented must be in the [**D3D12\_RESOURCE\_STATE\_PRESENT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_states) state. Present will fail with DXGI\_ERROR\_INVALID\_CALL if this is not the case.

Full-screen swap chains continue to have the restriction that [**SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate)(FALSE, NULL) must be called before the final release of the swap chain. **SetFullscreenState**(FALSE) succeeds on swap chains running on D3D12 devices.

Present operations occur on the default 3D queue associated with the device., and apps are free to concurrently present multiple swap chains, and record and execute command lists.

### Example

The following example code would be present in the main rendering loop:

``` syntax
        CComPtr<IDXGISwapChain3> spSwapChain3;
        m_spSwapChain->QueryInterface(&spSwapChain3);
        UINT backBufferIndex = spSwapChain3->GetCurrentBackBufferIndex();

        CComPtr<ID3D12Resource>         spBackBuffer;
        m_spSwapChain->GetBuffer(backBufferIndex, IID_PPV_ARGS(&spBackBuffer));

        // record and execute a command list referencing spBackBuffer
        m_spSwapChain->Present1(0, 0);
```

### Creating swap chains

When using the [**CreateSwapChainForHwnd**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforhwnd), [**CreateSwapChainForCoreWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcorewindow), or [**CreateSwapChainForComposition**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcomposition) calls, note that the *pDevice* parameter actually requires a pointer to a direct command queue in Direct3D 12, and not a device.

## Related topics

<dl> <dt>

[**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags)
</dt> <dt>

[DirectX advanced learning video tutorials : Unthrottled Framerate](https://www.youtube.com/watch?v=wn02zCXa9IU)
</dt> <dt>

[Rendering](rendering.md)
</dt> </dl>

 

 