---
Description: 'The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.2.'
ms.assetid: 'E2D8DA99-4EA2-4847-B699-80A6994C66C0'
title: 'DXGI 1.2 Improvements'
---

# DXGI 1.2 Improvements

The following functionality has been added in Microsoft DirectX Graphics Infrastructure (DXGI) 1.2.

-   [Presentation enhancements and optimizations](#presentation-enhancements-and-optimizations)
-   [Desktop duplication](#desktop-duplication)
-   [Improved usage of shared resources and synchronized events](#improved-usage-of-shared-resources-and-synchronized-events)
-   [Offer the video memory of resources](#offer-the-video-memory-of-resources)
-   [GPU preemption at finer granularity levels for WDDM 1.2 driver model](#gpu-preemption-at-finer-granularity-levels-for-wddm-12-driver-model)
-   [Debugging APIs](#debugging-apis)
-   [Related topics](#related-topics)

## Presentation enhancements and optimizations

DXGI 1.2 enhances presentation with a new flip-model swap chain, content protection, windowless presentation, and optimized presentation wherein you specify dirty rectangles and scrolled areas. Presentation is also enhanced with stereoscopic 3D display behavior.

You can use the following DXGI 1.2 API for enhanced presentation.

-   [**IDXGIDisplayControl::IsStereoEnabled**](direct3ddxgi.idxgidisplaycontrol_isstereoenabled)
-   [**IDXGIDisplayControl::SetStereoEnabled**](direct3ddxgi.idxgidisplaycontrol_setstereoenabled)
-   [**IDXGIFactory2::CreateSwapChainForHwnd**](idxgifactory2-createswapchain1.md)
-   [**IDXGIFactory2::CreateSwapChainForCoreWindow**](idxgifactory2-createswapchainforimmersivewindow.md)
-   [**IDXGIFactory2::CreateSwapChainForComposition**](idxgifactory2-createswapchainforcompositionsurface.md)
-   [**IDXGIFactory2::IsWindowedStereoEnabled**](idxgifactory2-iswindowedstereoenabled.md)
-   [**IDXGIFactory2::RegisterStereoStatusWindow**](direct3ddxgi.idxgifactory2_registerstereostatuswindow)
-   [**IDXGIFactory2::RegisterStereoStatusEvent**](direct3ddxgi.idxgifactory2_registerstereostatusevent)
-   [**IDXGIFactory2::UnregisterStereoStatus**](direct3ddxgi.idxgifactory2_unregisterstereostatus)
-   [**IDXGIFactory2::RegisterOcclusionStatusWindow**](idxgifactory2-registerocclusionstatuswindow.md)
-   [**IDXGIFactory2::RegisterOcclusionStatusEvent**](idxgifactory2-registerocclusionstatusevent.md)
-   [**IDXGIFactory2::UnregisterOcclusionStatus**](idxgifactory2-unregisterocclusionstatus.md)
-   [**IDXGIOutput1::GetDisplayModeList1**](idxgioutput1-getdisplaymodelist1.md)
-   [**IDXGIOutput1::GetDisplaySurfaceData1**](idxgioutput1-getdisplaysurfacedata1.md)
-   [**IDXGIOutput1::FindClosestMatchingMode1**](idxgioutput1-findclosestmatchingmode1.md)
-   [**IDXGIResource1::CreateSubresourceSurface**](idxgiresource1-createsubresourcesurface.md)
-   [**IDXGISurface2::GetResource**](idxgisurface2-getresource.md)
-   [**IDXGISwapChain1::GetDesc1**](idxgiswapchain1-getdesc1.md)
-   [**IDXGISwapChain1::GetFullscreenDesc**](idxgiswapchain1-getfullscreendesc.md)
-   [**IDXGISwapChain1::GetHwnd**](idxgiswapchain1-gethwnd.md)
-   [**IDXGISwapChain1::GetCoreWindow**](idxgiswapchain1-getimmersivewindow.md)
-   [**IDXGISwapChain1::Present1**](idxgiswapchain1-present1.md)
-   [**IDXGISwapChain1::IsTemporaryMonoSupported**](idxgiswapchain1-istemporarymonosupported.md)
-   [**IDXGISwapChain1::GetRestrictToOutput**](idxgiswapchain1-getrestricttooutput.md)
-   [**IDXGISwapChain1::SetBackgroundColor**](idxgiswapchain1-setbackgroundcolor.md)
-   [**IDXGISwapChain1::GetBackgroundColor**](idxgiswapchain1-getbackgroundcolor.md)
-   [**IDXGISwapChain1::SetRotation**](idxgiswapchain1-setrotation.md)
-   [**IDXGISwapChain1::GetRotation**](idxgiswapchain1-getrotation.md)

For more info about how to use the DXGI 1.2 API for enhanced presentation, see [Enhancing presentation with the flip model, dirty rectangles, and scrolled areas](dxgi-1-2-presentation-improvements.md).

For info about how to determine whether you can render in stereo, see [Rendering in stereo and notifying about stereo status](stereo-rendering-stereo-status-notifying.md).

For info about how to determine changes in your app's occlusion status, see [Waiting on an event when rendering is unnecessary](waiting-when-occluded.md).

For info about how data values change when you present content to the screen, see [Converting data for the color space](converting-data-color-space.md).

## Desktop duplication

Windows 8 disables standard Windows 2000 Display Driver Model (XDDM) mirror drivers. DXGI 1.2 provides the desktop duplication API as an alternative. The desktop duplication API provides remote access to the desktop image for collaboration scenarios.

The desktop duplication API consists of the following methods.

-   [**IDXGIOutput1::DuplicateOutput**](idxgioutput1-duplicateoutput.md)
-   [**IDXGIOutputDuplication::GetDesc**](idxgioutputduplication-getdesc.md)
-   [**IDXGIOutputDuplication::AcquireNextFrame**](idxgioutputduplication-acquirenextframe.md)
-   [**IDXGIOutputDuplication::GetFrameDirtyRects**](idxgioutputduplication-getframedirtyrects.md)
-   [**IDXGIOutputDuplication::GetFrameMoveRects**](idxgioutputduplication-getframemoverects.md)
-   [**IDXGIOutputDuplication::GetFramePointerShape**](idxgioutputduplication-getframepointershape.md)
-   [**IDXGIOutputDuplication::MapDesktopSurface**](idxgioutputduplication-mapdesktopsurface.md)
-   [**IDXGIOutputDuplication::UnMapDesktopSurface**](idxgioutputduplication-unmapdesktopsurface.md)
-   [**IDXGIOutputDuplication::ReleaseFrame**](idxgioutputduplication-releaseframe.md)

For more info about how to use the desktop duplication API, see [Desktop Duplication API](desktop-dup-api.md).

## Improved usage of shared resources and synchronized events

In previous versions of Windows, apps use continuous polling to determine whether the graphics processing unit (GPU) is finished processing arbitrary commands. DXGI 1.2 enables an app to queue an event to a DXGI device. The app can then wait for the DXGI device to signal the event to determine that the GPU finished executing all rendering commands. DXGI 1.2 enables multiple devices to share a resource through a NT handle.

You can use the following DXGI 1.2 API and Direct3D 11.1 API to share resources and synchronize events.

-   [**IDXGIDevice2::EnqueueSetEvent**](idxgidevice2-enqueuesetevent.md)
-   [**IDXGIResource1::CreateSharedHandle**](idxgiresource1-createsharedhandle.md)
-   [**IDXGIFactory2::GetSharedResourceAdapterLuid**](idxgifactory2-getsharedresourceadapterluid.md)
-   [**ID3D11Device1::OpenSharedResource1**](direct3d11.id3d11device1_opensharedresource1)
-   [**ID3D11Device1::OpenSharedResourceByName**](direct3d11.id3d11device1_opensharedresourcebyname)
-   [**D3D11\_RESOURCE\_MISC\_SHARED\_NTHANDLE**](direct3d11.d3d11_resource_misc_flag#d3d11-resource-misc-shared-nthandle)

## Offer the video memory of resources

DXGI 1.2 enables an app to offer the video memory of its resources with low overhead. By offering the video memory, the operating system can free the video memory.

This DXGI 1.2 feature consists of the following methods.

-   [**IDXGIDevice2::OfferResources**](idxgidevice2-offerresources.md)
-   [**IDXGIDevice2::ReclaimResources**](idxgidevice2-reclaimresources.md)

You can use the [**ID3D11Debug::SetFeatureMask**](direct3d11.id3d11debug_setfeaturemask) method to set feature-mask flags that debug the behavior of the [**IDXGIDevice2::OfferResources**](idxgidevice2-offerresources.md) and [**IDXGIDevice2::ReclaimResources**](idxgidevice2-reclaimresources.md) methods in your app.

The [Direct3D 11.1 Offer and Reclaim Resources Sample](http://go.microsoft.com/fwlink/p/?linkid=239948) shows how to use these APIs.

## GPU preemption at finer granularity levels for WDDM 1.2 driver model

Starting with the Windows Display Driver Model (WDDM) 1.2 driver model, the WDDM scheduler can preempt the GPU's execution of application tasks at finer granularity levels. DXGI 1.2 lets you determine the GPU preemption granularity levels.

This DXGI 1.2 feature consists of the following method.

-   [**IDXGIAdapter2::GetDesc2**](idxgiadapter2-getdesc2.md)

## Debugging APIs

The Windows 8 SDK provides additional debugging capability. You can use the following DXGI APIs from Dxgidebug.dll to debug your app:

-   [**DXGIGetDebugInterface**](dxgigetdebuginterface.md)
-   [**IDXGIDebug**](idxgidebug.md)
-   [**IDXGIInfoQueue**](idxgiinfoqueue.md)

To access [**DXGIGetDebugInterface**](dxgigetdebuginterface.md), call the [**GetModuleHandle**](base.getmodulehandle) function to get Dxgidebug.dll and the [**GetProcAddress**](base.getprocaddress) function to get the address of **DXGIGetDebugInterface**. You can then call **DXGIGetDebugInterface** to obtain the [**IDXGIDebug**](idxgidebug.md) or [**IDXGIInfoQueue**](idxgiinfoqueue.md) interface.

For info about how to debug DirectX apps remotely, see [Debugging DirectX apps remotely](direct3dtools.debugging_directx_apps_remotely).

## Related topics

<dl> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 



