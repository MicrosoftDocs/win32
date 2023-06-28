---
description: This topic describes how to use DirectShow to play media files that are protected with Windows Media Digital Rights Management (DRM).
ms.assetid: a014942a-01e5-49d4-8a25-4604cd40f374
title: Reading DRM-Protected ASF Files in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reading DRM-Protected ASF Files in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to use DirectShow to play media files that are protected with Windows Media Digital Rights Management (DRM).

## DRM Concepts

Protecting a media file with Windows Media DRM involves two distinct steps:

-   The content provider packages the file—that is, encrypts the file and attaches licensing information to the ASF file header. The licensing information includes a URL where the client can obtain the license.
-   The client application acquires a license for the content.

Packaging happens before the file is distributed. License acquisition occurs when the user tries to play or copy the file. License acquisition may be either *silent* or *non-silent*. Silent acquisition does not require any interaction with the user. Non-silent acquisition requires the application to open a browser window and display a web page to the user. At that point, the user might need to provide some kind of information to the content provider. However, both types of license acquisition require the client to submit an HTTP request to a license server.

### DRM Versions

Several versions of Windows Media DRM exist. From the perspective of a client application, they can be grouped into two categories: DRM version 1, and DRM version 7 or later. (The second category includes DRM versions 9 and 10, as well as version 7.) The reason for categorizing DRM versions this way is that version 1 licenses are handled somewhat differently than version 7 or later licenses. In this documentation, the term *version 7 license* means version 7 or later.

It is also important to distinguish the DRM packaging from the DRM license. If the file is packaged using Windows Media Rights Manager version 7 or later, the DRM header can contain a version 1 license URL in addition to the version 7 license URL. The version 1 license URL enables older players that do not support version 7 to obtain a license for the content. However, the converse is not true, so a file with version 1 packaging cannot have a version 7 license URL.

### Application Security Level

To play DRM-protected files, the client application must be linked to a static library that is provided in binary form by Microsoft. This library, which uniquely identifies the application, is sometimes called the stub library. The stub library has an assigned security level, the value of which is determined by the license agreement that you signed when you obtained the stub library.

The content provider sets a minimum security level needed to acquire the license. If the security level of your stub library is less than the minimum security level required by the license server, the application cannot obtain the license.

### Individualization

To increase security, an application may update the DRM components on the client's computer. This update, called individualization, differentiates the user's copy of the application from all other copies of the same application. The DRM header of a protected file may specify may specify a minimum individualization level. (For more information, see the documentation for WMRMHeader.IndividualizedVersion in the Windows Media Rights Manager SDK.)

The Microsoft Individualization Service handles information from the user. So before your application individualizes, you must display the Microsoft Privacy Statement, or provide a link to it (see [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement)).

## Provide the Software Certificate

To enable the application to use the DRM license, the application must provide a software certificate or *key* to the Filter Graph Manager. This key is contained in a static library that is individualized for the application. For information about obtaining the individualized library, see [Obtaining the Required DRM Library](../wmformat/obtaining-the-required-drm-library.md) in the Windows Media Format SDK documentation.

To provide the software key, perform the following steps:

1.  Link to the static library.
2.  Implement the **IServiceProvider** interface.
3.  Query the Filter Graph Manager for the [**IObjectWithSite**](/windows/win32/api/ocidl/nn-ocidl-iobjectwithsite) interface.
4.  Call [**IObjectWithSite::SetSite**](/windows/win32/api/ocidl/nf-ocidl-iobjectwithsite-setsite) with a pointer to your implementation of **IServiceProvider**.
5.  The Filter Graph Manager will call **IServiceProvider::QueryService**, specifying **IID\_IWMReader** for the service identifier.
6.  In your implementation of **QueryService**, call [**WMCreateCertificate**](/previous-versions/windows/desktop/legacy/dd757745(v=vs.85)) to create the software key.

The following code shows how to implement the **QueryService** method:


```C++
STDMETHODIMP Player::QueryService(REFIID siid, REFIID riid, void **ppv)
{
    if (ppv == NULL ) 
    { 
        return E_POINTER; 
    }

    if (siid == __uuidof(IWMReader) && riid == __uuidof(IUnknown))
    {
        IUnknown *punkCert;

        HRESULT hr = WMCreateCertificate(&punkCert);

        if (SUCCEEDED(hr))
        {
            *ppv = (void *) punkCert;
        }

        return hr;
    }
    return E_NOINTERFACE;
}
```



The following code shows how to call [**SetSite**](/windows/win32/api/ocidl/nf-ocidl-iobjectwithsite-setsite) on the Filter Graph Manager:


```C++
HRESULT Player::CreateFilterGraph()
{
    CComPtr<IObjectWithSite> pSite;

    HRESULT hr = pGraph.CoCreateInstance(CLSID_FilterGraph);

    if (FAILED(hr))
    {
        goto done;
    }

    // Register the application as a site (service).
    hr = pGraph->QueryInterface(&pSite);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSite->SetSite(this);


done:
    return hr;
}
```





## Building the Playback Graph

To play a DRM-protected ASF file, perform the following steps:

