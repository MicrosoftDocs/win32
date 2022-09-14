---
title: Platform Update for Windows 7
description: This topic describes improvements to components of the Windows 7 graphics stack that become available through the Platform Update for Windows 7.
ms.assetid: C6DC0D38-E17C-4924-AF7C-6AE74C6C50D1
ms.topic: article
ms.date: 05/31/2018
---

# Platform Update for Windows 7

This topic describes improvements to components of the Windows 7 graphics stack that become available through the [Platform Update for Windows 7](https://support.microsoft.com/kb/2670838).

When installed on Windows 7, the Platform Update for Windows 7 updates Windows 7 with functionality available in Windows 8. For example, these Windows 8 components become available with full functionality:

-   Direct2D 1.1 (including Direct2D Effects)
-   DirectWrite
-   Windows Imaging Component (WIC)

These provide partial functionality:

-   Direct3D 11.1
-   DXGI 1.2

And, for example, this component is not available:

-   DirectComposition (DComp)

See these topics for info about Direct2D, DirectWrite, and WIC with the platform update:

-   [What's new in Direct2D for Windows 8 (Windows)](/windows/desktop/Direct2D/what-s-new-in-direct2d-for-windows-8-consumer-preview)
-   [What's new in DirectWrite for Windows 8 (Windows)](/windows/desktop/DirectWrite/what-s-new-in-directwrite-for-windows-8-consumer-preview)
-   [What’s New for WIC in Windows 8 (Windows)](/previous-versions//hh994467(v=vs.85))

See these topics for info about Direct3D and DXGI with the platform update:

-   [D3D11.1 Features](/windows/desktop/direct3d11/direct3d-11-1-features)
-   [DXGI 1.2 Improvements](/windows/desktop/direct3ddxgi/dxgi-1-2-improvements)

After the platform update has been installed, the interfaces introduced in Direct3D11.1 and DXGI 1.2 will be available with partial functionality. The features of these graphics components are tied directly to the graphics kernel components, graphics drivers, and graphics hardware. Before using Direct3D11.1 on Windows 7, be familiar with these specifics:

-   Windows 8 introduced the WDDM 1.2 driver model, which provided improvements across the associated API surface for all [feature levels](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro). When reading the Direct3D11.1 documentation, understand that *new drivers* means WDDM 1.2 drivers. These updated driver versions, as well as most optional features exposed through [**CheckFeatureSupport**](/windows/desktop/api/d3d11/nf-d3d11-id3d11device-checkfeaturesupport), are unavailable on Windows 7. Since there is no guarantee that these optional features are available, make sure your applications have appropriate fallback behaviors in the event that the desired functionality is unavailable.

    There’s one important exception. Several features, such as [**PSSetConstantBuffers1**](/windows/desktop/api/d3d11_1/nf-d3d11_1-id3d11devicecontext1-pssetconstantbuffers1) with constant buffer offsets, require new drivers for [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 10 and higher, but are actually emulated for feature level 9. This emulation is available on Windows 7 with the platform update. See [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_feature_data_d3d11_options) for more info about which features are emulated.

-   The Windows 8 WDDM 1.2 driver model supports a new generation of hardware, exposed through D3D [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 11.1. Windows 7 with the platform update supports only the WDDM 1.1 driver model and therefore, feature level 11.1 hardware support is not available (through the platform update). On Windows 7 with the platform update, [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice) always returns a feature level of 11.0 or lower, except for with a reference device that can be used to test an 11.1 code path on Windows 7. Only use features available at your target feature levels, as described in the feature level reference.
-   Some new methods introduced in DGXI 1.2 are not fully supported with the Platform Update for Windows 7.You can test for the availability of these functions by calling them directly and checking for an error code. Make sure your applications targeting Windows 7 with the platform update have a fallback in place when the desired functionality is unavailable. These classes of features are unavailable on Platform Update for Windows 7:

    -   Stereo
    -   Swapchains not targeting Hwnds
    -   Occlusion status notifications
    -   Desktop duplication
    -   NT Handle resources

    Specifically, the following APIs will return DXGI\_ERROR\_UNSUPPORTED, DXGI\_ERROR\_INVALID\_CALL, E\_NOTIMPL, or E\_INVALIDARG:

    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**CreateSwapChainForCoreWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcorewindow)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**CreateSwapChainForComposition**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcomposition)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**RegisterStereoStatusWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerstereostatuswindow)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**RegisterStereoStatusEvent**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerstereostatusevent)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**UnregisterStereoStatus**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-unregisterstereostatus)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**RegisterOcclusionStatusWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatuswindow)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**RegisterOcclusionStatusEvent**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatusevent)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**UnregisterOcclusionStatus**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-unregisterocclusionstatus)
    -   [**IDXGISwapChain1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1)::[**GetCoreWindow**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-getcorewindow)
    -   [**IDXGISwapChain1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1)::[**SetRotation**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-setrotation)
    -   [**IDXGISwapChain1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1)::[**GetRotation**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-getrotation)
    -   [**IDXGIOutput1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgioutput1)::[**DuplicateOutput**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgioutput1-duplicateoutput)
    -   [**IDXGIDevice2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgidevice2)::[**EnqueueSetEvent**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgidevice2-enqueuesetevent)
    -   [**IDXGIResource1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiresource1)::[**CreateSharedHandle**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiresource1-createsharedhandle)
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**GetSharedResourceAdapterLuid**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-getsharedresourceadapterluid)
    -   [**ID3D11Device1**](/windows/desktop/api/d3d11_1/nn-d3d11_1-id3d11device1)::[**OpenSharedResource1**](/windows/desktop/api/d3d11_1/nf-d3d11_1-id3d11device1-opensharedresource1)
    -   [**ID3D11Device1**](/windows/desktop/api/d3d11_1/nn-d3d11_1-id3d11device1)::[**OpenSharedResourceByName**](/windows/desktop/api/d3d11_1/nf-d3d11_1-id3d11device1-opensharedresourcebyname)

