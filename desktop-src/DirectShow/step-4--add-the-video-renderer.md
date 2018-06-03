---
Description: This topic is step 4 of the tutorial Audio/Video Playback in DirectShow.
ms.assetid: 34f35a95-1981-4467-a581-46db96c05224
title: 'Step 4: Add the Video Renderer'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Step 4: Add the Video Renderer

This topic is step 4 of the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md). The complete code is shown in the topic [DirectShow Playback Example](directshow-playback-example.md).

DirectShow provides several different filters that render video:

-   [**Enhanced Video Renderer Filter**](enhanced-video-renderer-filter.md) (EVR)
-   [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9)
-   [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7)

For more information about the differences between these filters, see [Choosing the Right Video Renderer](choosing-the-right-renderer.md).

In this tutorial, each video renderer filter is wrapped by a class that abstracts some of the differences between them. These classes all derive from an abstract base class named `CVideoRenderer`. The declaration of `CVideoRenderer` is shown in [Step 2: Declare CVideoRenderer and Derived Classes](step-2--declare-cvideorenderer-and-derived-classes.md).

The following method tries to create each video renderer in turn, starting with the EVR, then the VMR-9, and finally the VMR-7.


```C++
HRESULT DShowPlayer::CreateVideoRenderer()
{
    HRESULT hr = E_FAIL;

    enum { Try_EVR, Try_VMR9, Try_VMR7 };

    for (DWORD i = Try_EVR; i <= Try_VMR7; i++)
    {
        switch (i)
        {
        case Try_EVR:
            m_pVideo = new (std::nothrow) CEVR();
            break;

        case Try_VMR9:
            m_pVideo = new (std::nothrow) CVMR9();
            break;

        case Try_VMR7:
            m_pVideo = new (std::nothrow) CVMR7();
            break;
        }

        if (m_pVideo == NULL)
        {
            hr = E_OUTOFMEMORY;
            break;
        }

        hr = m_pVideo->AddToGraph(m_pGraph, m_hwnd);
        if (SUCCEEDED(hr))
        {
            break;
        }

        delete m_pVideo;
        m_pVideo = NULL;
    }
    return hr;
}

```



### EVR Filter

The following code creates the EVR filter and adds it to the filter graph. The function `AddFilterByCLSID` used in this example is shown in the topic [Add a Filter by CLSID](add-a-filter-by-clsid.md).


```C++
HRESULT CEVR::AddToGraph(IGraphBuilder *pGraph, HWND hwnd)
{
    IBaseFilter *pEVR = NULL;

    HRESULT hr = AddFilterByCLSID(pGraph, CLSID_EnhancedVideoRenderer, 
        &amp;pEVR, L"EVR");

    if (FAILED(hr))
    {
        goto done;
    }

    hr = InitializeEVR(pEVR, hwnd, &amp;m_pVideoDisplay);
    if (FAILED(hr))
    {
        goto done;
    }

    // Note: Because IMFVideoDisplayControl is a service interface,
    // you cannot QI the pointer to get back the IBaseFilter pointer.
    // Therefore, we need to cache the IBaseFilter pointer.

    m_pEVR = pEVR;
    m_pEVR->AddRef();

done:
    SafeRelease(&amp;pEVR);
    return hr;
}
```



The `InitializeEVR` function initializes the EVR filter. This function performs the following steps.

