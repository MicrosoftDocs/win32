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

## Overview

The programming model for swap chains in Direct3D 12 is not identical to that in earlier versions of D3D. The programming convenience, for example, of supporting automatic resource rotation that was present in D3D10 and D3D11 is not now supported. Automatic resource rotation enabled apps to render the same API object while the actual surface being rendered changes each frame. The behavior of swap chains is changed with Direct3D 12 to enable other features of Direct3D 12 to have low CPU overhead. Automatic color key and multisampling are not supported, although notably stretching and rotation still are.

### Buffer lifetime

Apps are allowed to store pre-created descriptors which reference back buffers This is enabled by ensuring that the set of buffers owned by a swap chain never changes for the lifetime of the swap chain. The set of buffers returned by [**IDXGISwapChain::GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) doesn't change until certain APIs are called:

-   [**IDXGISwapChain::ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget)
-   [**IDXGISwapChain::ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers)

The order of buffers returned by [**GetBuffer**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer) never changes.

[**IDXGISwapChain3::GetCurrentBackBufferIndex**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiswapchain3-getcurrentbackbufferindex) returns the index of the current back buffer to the app.

### Swap effects

The only supported swap effects are [**DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL**](/windows/win32/api/dxgi/ne-dxgi-dxgi_swap_effect) and [**DXGI_SWAP_EFFECT_FLIP_DISCARD**](/windows/win32/api/dxgi/ne-dxgi-dxgi_swap_effect), which requires the buffer count to be greater than one.

### Transitioning between windowed and full-screen modes

Direct3D 12 doesn't support full-screen exclusive mode (FSE). Instead, when a game is the only visible application on-screen, the OS uses a strategy called full-screen optimisations (FSO) to achieve a similar effect to FSE without the performance drawbacks. For more info about FSO, see [Demystifying Fullscreen Optimisations](https://devblogs.microsoft.com/directx/demystifying-full-screen-optimizations/).

Direct3D 12 maintains the restriction that applications must call [**ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) after transitioning between windowed and full-screen modes (D3D11 flip-model swap chains have the same restrictions).

The [**IDXGISwapChain::SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate) transitions do not change the set of app-visible buffers in the swap chain. Only the [**ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) and [**ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget) calls create or destroy app-visible buffers. However, in Direct3D 12 [**IDXGISwapChain::SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate) doesn't enter full-screen exclusive mode, and simply changes resolutions and refresh rates to allow full-screen optimisations. These changes can be made by an app without the use of this method

When or [**IDXGISwapChain::Present**](/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-present) or [**IDXGISwapChain1::Present**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-present1) is called, the back buffer to be presented must be in the [**D3D12\_RESOURCE\_STATE\_PRESENT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_states) state. Present will fail with **DXGI\_ERROR\_INVALID\_CALL** if this is not the case.

Full-screen swap chains continue to have the restriction that [**SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate)(FALSE, NULL) must be called before the final release of the swap chain. **SetFullscreenState**(FALSE) succeeds on swap chains running on Direct3D 12 devices.

Present operations occur on the 3D queue provided at swapchain creation, and apps are free to concurrently present multiple swap chains, and record and execute command lists.

When the final part of the graphics work (for example, frame postprocessing) is done on a compute queue, or doesn't involve the device's graphics queue, creating a second 3D queue to present on can be beneficial and prevent the latency of presentation delaying the start of the next frame. 

### Example

The following example code would be present in the main rendering loop:

```cpp
void Present()
{
    m_swapChain->Present(0, m_presentFlags);
    m_backBufferIndex = (m_backBufferIndex + 1) % m_backBufferCount;
}
```

### Creating swap chains

When using the [**CreateSwapChainForHwnd**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforhwnd), [**CreateSwapChainForCoreWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcorewindow), or [**CreateSwapChainForComposition**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcomposition) calls, note that the *pDevice* parameter actually requires a pointer to a direct command queue in Direct3D 12, and not a device.

### Presenting on Windows 7

When targeting Direct3D 12 on Windows 7, the necessary DXGI types for Direct3D 12 are not present, so you must use the D3D12On7-provided **ID3D12CommandQueueDownLevel** (queried off of the direct command queue) to present.

You provide an open command list to the Windows 7 present method, which will then be used, closed, and automatically submitted to the device for you. You must provide a back buffer which must be app-created, must be a committed resource, must be single-sampled, and must be one of the following formats.

* **DXGI_FORMAT_R16G16B16A16_FLOAT**
* **DXGI_FORMAT_R10G10B10A2_UNORM**
* **DXGI_FORMAT_R8G8B8A8_UNORM**
* **DXGI_FORMAT_R8G8B8A8_UNORM_SRGB**
* **DXGI_FORMAT_B8G8R8X8_UNORM**
* **DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM**
* **DXGI_FORMAT_B8G8R8A8_UNORM**
* **DXGI_FORMAT_B8G8R8A8_UNORM_SRGB**

## Related topics

* [D3D12_HEAP_FLAGS](/windows/win32/api/d3d12/ne-d3d12-d3d12_heap_flags)
* [DirectX advanced learning video tutorials : Unthrottled Framerate](https://www.youtube.com/watch?v=wn02zCXa9IU)
* [Rendering](rendering.md)