-   These APIs have behavior differences, as noted:
    -   [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**CreateSwapChainForHwnd**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforhwnd) takes a [**DXGI\_SWAP\_CHAIN\_DESC1**](/windows/desktop/api/dxgi1_2/ns-dxgi1_2-dxgi_swap_chain_desc1) structure, which has a field for **Scaling**. [**DXGI\_SCALING\_NONE**](/windows/desktop/api/dxgi1_2/ne-dxgi1_2-dxgi_scaling) is not supported on Windows 7 with the platform update and causes **CreateSwapChainForHwnd** to return DXGI\_ERROR\_INVALID\_CALL when called.
    -   [**IDXGISwapChain1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1)::[**SetBackgroundColor**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-setbackgroundcolor) is only useful when set on a swapchain using DXGI\_SCALING\_NONE. Its value is still stored and can be retrieved, but it has no effect.
    -   [**IDXGIDisplayControl**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgidisplaycontrol)::[**IsStereoEnabled**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgidisplaycontrol-isstereoenabled), [**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2)::[**IsWindowedStereoEnabled**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-iswindowedstereoenabled), and [**IDXGISwapChain1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1)::[**IsTemporaryMonoSupported**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-istemporarymonosupported) all return **FALSE**.
    -   [**IDXGIOutput1**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgioutput1)::[**GetDisplayModeList1**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgioutput1-getdisplaymodelist1) and **IDXGIOutput1**::[**FindClosestMatchingMode1**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgioutput1-findclosestmatchingmode1) were added to facilitate stereo display modes. Stereo is not supported on the Platform Update for Windows 7 so this method is equivalent to [**IDXGIOutput**](/windows/desktop/api/dxgi/nn-dxgi-idxgioutput)::[**FindClosestMatchingMode**](/windows/desktop/api/dxgi/nf-dxgi-idxgioutput-findclosestmatchingmode) as [**DXGI\_MODE\_DESC1**](/windows/desktop/api/dxgi1_2/ns-dxgi1_2-dxgi_mode_desc1).Stereo will always be FALSE.
    -   [**IDXGIDevice2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgidevice2)::[**OfferResources**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgidevice2-offerresources) and **IDXGIDevice2**::[**ReclaimResources**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgidevice2-reclaimresources) are not supported on the Platform Update for Windows 7. However, the runtime still allows them to be called, and performs validation that they are being used correctly on non-shared resources.
    -   [WARP](/windows/desktop/direct3d11/overviews-direct3d-11-devices-create-warp) devices only support [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 11.0. That is, WARP devices created by passing [D3D\_DRIVER\_TYPE\_WARP](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_driver_type) in the *DriverType* parameter of [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice) don’t support 11.1 nor do they support shared surfaces.
-   For developers currently working on applications in Microsoft Visual Studio 2010 or earlier using the [**D3D11\_CREATE\_DEVICE\_DEBUG**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_create_device_flag) flag, be aware that calls to [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice) will fail. This is because the D3D11.1 runtime now requires D3D11\_1SDKLayers.dll instead of D3D11SDKLayers.dll. To get this new DLL (D3D11\_1SDKLayers.dll), install the [Windows 8 SDK](https://dev.windows.com/downloads/windows-8-sdk), or [Visual Studio 2012](https://www.microsoft.com/visualstudio/eng/downloads), or the Visual Studio 2012 remote debugging tools. See the [Debug Layer](/windows/desktop/direct3d11/overviews-direct3d-11-devices-layers) documentation for more info.

 

 