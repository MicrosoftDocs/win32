---
title: Platform Update for Windows 7
description: This topic describes improvements to components of the Windows 7 graphics stack that become available through the Platform Update for Windows 7.
ms.assetid: C6DC0D38-E17C-4924-AF7C-6AE74C6C50D1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Platform Update for Windows 7

This topic describes improvements to components of the Windows 7 graphics stack that become available through the [Platform Update for Windows 7](http://support.microsoft.com/kb/2670838).

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

-   [What's new in Direct2D for Windows 8 (Windows)](https://msdn.microsoft.com/library/windows/desktop/hh802478)
-   [What's new in DirectWrite for Windows 8 (Windows)](https://msdn.microsoft.com/library/windows/desktop/hh802480)
-   [What’s New for WIC in Windows 8 (Windows)](https://msdn.microsoft.com/library/windows/desktop/hh994467)

See these topics for info about Direct3D and DXGI with the platform update:

-   [D3D11.1 Features](https://msdn.microsoft.com/library/windows/desktop/hh404562)
-   [DXGI 1.2 Improvements](https://msdn.microsoft.com/library/windows/desktop/hh404490)

After the platform update has been installed, the interfaces introduced in Direct3D11.1 and DXGI 1.2 will be available with partial functionality. The features of these graphics components are tied directly to the graphics kernel components, graphics drivers, and graphics hardware. Before using Direct3D11.1 on Windows 7, be familiar with these specifics:

-   Windows 8 introduced the WDDM 1.2 driver model, which provided improvements across the associated API surface for all [feature levels](https://msdn.microsoft.com/library/windows/desktop/ff476876). When reading the Direct3D11.1 documentation, understand that *new drivers* means WDDM 1.2 drivers. These updated driver versions, as well as most optional features exposed through [**CheckFeatureSupport**](https://msdn.microsoft.com/library/windows/desktop/ff476497), are unavailable on Windows 7. Since there is no guarantee that these optional features are available, make sure your applications have appropriate fallback behaviors in the event that the desired functionality is unavailable.

    There’s one important exception. Several features, such as [**PSSetConstantBuffers1**](https://msdn.microsoft.com/library/windows/desktop/hh404649) with constant buffer offsets, require new drivers for [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876) 10 and higher, but are actually emulated for feature level 9. This emulation is available on Windows 7 with the platform update. See [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](https://msdn.microsoft.com/library/windows/desktop/hh404457) for more info about which features are emulated.

-   The Windows 8 WDDM 1.2 driver model supports a new generation of hardware, exposed through D3D [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876) 11.1. Windows 7 with the platform update supports only the WDDM 1.1 driver model and therefore, feature level 11.1 hardware support is not available (through the platform update). On Windows 7 with the platform update, [**D3D11CreateDevice**](https://msdn.microsoft.com/library/windows/desktop/ff476082) always returns a feature level of 11.0 or lower, except for with a reference device that can be used to test an 11.1 code path on Windows 7. Only use features available at your target feature levels, as described in the feature level reference.
-   Some new methods introduced in DGXI 1.2 are not fully supported with the Platform Update for Windows 7.You can test for the availability of these functions by calling them directly and checking for an error code. Make sure your applications targeting Windows 7 with the platform update have a fallback in place when the desired functionality is unavailable. These classes of features are unavailable on Platform Update for Windows 7:

    -   Stereo
    -   Swapchains not targeting Hwnds
    -   Occlusion status notifications
    -   Desktop duplication
    -   NT Handle resources

    Specifically, the following APIs will return DXGI\_ERROR\_UNSUPPORTED, DXGI\_ERROR\_INVALID\_CALL, E\_NOTIMPL, or E\_INVALIDARG:

    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**CreateSwapChainForCoreWindow**](https://msdn.microsoft.com/library/windows/desktop/hh404559)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**CreateSwapChainForComposition**](https://msdn.microsoft.com/library/windows/desktop/hh404558)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**RegisterStereoStatusWindow**](https://msdn.microsoft.com/library/windows/desktop/hh404587)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**RegisterStereoStatusEvent**](https://msdn.microsoft.com/library/windows/desktop/hh404584)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**UnregisterStereoStatus**](https://msdn.microsoft.com/library/windows/desktop/hh404593)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**RegisterOcclusionStatusWindow**](https://msdn.microsoft.com/library/windows/desktop/hh404581)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**RegisterOcclusionStatusEvent**](https://msdn.microsoft.com/library/windows/desktop/hh404578)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**UnregisterOcclusionStatus**](https://msdn.microsoft.com/library/windows/desktop/hh404590)
    -   [**IDXGISwapChain1**](https://msdn.microsoft.com/library/windows/desktop/hh404631)::[**GetCoreWindow**](https://msdn.microsoft.com/library/windows/desktop/hh404650)
    -   [**IDXGISwapChain1**](https://msdn.microsoft.com/library/windows/desktop/hh404631)::[**SetRotation**](https://msdn.microsoft.com/library/windows/desktop/hh446801)
    -   [**IDXGISwapChain1**](https://msdn.microsoft.com/library/windows/desktop/hh404631)::[**GetRotation**](https://msdn.microsoft.com/library/windows/desktop/hh446791)
    -   [**IDXGIOutput1**](https://msdn.microsoft.com/library/windows/desktop/hh404597)::[**DuplicateOutput**](https://msdn.microsoft.com/library/windows/desktop/hh404600)
    -   [**IDXGIDevice2**](https://msdn.microsoft.com/library/windows/desktop/hh404543)::[**EnqueueSetEvent**](https://msdn.microsoft.com/library/windows/desktop/hh404546)
    -   [**IDXGIResource1**](https://msdn.microsoft.com/library/windows/desktop/hh404625)::[**CreateSharedHandle**](https://msdn.microsoft.com/library/windows/desktop/hh404626)
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**GetSharedResourceAdapterLuid**](https://msdn.microsoft.com/library/windows/desktop/hh404560)
    -   [**ID3D11Device1**](https://msdn.microsoft.com/library/windows/desktop/hh404575)::[**OpenSharedResource1**](https://msdn.microsoft.com/library/windows/desktop/hh404592)
    -   [**ID3D11Device1**](https://msdn.microsoft.com/library/windows/desktop/hh404575)::[**OpenSharedResourceByName**](https://msdn.microsoft.com/library/windows/desktop/hh404595)

-   These APIs have behavior differences, as noted:
    -   [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**CreateSwapChainForHwnd**](https://msdn.microsoft.com/library/windows/desktop/hh404557) takes a [**DXGI\_SWAP\_CHAIN\_DESC1**](https://msdn.microsoft.com/library/windows/desktop/hh404528) structure, which has a field for **Scaling**. [**DXGI\_SCALING\_NONE**](https://msdn.microsoft.com/library/windows/desktop/hh404526) is not supported on Windows 7 with the platform update and causes **CreateSwapChainForHwnd** to return DXGI\_ERROR\_INVALID\_CALL when called.
    -   [**IDXGISwapChain1**](https://msdn.microsoft.com/library/windows/desktop/hh404631)::[**SetBackgroundColor**](https://msdn.microsoft.com/library/windows/desktop/hh446799) is only useful when set on a swapchain using DXGI\_SCALING\_NONE. Its value is still stored and can be retrieved, but it has no effect.
    -   [**IDXGIDisplayControl**](https://msdn.microsoft.com/library/windows/desktop/hh404552)::[**IsStereoEnabled**](https://msdn.microsoft.com/library/windows/desktop/hh404553), [**IDXGIFactory2**](https://msdn.microsoft.com/library/windows/desktop/hh404556)::[**IsWindowedStereoEnabled**](https://msdn.microsoft.com/library/windows/desktop/hh404561), and [**IDXGISwapChain1**](https://msdn.microsoft.com/library/windows/desktop/hh404631)::[**IsTemporaryMonoSupported**](https://msdn.microsoft.com/library/windows/desktop/hh446794) all return **FALSE**.
    -   [**IDXGIOutput1**](https://msdn.microsoft.com/library/windows/desktop/hh404597)::[**GetDisplayModeList1**](https://msdn.microsoft.com/library/windows/desktop/hh404606) and **IDXGIOutput1**::[**FindClosestMatchingMode1**](https://msdn.microsoft.com/library/windows/desktop/hh404603) were added to facilitate stereo display modes. Stereo is not supported on the Platform Update for Windows 7 so this method is equivalent to [**IDXGIOutput**](https://msdn.microsoft.com/library/windows/desktop/bb174546)::[**FindClosestMatchingMode**](https://msdn.microsoft.com/library/windows/desktop/bb174547) as [**DXGI\_MODE\_DESC1**](https://msdn.microsoft.com/library/windows/desktop/hh404507).Stereo will always be FALSE.
    -   [**IDXGIDevice2**](https://msdn.microsoft.com/library/windows/desktop/hh404543)::[**OfferResources**](https://msdn.microsoft.com/library/windows/desktop/hh404549) and **IDXGIDevice2**::[**ReclaimResources**](https://msdn.microsoft.com/library/windows/desktop/hh404551) are not supported on the Platform Update for Windows 7. However, the runtime still allows them to be called, and performs validation that they are being used correctly on non-shared resources.
    -   [WARP](https://msdn.microsoft.com/library/windows/desktop/ff476871) devices only support [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876) 11.0. That is, WARP devices created by passing [D3D\_DRIVER\_TYPE\_WARP](https://msdn.microsoft.com/library/windows/desktop/ff476328) in the *DriverType* parameter of [**D3D11CreateDevice**](https://msdn.microsoft.com/library/windows/desktop/ff476082) don’t support 11.1 nor do they support shared surfaces.
-   For developers currently working on applications in Microsoft Visual Studio 2010 or earlier using the [**D3D11\_CREATE\_DEVICE\_DEBUG**](https://msdn.microsoft.com/library/windows/desktop/ff476107) flag, be aware that calls to [**D3D11CreateDevice**](https://msdn.microsoft.com/library/windows/desktop/ff476082) will fail. This is because the D3D11.1 runtime now requires D3D11\_1SDKLayers.dll instead of D3D11SDKLayers.dll. To get this new DLL (D3D11\_1SDKLayers.dll), install the [Windows 8 SDK](https://dev.windows.com/downloads/windows-8-sdk), or [Visual Studio 2012](http://www.microsoft.com/visualstudio/eng/downloads), or the Visual Studio 2012 remote debugging tools. See the [Debug Layer](https://msdn.microsoft.com/library/windows/desktop/ff476881) documentation for more info.

 

 