1.  Queries the filter for the [**IMFGetService**](https://msdn.microsoft.com/windows/desktop/102a1dff-8419-4f86-a145-53ce3d0123f5) interface.
2.  Calls [**IMFGetService::GetService**](https://msdn.microsoft.com/windows/desktop/4287dd1f-1718-4231-bc62-b58e0e61d688) to get a pointer to the [**IMFVideoDisplayControl**](https://msdn.microsoft.com/windows/desktop/db9b4663-9240-484f-8c47-cb1f5daa238d) interface.
3.  Calls [**IMFVideoDisplayControl::SetVideoWindow**](https://msdn.microsoft.com/windows/desktop/50bc345c-ee44-4174-9b1a-e406041096b5) to set the video window.
4.  Calls [**IMFVideoDisplayControl::SetAspectRatioMode**](https://msdn.microsoft.com/windows/desktop/dd49a110-1c11-4eca-9e7b-6021f3bdd397) to configure the EVR to preserve the video aspect ratio.

The following code shows the `InitializeEVR` function.


```C++
HRESULT InitializeEVR( 
    IBaseFilter *pEVR,              // Pointer to the EVR
    HWND hwnd,                      // Clipping window
    IMFVideoDisplayControl** ppDisplayControl
    ) 
{ 
    IMFGetService *pGS = NULL;
    IMFVideoDisplayControl *pDisplay = NULL;

    HRESULT hr = pEVR->QueryInterface(IID_PPV_ARGS(&amp;pGS)); 
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pGS->GetService(MR_VIDEO_RENDER_SERVICE, IID_PPV_ARGS(&amp;pDisplay));
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the clipping window.
    hr = pDisplay->SetVideoWindow(hwnd);
    if (FAILED(hr))
    {
        goto done;
    }

    // Preserve aspect ratio by letter-boxing
    hr = pDisplay->SetAspectRatioMode(MFVideoARMode_PreservePicture);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the IMFVideoDisplayControl pointer to the caller.
    *ppDisplayControl = pDisplay;
    (*ppDisplayControl)->AddRef();

done:
    SafeRelease(&amp;pGS);
    SafeRelease(&amp;pDisplay);
    return hr; 
} 
```



After the graph is built, the `DShowPlayer::RenderStreams` calls `CVideoRenderer::FinalizeGraph`. This method performs any final initialization or cleanup. The following code shows the `CEVR` implementation of this method.


```C++
HRESULT CEVR::FinalizeGraph(IGraphBuilder *pGraph)
{
    if (m_pEVR == NULL)
    {
        return S_OK;
    }

    BOOL bRemoved;
    HRESULT hr = RemoveUnconnectedRenderer(pGraph, m_pEVR, &amp;bRemoved);
    if (bRemoved)
    {
        SafeRelease(&amp;m_pEVR);
        SafeRelease(&amp;m_pVideoDisplay);
    }
    return hr;
}
```



If the EVR is not connected to any other filter, this method removes the EVR from the graph. This can occur if the media file does not contain a video stream.

### VMR-9 Filter

The following code creates the VMR-9 filter and adds it to the filter graph.


```C++
HRESULT CVMR9::AddToGraph(IGraphBuilder *pGraph, HWND hwnd)
{
    IBaseFilter *pVMR = NULL;

    HRESULT hr = AddFilterByCLSID(pGraph, CLSID_VideoMixingRenderer9, 
        &amp;pVMR, L"VMR-9");
    if (SUCCEEDED(hr))
    {
        // Set windowless mode on the VMR. This must be done before the VMR 
        // is connected.
        hr = InitWindowlessVMR9(pVMR, hwnd, &amp;m_pWindowless);
    }
    SafeRelease(&amp;pVMR);
    return hr;
}
```



The `InitWindowlessVMR9` function initializes the VMR-9 for windowless mode. (For more information about windowless mode, see [VMR Windowless Mode](vmr-windowless-mode.md).) This function performs the following steps.

1.  Queries the VMR-9 filter for the [**IVMRFilterConfig9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9) interface.
2.  Calls the [**IVMRFilterConfig9::SetRenderingMode**](/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode) method to set windowless mode.
3.  Queries the VMR-9 filter for the [**IVMRWindowlessControl9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9) interface.
4.  Calls the [**IVMRWindowlessControl9::SetVideoClippingWindow**](/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-setvideoclippingwindow) method to set the video window.
5.  Calls the [**IVMRWindowlessControl9::SetAspectRatioMode**](/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-setaspectratiomode) method to preserve the video aspect ratio.

The following code shows the `InitWindowlessVMR9` function.


```C++
HRESULT InitWindowlessVMR9( 
    IBaseFilter *pVMR,              // Pointer to the VMR
    HWND hwnd,                      // Clipping window
    IVMRWindowlessControl9** ppWC   // Receives a pointer to the VMR.
    ) 
{ 

    IVMRFilterConfig9 * pConfig = NULL; 
    IVMRWindowlessControl9 *pWC = NULL;

    // Set the rendering mode.  
    HRESULT hr = pVMR->QueryInterface(IID_PPV_ARGS(&amp;pConfig)); 
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pConfig->SetRenderingMode(VMR9Mode_Windowless); 
    if (FAILED(hr))
    {
        goto done;
    }

    // Query for the windowless control interface.
    hr = pVMR->QueryInterface(IID_PPV_ARGS(&amp;pWC));
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the clipping window.
    hr = pWC->SetVideoClippingWindow(hwnd);
    if (FAILED(hr))
    {
        goto done;
    }

    // Preserve aspect ratio by letter-boxing
    hr = pWC->SetAspectRatioMode(VMR9ARMode_LetterBox);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the IVMRWindowlessControl pointer to the caller.
    *ppWC = pWC;
    (*ppWC)->AddRef();

done:
    SafeRelease(&amp;pConfig);
    SafeRelease(&amp;pWC);
    return hr; 
} 
```



The `CVMR9::FinalizeGraph` method checks if the VMR-9 filter is connected, and if not, removes it from the filter graph.


```C++
HRESULT CVMR9::FinalizeGraph(IGraphBuilder *pGraph)
{
    if (m_pWindowless == NULL)
    {
        return S_OK;
    }

    IBaseFilter *pFilter = NULL;

    HRESULT hr = m_pWindowless->QueryInterface(IID_PPV_ARGS(&amp;pFilter));
    if (FAILED(hr))
    {
        goto done;
    }

    BOOL bRemoved;
    hr = RemoveUnconnectedRenderer(pGraph, pFilter, &amp;bRemoved);

    // If we removed the VMR, then we also need to release our 
    // pointer to the VMR's windowless control interface.
    if (bRemoved)
    {
        SafeRelease(&amp;m_pWindowless);
    }

done:
    SafeRelease(&amp;pFilter);
    return hr;
}
```



### VMR-7 Filter

The steps for the VMR-7 filter are nearly identical to those for the VMR-9, except the VMR-7 interfaces are used instead. The following code creates the VMR-7 filter and adds it to the filter graph.


```C++
HRESULT CVMR7::AddToGraph(IGraphBuilder *pGraph, HWND hwnd)
{
    IBaseFilter *pVMR = NULL;

    HRESULT hr = AddFilterByCLSID(pGraph, CLSID_VideoMixingRenderer, 
        &amp;pVMR, L"VMR-7");

    if (SUCCEEDED(hr))
    {
        // Set windowless mode on the VMR. This must be done before the VMR
        // is connected.
        hr = InitWindowlessVMR(pVMR, hwnd, &amp;m_pWindowless);
    }
    SafeRelease(&amp;pVMR);
    return hr;
}
```



The `InitWindowlessVMR` function initializes the VMR-7 for windowless mode. This function performs the following steps.

1.  Queries the VMR-7 filter for the [**IVMRFilterConfig**](/windows/desktop/api/Strmif/nn-strmif-ivmrfilterconfig) interface.
2.  Calls the [**IVMRFilterConfig::SetRenderingMode**](/windows/desktop/api/Strmif/nf-strmif-ivmrfilterconfig-setrenderingmode) method to set windowless mode.
3.  Queries the VMR-7 filter for the [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol) interface.
4.  Calls the [**IVMRWindowlessControl::SetVideoClippingWindow**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-setvideoclippingwindow) method to set the video window.
5.  Calls the [**IVMRWindowlessControl::SetAspectRatioMode**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-setaspectratiomode) method to preserve the video aspect ratio.

The following code shows the `InitWindowlessVMR` function.


```C++
HRESULT InitWindowlessVMR( 
    IBaseFilter *pVMR,              // Pointer to the VMR
    HWND hwnd,                      // Clipping window
    IVMRWindowlessControl** ppWC    // Receives a pointer to the VMR.
    ) 
{ 

    IVMRFilterConfig* pConfig = NULL; 
    IVMRWindowlessControl *pWC = NULL;

    // Set the rendering mode.  
    HRESULT hr = pVMR->QueryInterface(IID_PPV_ARGS(&amp;pConfig)); 
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pConfig->SetRenderingMode(VMRMode_Windowless); 
    if (FAILED(hr))
    {
        goto done;
    }

    // Query for the windowless control interface.
    hr = pVMR->QueryInterface(IID_PPV_ARGS(&amp;pWC));
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the clipping window.
    hr = pWC->SetVideoClippingWindow(hwnd);
    if (FAILED(hr))
    {
        goto done;
    }

    // Preserve aspect ratio by letter-boxing
    hr = pWC->SetAspectRatioMode(VMR_ARMODE_LETTER_BOX);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the IVMRWindowlessControl pointer to the caller.
    *ppWC = pWC;
    (*ppWC)->AddRef();

done:
    SafeRelease(&amp;pConfig);
    SafeRelease(&amp;pWC);
    return hr; 
} 
```



The `CVMR7::FinalizeGraph` method checks if the VMR-7 filter is connected, and if not, removes it from the filter graph.


```C++
HRESULT CVMR7::FinalizeGraph(IGraphBuilder *pGraph)
{
    if (m_pWindowless == NULL)
    {
        return S_OK;
    }

    IBaseFilter *pFilter = NULL;

    HRESULT hr = m_pWindowless->QueryInterface(IID_PPV_ARGS(&amp;pFilter));
    if (FAILED(hr))
    {
        goto done;
    }

    BOOL bRemoved;
    hr = RemoveUnconnectedRenderer(pGraph, pFilter, &amp;bRemoved);

    // If we removed the VMR, then we also need to release our 
    // pointer to the VMR's windowless control interface.
    if (bRemoved)
    {
        SafeRelease(&amp;m_pWindowless);
    }

done:
    SafeRelease(&amp;pFilter);
    return hr;
}
```



## Related topics

<dl> <dt>

[DirectShow Playback Example](directshow-playback-example.md)
</dt> <dt>

[Using the DirectShow EVR Filter](https://msdn.microsoft.com/windows/desktop/4d85aed0-4b11-4c5f-bfc0-cad0a7d2f490)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



