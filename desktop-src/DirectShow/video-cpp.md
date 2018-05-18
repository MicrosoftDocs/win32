---
Description: 'This topic contains code for the tutorial Audio/Video Playback in DirectShow.'
ms.assetid: 'c406a099-4956-46a8-b1f4-6d2e6ab3427a'
title: 'video.cpp'
---

# video.cpp

This topic contains code for the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md).


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (c) Microsoft Corporation. All rights reserved.

#include "video.h"
#include <Mfidl.h>

HRESULT InitializeEVR(IBaseFilter *pEVR, HWND hwnd, IMFVideoDisplayControl ** ppWc); 
HRESULT InitWindowlessVMR9(IBaseFilter *pVMR, HWND hwnd, IVMRWindowlessControl9 ** ppWc); 
HRESULT InitWindowlessVMR(IBaseFilter *pVMR, HWND hwnd, IVMRWindowlessControl** ppWc); 
HRESULT FindConnectedPin(IBaseFilter *pFilter, PIN_DIRECTION PinDir, IPin **ppPin);

/// VMR-7 Wrapper

CVMR7::CVMR7() : m_pWindowless(NULL)
{

}

CVMR7::~CVMR7()
{
    SafeRelease(&amp;m_pWindowless);
}

BOOL CVMR7::HasVideo() const 
{ 
    return (m_pWindowless != NULL); 
}

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

HRESULT CVMR7::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pWindowless == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pWindowless->SetVideoPosition(NULL, prc);
    }
    else
    {
        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pWindowless->SetVideoPosition(NULL, &amp;rc);
    }
}

HRESULT CVMR7::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pWindowless)
    {
        return m_pWindowless->RepaintVideo(hwnd, hdc);
    }
    else
    {
        return S_OK;
    }
}

HRESULT CVMR7::DisplayModeChanged()
{
    if (m_pWindowless)
    {
        return m_pWindowless->DisplayModeChanged();
    }
    else
    {
        return S_OK;
    }
}


// Initialize the VMR-7 for windowless mode. 

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


/// VMR-9 Wrapper

CVMR9::CVMR9() : m_pWindowless(NULL)
{

}

BOOL CVMR9::HasVideo() const 
{ 
    return (m_pWindowless != NULL); 
}

CVMR9::~CVMR9()
{
    SafeRelease(&amp;m_pWindowless);
}

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


HRESULT CVMR9::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pWindowless == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pWindowless->SetVideoPosition(NULL, prc);
    }
    else
    {

        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pWindowless->SetVideoPosition(NULL, &amp;rc);
    }
}

HRESULT CVMR9::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pWindowless)
    {
        return m_pWindowless->RepaintVideo(hwnd, hdc);
    }
    else
    {
        return S_OK;
    }
}

HRESULT CVMR9::DisplayModeChanged()
{
    if (m_pWindowless)
    {
        return m_pWindowless->DisplayModeChanged();
    }
    else
    {
        return S_OK;
    }
}


// Initialize the VMR-9 for windowless mode. 

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


/// EVR Wrapper

CEVR::CEVR() : m_pEVR(NULL), m_pVideoDisplay(NULL)
{

}

CEVR::~CEVR()
{
    SafeRelease(&amp;m_pEVR);
    SafeRelease(&amp;m_pVideoDisplay);
}

BOOL CEVR::HasVideo() const 
{ 
    return (m_pVideoDisplay != NULL); 
}

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

HRESULT CEVR::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pVideoDisplay == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pVideoDisplay->SetVideoPosition(NULL, prc);
    }
    else
    {

        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pVideoDisplay->SetVideoPosition(NULL, &amp;rc);
    }
}

HRESULT CEVR::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pVideoDisplay)
    {
        return m_pVideoDisplay->RepaintVideo();
    }
    else
    {
        return S_OK;
    }
}

HRESULT CEVR::DisplayModeChanged()
{
    // The EVR does not require any action in response to WM_DISPLAYCHANGE.
    return S_OK;
}


// Initialize the EVR filter. 

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

// Helper functions.

HRESULT RemoveUnconnectedRenderer(IGraphBuilder *pGraph, IBaseFilter *pRenderer, BOOL *pbRemoved)
{
    IPin *pPin = NULL;

    *pbRemoved = FALSE;

    // Look for a connected input pin on the renderer.

    HRESULT hr = FindConnectedPin(pRenderer, PINDIR_INPUT, &amp;pPin);
    SafeRelease(&amp;pPin);

    // If this function succeeds, the renderer is connected, so we don't remove it.
    // If it fails, it means the renderer is not connected to anything, so
    // we remove it.

    if (FAILED(hr))
    {
        hr = pGraph->RemoveFilter(pRenderer);
        *pbRemoved = TRUE;
    }

    return hr;
}

HRESULT IsPinConnected(IPin *pPin, BOOL *pResult)
{
    IPin *pTmp = NULL;
    HRESULT hr = pPin->ConnectedTo(&amp;pTmp);
    if (SUCCEEDED(hr))
    {
        *pResult = TRUE;
    }
    else if (hr == VFW_E_NOT_CONNECTED)
    {
        // The pin is not connected. This is not an error for our purposes.
        *pResult = FALSE;
        hr = S_OK;
    }

    SafeRelease(&amp;pTmp);
    return hr;
}

HRESULT IsPinDirection(IPin *pPin, PIN_DIRECTION dir, BOOL *pResult)
{
    PIN_DIRECTION pinDir;
    HRESULT hr = pPin->QueryDirection(&amp;pinDir);
    if (SUCCEEDED(hr))
    {
        *pResult = (pinDir == dir);
    }
    return hr;
}

HRESULT FindConnectedPin(IBaseFilter *pFilter, PIN_DIRECTION PinDir, 
    IPin **ppPin)
{
    *ppPin = NULL;

    IEnumPins *pEnum = NULL;
    IPin *pPin = NULL;

    HRESULT hr = pFilter->EnumPins(&amp;pEnum);
    if (FAILED(hr))
    {
        return hr;
    }

    BOOL bFound = FALSE;
    while (S_OK == pEnum->Next(1, &amp;pPin, NULL))
    {
        BOOL bIsConnected;
        hr = IsPinConnected(pPin, &amp;bIsConnected);
        if (SUCCEEDED(hr))
        {
            if (bIsConnected)
            {
                hr = IsPinDirection(pPin, PinDir, &amp;bFound);
            }
        }

        if (FAILED(hr))
        {
            pPin->Release();
            break;
        }
        if (bFound)
        {
            *ppPin = pPin;
            break;
        }
        pPin->Release();
    }

    pEnum->Release();

    if (!bFound)
    {
        hr = VFW_E_NOT_FOUND;
    }
    return hr;
}

HRESULT AddFilterByCLSID(IGraphBuilder *pGraph, REFGUID clsid, 
    IBaseFilter **ppF, LPCWSTR wszName)
{
    *ppF = 0;

    IBaseFilter *pFilter = NULL;
    
    HRESULT hr = CoCreateInstance(clsid, NULL, CLSCTX_INPROC_SERVER, 
        IID_PPV_ARGS(&amp;pFilter));
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pGraph->AddFilter(pFilter, wszName);
    if (FAILED(hr))
    {
        goto done;
    }

    *ppF = pFilter;
    (*ppF)->AddRef();

done:
    SafeRelease(&amp;pFilter);
    return hr;
}
```



## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md)
</dt> <dt>

[DirectShow Playback Example](directshow-playback-example.md)
</dt> </dl>

 

 



