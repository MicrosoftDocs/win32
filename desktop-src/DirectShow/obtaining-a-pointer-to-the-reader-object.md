---
Description: Obtaining a Pointer to the Reader Object
ms.assetid: d1292e2f-bd0e-4961-a6fa-8cdaeb28b692
title: Obtaining a Pointer to the Reader Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining a Pointer to the Reader Object

In certain cases, for example when determining which data unit extensions are set on a given stream, you may need to access the Reader Object of the Windows Media Format SDK directly. The following function shows how to obtain the [**IWMReaderAdvanced2**](wmformat.iwmreaderadvanced2) interface on the Reader Object itself:


```C++
#include <wmsdk.h>
HRESULT GetReaderAdvanced(IGraphBuilder *pGraph, IWMReaderAdvanced2** pReaderAdvanced2) 
{
  CComPtr<IEnumFilters> pEnum;
  CComPtr<IBaseFilter> pFilter;
  ULONG cFetched;

  HRESULT hr = pGraph->EnumFilters(&amp;pEnum);
  if (FAILED(hr)) 
  {
    return hr;
  }

  while(pEnum->Next(1, &amp;pFilter, &amp;cFetched) == S_OK)
  {
    IWMHeaderInfo *pHI = NULL;
    // Only the WM ASF Reader will have interface. 
    hr = pFilter->QueryInterface(__uuidof(IWMHeaderInfo), (void**)&amp;pHI);
    if (SUCCEEDED(hr))
    {
      // We use the IWMDRMReader interface only as a way to get
      // a pointer to the Reader Object.
      CComPtr<IWMDRMReader> pWMDRMReader;
      CComQIPtr<IServiceProvider, &amp;IID_IServiceProvider> pSP;
      hr = pHI->QueryInterface(__uuidof(IServiceProvider), (void**)&amp;pSP);
      if (!pSP)
      {
        return E_NOINTERFACE;
      }
      
      hr = pSP->QueryService(IID_IWMDRMReader, IID_IWMDRMReader, (void **) &amp;pWMDRMReader);
      if (FAILED(hr))
      {
        return hr;
      }

      CComQIPtr<IWMReaderAdvanced2, &amp;IID_IWMReaderAdvanced2> pRA2(pWMDRMReader);
      if (pRA2)
      {
        *pReaderAdvanced2 = pRA2.Detach();
        return S_OK;
      }

    }
    pFilter.Release();
  }
  
  //if we get here, we didn't find the WM ASF Reader
  return E_FAIL;
}
```



## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