1.  Create the [Filter Graph Manager](filter-graph-manager.md) and use the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) interface to register for graph events.
2.  Call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create a new instance of the [WM ASF Reader](wm-asf-reader-filter.md) filter.
3.  Call [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter) to add the filter to the filter graph.
4.  Query the filter for the [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter) interface.
5.  Call [**IFileSourceFilter::Load**](/windows/desktop/api/Strmif/nf-strmif-ifilesourcefilter-load) with the URL of the file.
6.  Handle [**EC\_WMT\_EVENT**](ec-wmt-event.md) events.
7.  On the first [**EC\_WMT\_EVENT**](ec-wmt-event.md) event, query the [WM ASF Reader](wm-asf-reader-filter.md) filter for the **IServiceProvider** interface.
8.  Call **IServiceProvider::QueryService** to get a pointer to the [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) interface.
9.  Call [**IGraphBuilder::Render**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-render) to render the output pins of the [WM ASF Reader](wm-asf-reader-filter.md) filter.

> [!Note]  
> When opening a DRM-protected file, do not call [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) to create the filter graph. The WM ASF Reader filter cannot connect to any other filters until the DRM license is acquired. This step requires the application to use the [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) interface, which must be obtained from the filter, as described in steps 7–8. Therefore, you must create the filter and add it to the graph

 

> [!Note]  
> It is important to register for graph events (step 1) before adding the [WM ASF Reader](wm-asf-reader-filter.md) filter to the graph (step 3), because the application must handle the [**EC\_WMT\_EVENT**](ec-wmt-event.md) events. The events are sent when [**Load**](/windows/desktop/api/Strmif/nf-strmif-ifilesourcefilter-load) is called (step 5).

 

The following code shows how to build the graph:


```C++
HRESULT Player::LoadMediaFile(PCWSTR pwszFile)
{


    BOOL bIsWindowsMediaFile = IsWindowsMediaFile(pwszFile);

    HRESULT hr = S_OK;

    // If this is the first time opening the file, create the
    // filter graph and add the WM ASF Reader filter.

    if (m_DRM.State() == DRM_INITIAL)
    {
        hr = CreateFilterGraph();
        if (FAILED(hr))
        {
            goto done;
        }

        // Use special handling for Windows Media files.
        if (bIsWindowsMediaFile)
        {
            // Add the ASF Reader filter to the graph.
            hr = m_pReader.CoCreateInstance(CLSID_WMAsfReader);
            if (FAILED(hr))
            {
                goto done;
            }

            hr = pGraph->AddFilter(m_pReader, NULL);
            if (FAILED(hr))
            {
                goto done;
            }

            hr = m_pReader->QueryInterface(&m_pFileSource);
            if (FAILED(hr))
            {
                goto done;
            }
        }
    }

    if (bIsWindowsMediaFile)
    {
            hr = m_pFileSource->Load(pwszFile, NULL);
```




| C++ | 
|-----|
| <pre><code>            if (FAILED(hr))            {                goto done;            }            hr = RenderOutputPins(pGraph, m_pReader);    }    else    {        // Not a Windows Media file, so just render the standard way.        hr = pGraph-&gt;RenderFile(pwszFile, NULL);    }done:    return hr;}</code></pre> | 




In the previous code, the `RenderOutputPins` function enumerates the output pins on the [WM ASF Reader](wm-asf-reader-filter.md) filter and calls [**IGraphBuilder::Render**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-render) for each pin.


```C++
HRESULT RenderOutputPins(IGraphBuilder *pGraph, IBaseFilter *pFilter)
{
    CComPtr<IEnumPins>  pEnumPin = NULL;
    CComPtr<IPin>       pConnectedPin;
    CComPtr<IPin>       pPin;

    // Enumerate all pins on the filter
    HRESULT hr = pFilter->EnumPins(&pEnumPin);
    if (FAILED(hr))
    {
        goto done;
    }

    // Step through every pin, looking for the output pins.
    while (S_OK == (hr = pEnumPin->Next(1, &pPin, NULL)))
    {
        // Skip connected pins.
        hr = pPin->ConnectedTo(&pConnectedPin);
        if (hr == VFW_E_NOT_CONNECTED)
        {
            PIN_DIRECTION PinDirection;
            hr = pPin->QueryDirection(&PinDirection);

            if ((S_OK == hr) && (PinDirection == PINDIR_OUTPUT))
            {
                hr = pGraph->Render(pPin);
            }
        }

        pConnectedPin.Release();
        pPin.Release();

        // If there was an error, stop enumerating.
        if (FAILED(hr))
        {
            break;
        }
    }

done:
    return hr;
}
```



The following code shows how to get a pointer to the [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) interface from the [WM ASF Reader](wm-asf-reader-filter.md):


```C++
HRESULT DrmManager::Initialize(IBaseFilter *pFilter)
{


    CComPtr<IServiceProvider> pService;
    CComPtr<IWMDRMReader> pDrmReader;

    HRESULT hr = pFilter->QueryInterface(&pService);
    if (SUCCEEDED(hr))
    {
        hr = pService->QueryService(
            __uuidof(IWMDRMReader), IID_PPV_ARGS(&m_pDrmReader));
    }
    return hr;
}
```





## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 
