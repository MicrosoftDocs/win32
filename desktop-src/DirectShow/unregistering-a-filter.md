---
Description: Unregistering a Filter
ms.assetid: '5459d172-7dfe-4786-bcf2-031e441e30a2'
title: Unregistering a Filter
---

# Unregistering a Filter

To unregister a filter, implement the **DllUnregisterServer** function. Within this function, call the DirectShow [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) function with a value of **FALSE**. If you called **IFilterMapper2::RegisterFilter** when you registered the filter, call the [**IFilterMapper2::UnregisterFilter**](ifiltermapper2-unregisterfilter.md) method here.

The following example shows how to unregister a filter:


```C++
STDAPI DllUnregisterServer()
{
    HRESULT hr;
    IFilterMapper2 *pFM2 = NULL;

    hr = AMovieDllRegisterServer2(FALSE);
    if (FAILED(hr))
        return hr;
 
    hr = CoCreateInstance(CLSID_FilterMapper2, NULL, CLSCTX_INPROC_SERVER,
            IID_IFilterMapper2, (void **)&amp;pFM2);

    if (FAILED(hr))
        return hr;

    hr = pFM2->UnregisterFilter(&amp;CLSID_VideoCompressorCategory, 
            g_wszName, CLSID_SomeFilter);

    pFM2->Release();
    return hr;
}
```



 

 



