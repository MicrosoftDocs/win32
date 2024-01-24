---
description: The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.2.
ms.assetid: E2D8DA99-4EA2-4847-B699-80A6994C66C0
title: DXGI 1.2 improvements
ms.topic: article
ms.date: 05/31/2018
---

# DXGI 1.2 improvements

The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.2.

## Presentation enhancements and optimizations

DXGI 1.2 enhances presentation with a new flip-model swap chain, content protection, windowless presentation, and optimized presentation wherein you specify dirty rectangles and scrolled areas. Presentation is also enhanced with stereoscopic 3D display behavior.

You can use the following DXGI 1.2 API for enhanced presentation.

-   [**IDXGIDisplayControl::IsStereoEnabled**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgidisplaycontrol-isstereoenabled)
-   [**IDXGIDisplayControl::SetStereoEnabled**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgidisplaycontrol-setstereoenabled)
-   [**IDXGIFactory2::CreateSwapChainForHwnd**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-createswapchainforhwnd)
-   [**IDXGIFactory2::CreateSwapChainForCoreWindow**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcorewindow)
-   [**IDXGIFactory2::CreateSwapChainForComposition**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcomposition)
-   [**IDXGIFactory2::IsWindowedStereoEnabled**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-iswindowedstereoenabled)
-   [**IDXGIFactory2::RegisterStereoStatusWindow**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerstereostatuswindow)
-   [**IDXGIFactory2::RegisterStereoStatusEvent**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerstereostatusevent)
-   [**IDXGIFactory2::UnregisterStereoStatus**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-unregisterstereostatus)
-   [**IDXGIFactory2::RegisterOcclusionStatusWindow**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatuswindow)
-   [**IDXGIFactory2::RegisterOcclusionStatusEvent**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatusevent)
-   [**IDXGIFactory2::UnregisterOcclusionStatus**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-unregisterocclusionstatus)
-   [**IDXGIOutput1::GetDisplayModeList1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-getdisplaymodelist1)
-   [**IDXGIOutput1::GetDisplaySurfaceData1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-getdisplaysurfacedata1)
-   [**IDXGIOutput1::FindClosestMatchingMode1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-findclosestmatchingmode1)
-   [**IDXGIResource1::CreateSubresourceSurface**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiresource1-createsubresourcesurface)
-   [**IDXGISurface2::GetResource**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgisurface2-getresource)
-   [**IDXGISwapChain1::GetDesc1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getdesc1)
-   [**IDXGISwapChain1::GetFullscreenDesc**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getfullscreendesc)
-   [**IDXGISwapChain1::GetHwnd**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-gethwnd)
-   [**IDXGISwapChain1::GetCoreWindow**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getcorewindow)
-   [**IDXGISwapChain1::Present1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-present1)
-   [**IDXGISwapChain1::IsTemporaryMonoSupported**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-istemporarymonosupported)
-   [**IDXGISwapChain1::GetRestrictToOutput**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getrestricttooutput)
-   [**IDXGISwapChain1::SetBackgroundColor**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-setbackgroundcolor)
-   [**IDXGISwapChain1::GetBackgroundColor**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getbackgroundcolor)
-   [**IDXGISwapChain1::SetRotation**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-setrotation)
-   [**IDXGISwapChain1::GetRotation**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getrotation)

For more info about how to use the DXGI 1.2 API for enhanced presentation, see [Enhancing presentation with the flip model, dirty rectangles, and scrolled areas](dxgi-1-2-presentation-improvements.md).

For info about how to determine whether you can render in stereo, see [Rendering in stereo and notifying about stereo status](stereo-rendering-stereo-status-notifying.md).

For info about how to determine changes in your app's occlusion status, see [Waiting on an event when rendering is unnecessary](waiting-when-occluded.md).

For info about how data values change when you present content to the screen, see [Converting data for the color space](converting-data-color-space.md).

## Desktop duplication

Windows 8 disables standard Windows 2000 Display Driver Model (XDDM) mirror drivers. DXGI 1.2 provides the desktop duplication API as an alternative. The desktop duplication API provides remote access to the desktop image for collaboration scenarios.

The desktop duplication API consists of the following methods.

