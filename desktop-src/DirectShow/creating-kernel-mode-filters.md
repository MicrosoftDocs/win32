---
Description: Creating Kernel-Mode Filters
ms.assetid: cbc86a5d-c53a-44a0-aa81-5c41527a8f67
title: Creating Kernel-Mode Filters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Kernel-Mode Filters

Certain kernel-mode filters cannot be created through **CoCreateInstance**, and thus do not have CLSIDs. These filters include the [Tee/Sink-to-Sink Converter](tee-sink-to-sink-converter.md), the [CC Decoder](cc-decoder-filter.md) filter, and the [WST Codec](wst-codec-filter.md) filter. To create one of these filters, use the [System Device Enumerator](system-device-enumerator.md) object and search by the filter's name.

1.  Create the System Device Enumerator.
2.  Call the [**ICreateDevEnum::CreateClassEnumerator**](/windows/win32/Strmif/nf-strmif-icreatedevenum-createclassenumerator?branch=master) method with the CLSID of the filter category for that filter. This method creates an enumerator for the filter category. (An *enumerator* is simply an object that returns a list of other objects, using a defined COM interface.) The enumerator returns **IMoniker** pointers, which represent the filters in that category.
3.  For each moniker, call **IMoniker::BindToStorage** to get an **IPropertyBag** interface.
4.  Call **IPropertyBag::Read** to get the name of the filter.
5.  If the name matches, call **IMoniker::BindToObject** to create the filter.

The following code shows a function that performs these steps:


```C++
HRESULT CreateKernelFilter(
    const GUID &amp;guidCategory,  // Filter category.
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
        IID_ICreateDevEnum, (void**)&amp;pDevEnum);
    if (FAILED(hr))
    {
        return hr;
    }

    // Create a class enumerator for the specified category.
    hr = pDevEnum->CreateClassEnumerator(guidCategory, &amp;pEnum, 0);
    pDevEnum->Release();
    if (hr != S_OK) // S_FALSE means the category is empty.
    {
        return E_FAIL;
    }

    // Enumerate devices within this category.
    bool bFound = false;
    IMoniker *pMoniker;
    while (!bFound &amp;&amp; (S_OK == pEnum->Next(1, &amp;pMoniker, 0)))
    {
        IPropertyBag *pBag = NULL;
        hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, (void **)&amp;pBag);
        if (FAILED(hr))
        {
            pMoniker->Release();
            continue; // Maybe the next one will work.
        }
        // Check the friendly name.
        VARIANT var;
        VariantInit(&amp;var);
        hr = pBag->Read(L"FriendlyName", &amp;var, NULL);
        if (SUCCEEDED(hr) &amp;&amp; (lstrcmpiW(var.bstrVal, szName) == 0))
        {
            // This is the right filter.
            hr = pMoniker->BindToObject(0, 0, IID_IBaseFilter,
                (void**)ppFilter);
            bFound = true;
        }
        VariantClear(&amp;var);
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
    OLESTR("CC Decoder"), &amp;pCC);
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

 

 



