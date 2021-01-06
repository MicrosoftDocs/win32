---
description: Variable refresh rate displays require tearing to be enabled, this is also known as &\#0034;vsync-off&\#0034; support.
ms.assetid: C5F140DD-5BAF-404A-9253-611831C4D424
title: Variable refresh rate displays
ms.topic: article
ms.date: 05/31/2018
---

# Variable refresh rate displays

Variable refresh rate displays require *tearing* to be enabled, this is also known as "vsync-off" support.

-   [Variable refresh rate displays/Vsync off](#variable-refresh-rate-displaysvsync-off)
-   [Related topics](#related-topics)

## Variable refresh rate displays/Vsync off

Support for variable refresh rate displays is achieved by setting certain flags when creating and presenting the swap chain.

To use this feature, app users need to be on Windows 10 systems with either [KB3156421](https://support.microsoft.com/kb/3156421) or the Anniversary Update installed. The feature works on all versions of Direct3D 11 and 12 using **DXGI\_SWAP\_EFFECT\_FLIP\_\*** swap effects.

To add vsync-off support to your apps, you can refer to a complete running sample for Direct3D 12, **D3D12Fullscreen** (refer to [Working Samples](../direct3d12/working-samples.md)). There are also a few points not explicitly called out in the sample code but you need to pay attention to.

-   [**ResizeBuffers**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-resizebuffers) (or [**ResizeBuffers1**](/windows/desktop/api/DXGI1_4/nf-dxgi1_4-idxgiswapchain3-resizebuffers1)) must have the same swap chain creation flag (DXGI\_SWAP\_CHAIN\_FLAG\_ALLOW\_TEARING) passed to it as [**Present**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-present) (or [**Present1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-present1)).
-   DXGI\_PRESENT\_ALLOW\_TEARING can only be used with sync interval 0. It is recommended to always pass this tearing flag when using sync interval 0 if [**CheckFeatureSupport**](/windows/desktop/api/DXGI1_5/nf-dxgi1_5-idxgifactory5-checkfeaturesupport) reports that tearing is supported *and* the app is in a windowed mode - including border-less fullscreen mode. Refer to the [**DXGI\_PRESENT**](dxgi-present.md) constants for more details.
-   Disabling vsync does not necessarily uncap your frame rate: developers also need to make sure [**Present**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-present) calls are not throttled by other timing events (such as the `CompositionTarget::Rendering` event in an XAML-based app).

The code below recaps a few key pieces you need to add to your apps.

``` syntax
//--------------------------------------------------------------------------------------------------------
// Check Tearing Support
//--------------------------------------------------------------------------------------------------------

// Determines whether tearing support is available for fullscreen borderless windows.

void DXSample::CheckTearingSupport()
{
// Rather than create the 1.5 factory interface directly, we create the 1.4
// interface and query for the 1.5 interface. This will enable the graphics
// debugging tools which might not support the 1.5 factory interface.

    ComPtr<IDXGIFactory4> factory4;
    HRESULT hr = CreateDXGIFactory1(IID_PPV_ARGS(&factory4));
    BOOL allowTearing = FALSE;
    if (SUCCEEDED(hr))
    { 
        ComPtr<IDXGIFactory5> factory5;
        hr = factory4.As(&factory5);
        if (SUCCEEDED(hr))
        {
            hr = factory5->CheckFeatureSupport(DXGI_FEATURE_PRESENT_ALLOW_TEARING, &allowTearing, sizeof(allowTearing));
        }
    }
    m_tearingSupport = SUCCEEDED(hr) && allowTearing;
}

//--------------------------------------------------------------------------------------------------------
// Set up swapchain properly
//--------------------------------------------------------------------------------------------------------

// It is recommended to always use the tearing flag when it is supported.
swapChainDesc.Flags = m_tearingSupport ? DXGI_SWAP_CHAIN_FLAG_ALLOW_TEARING : 0;

//--------------------------------------------------------------------------------------------------------
// Present
//--------------------------------------------------------------------------------------------------------

UINT presentFlags = (m_tearingSupport && m_windowedMode) ? DXGI_PRESENT_ALLOW_TEARING : 0;

// Present the frame.
ThrowIfFailed(m_swapChain->Present(0, presentFlags));
```

## Related topics

<dl> <dt>

[DXGI 1.5 Improvements](dxgi-1-5-improvements.md)
</dt> <dt>

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
</dt> </dl>

 

 
