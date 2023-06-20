---
description: Creating Kernel-Mode Filters
ms.assetid: cbc86a5d-c53a-44a0-aa81-5c41527a8f67
title: Creating Kernel-Mode Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Kernel-Mode Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Certain kernel-mode filters cannot be created through **CoCreateInstance**, and thus do not have CLSIDs. These filters include the [Tee/Sink-to-Sink Converter](tee-sink-to-sink-converter.md), the [CC Decoder](cc-decoder-filter.md) filter, and the [WST Codec](wst-codec-filter.md) filter. To create one of these filters, use the [System Device Enumerator](system-device-enumerator.md) object and search by the filter's name.

1.  Create the System Device Enumerator.
2.  Call the [**ICreateDevEnum::CreateClassEnumerator**](/windows/desktop/api/Strmif/nf-strmif-icreatedevenum-createclassenumerator) method with the CLSID of the filter category for that filter. This method creates an enumerator for the filter category. (An *enumerator* is simply an object that returns a list of other objects, using a defined COM interface.) The enumerator returns **IMoniker** pointers, which represent the filters in that category.
3.  For each moniker, call **IMoniker::BindToStorage** to get an **IPropertyBag** interface.
4.  Call **IPropertyBag::Read** to get the name of the filter.
5.  If the name matches, call **IMoniker::BindToObject** to create the filter.

The following code shows a function that performs these steps:


```C++
HRESULT CreateKernelFilter(
    const GUID &guidCategory,  // Filter category.
    LPCOLESTR szName,          // The name of the filter.
    IBaseFilter **ppFilter     // Receives a pointer to the filter.
)
{
    HRESULT hr;
    ICreateDevEnum *pDevEnum = NULL;
    IEnumMoniker *pEnum = NULL;
    if (!szName || !ppFilter) 
    {
        return E_POINTER;
    }

    // Create the system device enumerator.
    hr = CoCreateInstance(CLSID_SystemDeviceEnum, NULL, CLSCTX_INPROC,
        IID_ICreateDevEnum, (void**)&pDevEnum);
    if (FAILED(hr))
    {
        return hr;
    }

    // Create a class enumerator for the specified category.
    hr = pDevEnum->CreateClassEnumerator(guidCategory, &pEnum, 0);
    pDevEnum->Release();
    if (hr != S_OK) // S_FALSE means the category is empty.
    {
        return E_FAIL;
    }

    // Enumerate devices within this category.
    bool bFound = false;
    IMoniker *pMoniker;
    while (!bFound && (S_OK == pEnum->Next(1, &pMoniker, 0)))
    {
        IPropertyBag *pBag = NULL;
        hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, (void **)&pBag);
        if (FAILED(hr))
        {
            pMoniker->Release();
            continue; // Maybe the next one will work.
        }
        // Check the friendly name.
        VARIANT var;
        VariantInit(&var);
        hr = pBag->Read(L"FriendlyName", &var, NULL);
        if (SUCCEEDED(hr) && (lstrcmpiW(var.bstrVal, szName) == 0))
        {
            // This is the right filter.
            hr = pMoniker->BindToObject(0, 0, IID_IBaseFilter,
                (void**)ppFilter);
            bFound = true;
        }
        VariantClear(&var);
        pBag->Release();
        pMoniker->Release();
    }
    pEnum->Release();
    return (bFound ? hr : E_FAIL);
}
```



The following code example uses this function to create the CC Decoder filter and add it to the filter graph:


```C++
IBaseFilter *pCC = NULL;
hr = CreateKernelFilter(AM_KSCATEGORY_VBICODEC, 
    OLESTR("CC Decoder"), &pCC);
if (SUCCEEDED(hr))
{
    hr = pGraph->AddFilter(pCC, L"CC Decoder");
    pCC->Release();
}
```



## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> <dt>

[Using the System Device Enumerator](using-the-system-device-enumerator.md)
</dt> </dl>

 

 