-   [**IDXGIOutput1::DuplicateOutput**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-duplicateoutput)
-   [**IDXGIOutputDuplication::GetDesc**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getdesc)
-   [**IDXGIOutputDuplication::AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe)
-   [**IDXGIOutputDuplication::GetFrameDirtyRects**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframedirtyrects)
-   [**IDXGIOutputDuplication::GetFrameMoveRects**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframemoverects)
-   [**IDXGIOutputDuplication::GetFramePointerShape**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframepointershape)
-   [**IDXGIOutputDuplication::MapDesktopSurface**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-mapdesktopsurface)
-   [**IDXGIOutputDuplication::UnMapDesktopSurface**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-unmapdesktopsurface)
-   [**IDXGIOutputDuplication::ReleaseFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-releaseframe)

For more info about how to use the desktop duplication API, see [Desktop Duplication API](desktop-dup-api.md).

## Improved usage of shared resources and synchronized events

In previous versions of Windows, apps use continuous polling to determine whether the graphics processing unit (GPU) is finished processing arbitrary commands. DXGI 1.2 enables an app to queue an event to a DXGI device. The app can then wait for the DXGI device to signal the event to determine that the GPU finished executing all rendering commands. DXGI 1.2 enables multiple devices to share a resource through a NT handle.

You can use the following DXGI 1.2 API and Direct3D 11.1 API to share resources and synchronize events.

-   [**IDXGIDevice2::EnqueueSetEvent**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-enqueuesetevent)
-   [**IDXGIResource1::CreateSharedHandle**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiresource1-createsharedhandle)
-   [**IDXGIFactory2::GetSharedResourceAdapterLuid**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-getsharedresourceadapterluid)
-   [**ID3D11Device1::OpenSharedResource1**](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11device1-opensharedresource1)
-   [**ID3D11Device1::OpenSharedResourceByName**](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11device1-opensharedresourcebyname)
-   [**D3D11\_RESOURCE\_MISC\_SHARED\_NTHANDLE**](/windows/win32/api/d3d11/ne-d3d11-d3d11_resource_misc_flag)

## Offer the video memory of resources

DXGI 1.2 enables an app to offer the video memory of its resources with low overhead. By offering the video memory, the operating system can free the video memory.

This DXGI 1.2 feature consists of the following methods.

-   [**IDXGIDevice2::OfferResources**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-offerresources)
-   [**IDXGIDevice2::ReclaimResources**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-reclaimresources)

You can use the [**ID3D11Debug::SetFeatureMask**](/windows/win32/api/d3d11sdklayers/nf-d3d11sdklayers-id3d11debug-setfeaturemask) method to set feature-mask flags that debug the behavior of the [**IDXGIDevice2::OfferResources**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-offerresources) and [**IDXGIDevice2::ReclaimResources**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-reclaimresources) methods in your app.

## GPU preemption at finer granularity levels for WDDM 1.2 driver model

Starting with the Windows Display Driver Model (WDDM) 1.2 driver model, the WDDM scheduler can preempt the GPU's execution of application tasks at finer granularity levels. DXGI 1.2 lets you determine the GPU preemption granularity levels.

This DXGI 1.2 feature consists of the following method.

-   [**IDXGIAdapter2::GetDesc2**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiadapter2-getdesc2)

## Debugging APIs

The Windows 8 SDK provides additional debugging capability. You can use the following DXGI APIs from Dxgidebug.dll to debug your app:

-   [**DXGIGetDebugInterface**](/windows/desktop/api/DXGIDebug/nf-dxgidebug-dxgigetdebuginterface)
-   [**IDXGIDebug**](/windows/desktop/api/DXGIDebug/nn-dxgidebug-idxgidebug)
-   [**IDXGIInfoQueue**](/windows/desktop/api/DXGIDebug/nn-dxgidebug-idxgiinfoqueue)

To access [**DXGIGetDebugInterface**](/windows/desktop/api/DXGIDebug/nf-dxgidebug-dxgigetdebuginterface), call the [**GetModuleHandle**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea) function to get Dxgidebug.dll and the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) function to get the address of **DXGIGetDebugInterface**. You can then call **DXGIGetDebugInterface** to obtain the [**IDXGIDebug**](/windows/desktop/api/DXGIDebug/nn-dxgidebug-idxgidebug) or [**IDXGIInfoQueue**](/windows/desktop/api/DXGIDebug/nn-dxgidebug-idxgiinfoqueue) interface.

For info about how to debug DirectX apps remotely, see [Debugging DirectX apps remotely](../direct3dtools/debugging-directx-apps-remotely.md).

## Related topics

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
