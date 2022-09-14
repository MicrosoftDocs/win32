---
description: The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.3, which is included starting in Windows 8.1.
ms.assetid: 56816212-2B6A-41EC-B57D-29DEBBF440E7
title: DXGI 1.3 Improvements
ms.topic: article
ms.date: 05/31/2018
---

# DXGI 1.3 Improvements

The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.3, which is included starting in Windows 8.1.

## Trim DXGI adapter memory usage

Starting in Windows 8.1, DXGI 1.3 adds the capability to flush and release unused memory resources allocated by the DXGI adapter. This allows apps to release temporary memory while suspending, reducing the chance the app will be terminated to free resources for other apps. When the app resumes, device drivers that support trim will recreate resources as they are needed. As of Windows 8.1, all Direct3D devices created by an app must call [**IDXGIDevice3::Trim**](/windows/desktop/api/DXGI1_3/nf-dxgi1_3-idxgidevice3-trim) when suspending to reduce memory footprint and reduce the chance that the app will be terminated to reclaim system resources.

## Multi-plane overlays

Starting in Windows 8.1, DXGI 1.3 supports multi-plane overlays. You can find out if the device supports multi-plane overlays in hardware by using [**IDXGIOutput2::SupportsOverlays**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgioutput2-supportsoverlays).

## Overlapping swap chains and swap chain scaling

Starting in Windows 8.1, DXGI 1.3 supports overlapping swap chains. Overlapping swap chains are used to draw 3D graphics at non-native resolutions (with hardware upscaling) while presenting UI at native resolution. This lets games take advantage of higher fill rates for responsive gameplay without degrading the visual quality of UI elements, such as player score and dialog text. On devices that support multi-plane overlays, Direct3D will use multi-plane overlays for overlapping swap chains. Create a foreground swap chain by specifying the [**DXGI\_SWAP\_CHAIN\_FLAG\_FOREGROUND\_LAYER**](/windows/win32/api/dxgi/ne-dxgi-dxgi_swap_chain_flag) flag when creating the swap chain, and use [**IDXGISwapChain2::SetMatrixTransform**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-setmatrixtransform) and [**IDXGISwapChain2::GetMatrixTransform**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-getmatrixtransform) to scale the swap chain used for gameplay.

## Select backbuffer subregion for swap chain

Starting in Windows 8.1, DXGI 1.3 can be used to select a subregion of the backbuffer for use with the swap chain, making it possible to render to a smaller back buffer without recreating the swap chain. See [**IDXGISwapChain2::SetSourceSize**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-setsourcesize) and [**IDXGISwapChain2::GetSourceSize**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-getsourcesize).

## Lower-latency swap chain presentation

Starting in Windows 8.1, DXGI 1.3 makes it possible to reduce latency by letting the swap chain finish presenting the previous frame before starting to use the device to draw the next frame. See [**IDXGISwapChain2::GetFrameLatencyWaitableObject**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-getframelatencywaitableobject), [**IDXGISwapChain2::GetMaximumFrameLatency**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-getmaximumframelatency), and [**IDXGISwapChain2::SetMaximumFrameLatency**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-idxgiswapchain2-setmaximumframelatency).

## Related topics

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
