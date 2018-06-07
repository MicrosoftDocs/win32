---
title: Multichannel Audio Playback in DirectShow
description: Multichannel Audio Playback in DirectShow
ms.assetid: 5123854a-0f1f-40f4-bf57-47622b91103f
keywords:
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,multichannel audio playback
- Windows Media Format SDK,audio playback
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),multichannel audio playback
- ASF (Advanced Systems Format),multichannel audio playback
- Advanced Systems Format (ASF),audio playback
- ASF (Advanced Systems Format),audio playback
- DirectShow,multichannel audio playback
- DirectShow,audio playback
- multichannel audio,playback
- audio playback
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Multichannel Audio Playback in DirectShow

To play back a multichannel Windows Media Audio file in DirectShow, you must set the "\_HIRESOUTPUT" property directly on the decoder after it has been connected to the WM ASF Reader. No configuration of the Reader Object is necessary. However, to work with the DMO directly, you need wmcodecconst.h from the [Sample Code for Using the Windows Media Audio and Video Codec Interfaces](http://go.microsoft.com/fwlink/p/?linkid=16185) download package.

**Note** This configuration procedure is supported only for files that are not protected by Digital Rights Management.

The basic steps to enable multichannel output are as follows:

1.  Call RenderFile to create the filter graph.
2.  Obtain a pointer to the DMO Wrapper filter
3.  Disconnect the DMO Wrapper from the Audio Renderer
4.  Set the "\_HIRESOUTPUT" property on the decoder.
5.  Reconnect the DMO Wrapper and the Audio Renderer.
6.  Run the graph.

The following code snippets demonstrate these steps. (All error checking has been omitted for the sake of simplicity. You should add proper error handling routines if you use this code in an application.)


```C++
    ...
    //ENABLE MULTICHANNEL OUTPUT
    //Render the file
    hr = m_pGraphBuilder->RenderFile(wFileName, NULL);

    // Get pointers to the two DMO Wrapper interfaces we need.
    // (Function bodies provided at the end of this snippet.)
    hr = GetDMOWrapper(pGB, &amp;m_pDMOBaseFilter, &amp;m_pWrapper); 

    //Disconnect the DMO Wrapper from the Audio Renderer
    CComPtr<IPin> pDMOOut;
    CComPtr<IPin> pRendererIn;
    hr = GetPin(m_pDMOBaseFilter, PINDIR_OUTPUT, &amp;pDMOOut);
    hr = pDMOOut->ConnectedTo(&amp;pRendererIn);
    hr = pDMOOut->Disconnect();
    hr = pRendererIn->Disconnect();

    //Set the property on the DMO
    VARIANT varg;
    ::VariantInit(&amp;varg);
    varg.vt    = VT_BOOL;
    varg.boolVal = TRUE;
    CComQIPtr<IMediaObject, &amp;IID_IMediaObject> pMediaObject(m_pWrapper);
    CComQIPtr<IPropertyBag, &amp;IID_IPropertyBag> pPropertyBag(pMediaObject);
    hr = pPropertyBag->Write(g_wszWMACHiResOutput, &amp;varg);

    // Reconnect the DMO Wrapper and the Audio Renderer
    hr = pGB->Connect(pDMOOut, pRendererIn);
    //END MULTICHANNEL (now the graph can be run)
...

```



The GetDMOWrapper and GetPin functions from the previous code snippet are implemented as follows:


```C++
// In this example, the IBaseFilter and IDMOWrapperFilter interfaces are
// declared  at global scope
HRESULT GetDMOWrapper (IFilterGraph *pGraph, IBaseFilter** m_pDMOBaseFilter, IDMOWrapperFilter** m_pWrapper) 
{
    CComPtr<IEnumFilters> pEnum;
    CComPtr<IBaseFilter> pFilter;
    ULONG cFetched;

    HRESULT hr = pGraph->EnumFilters(&amp;pEnum);
    if (FAILED(hr)) return hr;

    while(pEnum->Next(1, &amp;pFilter, &amp;cFetched) == S_OK)
    {
        // If we find the IDMOWrapperFilter interface, that means we 
        // have the DMO Wrapper filter. Store both interfaces for future use.
        CComPtr<IDMOWrapperFilter> pWrapper;
        hr = pFilter->QueryInterface(IID_IDMOWrapperFilter, (void**) &amp;pWrapper);
        if (SUCCEEDED(hr))
        {
            *m_pWrapper = pWrapper.Detach();
            *m_pDMOBaseFilter = pFilter.Detach();
            return S_OK;
        }

        pFilter.Release();
    }

    return E_FAIL;
}

HRESULT GetPin(IBaseFilter *pFilter, PIN_DIRECTION PinDir, IPin** ppPin)
{
    CComPtr<IEnumPins>  pEnum;
    CComPtr<IPin>       pPin;

         HRESULT hr = pFilter->EnumPins(&amp;pEnum);
    if (FAILED(hr))
    {
        return hr;
    }
    while(pEnum->Next(1, &amp;pPin, 0) == S_OK)
    {
        PIN_DIRECTION PinDirThis;
        pPin->QueryDirection(&amp;PinDirThis);
        if (PinDir == PinDirThis)
        {
            *ppPin = pPin.Detach();
            return S_OK;
        }
        pPin.Release();
    }
    
    return E_FAIL;
}
```



 

 




