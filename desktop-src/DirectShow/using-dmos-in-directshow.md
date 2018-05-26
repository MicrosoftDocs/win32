---
Description: Using DMOs in DirectShow
ms.assetid: 47d75b9c-8b0d-4235-8ac1-02ae1502c0e7
title: Using DMOs in DirectShow
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using DMOs in DirectShow

Applications based on DirectShow can use DMOs in a filter graph, through the [DMO Wrapper](dmo-wrapper-filter.md) filter. This filter aggregates a DMO and handles all the details of using the DMO, such as passing data to and from the DMO, allocating [**IMediaBuffer**](/windows/win32/Mediaobj/nn-mediaobj-imediabuffer?branch=master) objects, and so forth.

Because the DMO is aggregated by the filter, the application can query the filter for any COM interfaces that the DMO exposes. However, the application should let the filter handle all streaming operations on the DMO. For example, do not set media types, process any buffers, flush the DMO, lock the DMO, enable or disable quality control, or set video optimizations.

If you know the class identifier (CLSID) of a specific DMO that you want to use, you can initialize the DMO Wrapper filter with that DMO, as follows:

1.  Call **CoCreateInstance** to create the DMO Wrapper filter.
2.  Query the DMO Wrapper filter for the [**IDMOWrapperFilter**](/windows/win32/Dmodshow/nn-dmodshow-idmowrapperfilter?branch=master) interface.
3.  Call the [**IDMOWrapperFilter::Init**](/windows/win32/Dmodshow/nf-dmodshow-idmowrapperfilter-init?branch=master) method. Specify the CLSID of the DMO and the GUID of the DMO's category. For a list of DMO categories, see [DMO GUIDs](dmo-guids.md).

The following code shows these steps:


```C++
// Create the DMO Wrapper filter.
IBaseFilter *pFilter;
HRESULT hr = CoCreateInstance(CLSID_DMOWrapperFilter, NULL, 
    CLSCTX_INPROC_SERVER, IID_IBaseFilter, 
    reinterpret_cast<void**>(&amp;pFilter));

if (SUCCEEDED(hr)) 
{
    // Query for IDMOWrapperFilter.
    IDMOWrapperFilter *pDmoWrapper;
    hr = pFilter->QueryInterface(IID_IDMOWrapperFilter, 
        reinterpret_cast<void**>(&amp;pDmoWrapper));

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



The [**DMOEnum**](/windows/win32/Dmoreg/nf-dmoreg-dmoenum?branch=master) function enumerates DMOs in the registry. This function uses a different set of category GUIDs from the ones used for DirectShow filters.

**Using the System Device Enumerator with DMOs**

Instead of creating a DMO directly, you can use the [System Device Enumerator](system-device-enumerator.md), which can enumerate any DMO category that is supported by the **DMOEnum** method. The System Device Enumerator also includes DMOs when it enumerates certain DirectShow filter categories. The following table shows the mapping between DMO categories and DirectShow categories.



|                             |                                |
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
-   All pin connections on the DMO Wrapper Filter use the [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master) interface.
-   DirectShow Editing Services does not support DMO-based effects or transitions.

## Related topics

<dl> <dt>

[Using DMOs](using-dmos.md)
</dt> </dl>

 

 



