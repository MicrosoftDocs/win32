---
description: Using DMOs in DirectShow
ms.assetid: 47d75b9c-8b0d-4235-8ac1-02ae1502c0e7
title: Using DMOs in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using DMOs in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applications based on DirectShow can use DMOs in a filter graph, through the [DMO Wrapper](dmo-wrapper-filter.md) filter. This filter aggregates a DMO and handles all the details of using the DMO, such as passing data to and from the DMO, allocating [**IMediaBuffer**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediabuffer) objects, and so forth.

Because the DMO is aggregated by the filter, the application can query the filter for any COM interfaces that the DMO exposes. However, the application should let the filter handle all streaming operations on the DMO. For example, do not set media types, process any buffers, flush the DMO, lock the DMO, enable or disable quality control, or set video optimizations.

If you know the class identifier (CLSID) of a specific DMO that you want to use, you can initialize the DMO Wrapper filter with that DMO, as follows:

1.  Call **CoCreateInstance** to create the DMO Wrapper filter.
2.  Query the DMO Wrapper filter for the [**IDMOWrapperFilter**](/previous-versions/windows/desktop/api/Dmodshow/nn-dmodshow-idmowrapperfilter) interface.
3.  Call the [**IDMOWrapperFilter::Init**](/previous-versions/windows/desktop/api/Dmodshow/nf-dmodshow-idmowrapperfilter-init) method. Specify the CLSID of the DMO and the GUID of the DMO's category. For a list of DMO categories, see [DMO GUIDs](dmo-guids.md).

The following code shows these steps:


```C++
// Create the DMO Wrapper filter.
IBaseFilter *pFilter;
HRESULT hr = CoCreateInstance(CLSID_DMOWrapperFilter, NULL, 
    CLSCTX_INPROC_SERVER, IID_IBaseFilter, 
    reinterpret_cast<void**>(&pFilter));

if (SUCCEEDED(hr)) 
{
    // Query for IDMOWrapperFilter.
    IDMOWrapperFilter *pDmoWrapper;
    hr = pFilter->QueryInterface(IID_IDMOWrapperFilter, 
        reinterpret_cast<void**>(&pDmoWrapper));

    if (SUCCEEDED(hr)) 
    {     
        // Initialize the filter.
        hr = pDmoWrapper->Init(CLSID_MyDMO, DMOCATEGORY_VIDEO_EFFECT); 
        pDmoWrapper->Release();

        if (SUCCEEDED(hr)) 
        {
            // Add the filter to the graph.
            hr = pGraph->AddFilter(pFilter, L"My DMO");
        }
    }
    pFilter->Release();
}
```



The [**DMOEnum**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoenum) function enumerates DMOs in the registry. This function uses a different set of category GUIDs from the ones used for DirectShow filters.

**Using the System Device Enumerator with DMOs**

Instead of creating a DMO directly, you can use the [System Device Enumerator](system-device-enumerator.md), which can enumerate any DMO category that is supported by the **DMOEnum** method. The System Device Enumerator also includes DMOs when it enumerates certain DirectShow filter categories. The following table shows the mapping between DMO categories and DirectShow categories.



| Label | Value |
|-----------------------------|--------------------------------|
| DMO Category                | DirectShow Equivalent          |
| DMOCATEGORY\_AUDIO\_ENCODER | CLSID\_AudioCompressorCategory |
| DMOCATEGORY\_AUDIO\_DECODER | CLSID\_LegacyAmFilterCategory  |
| DMOCATEGORY\_VIDEO\_ENCODER | CLSID\_VideoCompressorCategory |
| DMOCATEGORY\_VIDEO\_DECODER | CLSID\_LegacyAmFilterCategory  |



 

The System Device Enumerator returns a list of moniker objects. If the moniker represents a DMO, the **IMoniker::BindToObject** method automatically creates the DMO Wrapper filter and initializes it with that DMO. Thus, the fact that a DMO is involved is transparent to the application. For more information on using the System Device Enumerator, see [Using the System Device Enumerator](using-the-system-device-enumerator.md).

**Limitations**

There are some limitations when using DMOs in DirectShow:

-   The DMO Wrapper filter does not support DMOs with zero inputs, multiple inputs, or zero outputs.
-   All pin connections on the DMO Wrapper Filter use the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface.
-   DirectShow Editing Services does not support DMO-based effects or transitions.

## Related topics

<dl> <dt>

[Using DMOs](using-dmos.md)
</dt> </dl>

 

 



