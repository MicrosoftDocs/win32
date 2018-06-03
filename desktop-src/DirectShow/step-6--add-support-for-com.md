---
Description: Step 6.
ms.assetid: 53e4f5b7-c85d-4b44-9a0c-0ad05ca872cc
title: Step 6. Add Support for COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Step 6. Add Support for COM

This is step 6 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

The final step is to add support for COM.

## Reference Counting

You do not have to implement [**IUnknown::AddRef**](https://msdn.microsoft.com/windows/desktop/b4316efd-73d4-4995-b898-8025a316ba63) or [**IUnknown::Release**](https://msdn.microsoft.com/windows/desktop/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a). All of the filter and pin classes derive from [**CUnknown**](cunknown.md), which handles reference counting.

## QueryInterface

All of the filter and pin classes implement [**IUnknown::QueryInterface**](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) for any COM interfaces they inherit. For example, [**CTransformFilter**](ctransformfilter.md) inherits [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) (through [**CBaseFilter**](cbasefilter.md)). If your filter does not expose any additional interfaces, you do not have to do anything else.

To expose additional interfaces, override the [**CUnknown::NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) method. For example, suppose your filter implements a custom interface named IMyCustomInterface. To expose this interface to clients, do the following:

-   Derive your filter class from that interface.
-   Put the [**DECLARE\_IUNKNOWN**](declare-iunknown.md) macro in the public declaration section.
-   Override [**NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) to check for the IID of your interface and return a pointer to your filter.

The following code shows these steps:


```C++
CMyFilter : public CBaseFilter, public IMyCustomInterface
{
public:
    DECLARE_IUNKNOWN
    STDMETHODIMP NonDelegatingQueryInterface(REFIID iid, void **ppv);
};
STDMETHODIMP CMyFilter::NonDelegatingQueryInterface(REFIID iid, void **ppv)
{
    if (riid == IID_IMyCustomInterface) {
        return GetInterface(static_cast<IMyCustomInterface*>(this), ppv);
    }
    return CBaseFilter::NonDelegatingQueryInterface(riid,ppv);
}
```



For more information, see [How to Implement IUnknown](how-to-implement-iunknown.md).

## Object Creation

If you plan to package your filter in a DLL and make it available to other clients, you must support [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) and other related COM functions. The base class library implements most of this; you just need to provide some information about your filter. This section gives a brief overview of what to do. For details, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).

First, write a static class method that returns a new instance of your filter. You can name this method anything you like, but the signature must match the one shown in the following example:


```C++
CUnknown * WINAPI CRleFilter::CreateInstance(LPUNKNOWN pUnk, HRESULT *pHr)
{
    CRleFilter *pFilter = new CRleFilter();
    if (pFilter== NULL) 
    {
        *pHr = E_OUTOFMEMORY;
    }
    return pFilter;
}
```



Next, declare a global array of [**CFactoryTemplate**](cfactorytemplate.md) class instances, named *g\_Templates*. Each **CFactoryTemplate** class contains registry information for one filter. Several filters can reside in a single DLL; simply include additional **CFactoryTemplate** entries. You can also declare other COM objects, such as property pages.


```C++
static WCHAR g_wszName[] = L"My RLE Encoder";
CFactoryTemplate g_Templates[] = 
{
  { 
    g_wszName,
    &amp;CLSID_RLEFilter,
    CRleFilter::CreateInstance,
    NULL,
    NULL
  }
};
```



Define a global integer named *g\_cTemplates* whose value equals the length of the *g\_Templates* array:


```C++
int g_cTemplates = sizeof(g_Templates) / sizeof(g_Templates[0]);  
```



Finally, implement the DLL registration functions. The following example shows the minimal implementation for these functions:


```C++
STDAPI DllRegisterServer()
{
    return AMovieDllRegisterServer2( TRUE );
}
STDAPI DllUnregisterServer()
{
    return AMovieDllRegisterServer2( FALSE );
}
```



## Filter Registry Entries

The previous examples show how to register a filter's CLSID for COM. For many filters, this is sufficient. The client is then expected to create the filter using [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) and add it to the filter graph by calling [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter). In some cases, however, you might want to provide additional information about the filter in the registry. This information does the following:

-   Enables clients to discover the filter using the [Filter Mapper](filter-mapper.md) or the [System Device Enumerator](system-device-enumerator.md).
-   Enables the Filter Graph Manager to discover the filter during automatic graph building.

The following example registers the RLE encoder filter in the video compressor category. For details, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md). Be sure to read the section [Guidelines for Registering Filters](guidelines-for-registering-filters.md), which describes the recommended practices for filter registration.


```C++
// Declare media type information.
FOURCCMap fccMap = FCC('MRLE'); 
REGPINTYPES sudInputTypes = { &amp;MEDIATYPE_Video, &amp;GUID_NULL };
REGPINTYPES sudOutputTypes = { &amp;MEDIATYPE_Video, (GUID*)&amp;fccMap };

// Declare pin information.
REGFILTERPINS sudPinReg[] = {
    // Input pin.
    { 0, FALSE, // Rendered?
         FALSE, // Output?
         FALSE, // Zero?
         FALSE, // Many?
         0, 0, 
         1, &amp;sudInputTypes  // Media types.
    },
    // Output pin.
    { 0, FALSE, // Rendered?
         TRUE, // Output?
         FALSE, // Zero?
         FALSE, // Many?
         0, 0, 
         1, &amp;sudOutputTypes      // Media types.
    }
};
 
// Declare filter information.
REGFILTER2 rf2FilterReg = {
    1,                // Version number.
    MERIT_DO_NOT_USE, // Merit.
    2,                // Number of pins.
    sudPinReg         // Pointer to pin information.
};

STDAPI DllRegisterServer(void)
{
    HRESULT hr = AMovieDllRegisterServer2(TRUE);
    if (FAILED(hr))
    {
        return hr;
    }
    IFilterMapper2 *pFM2 = NULL;
    hr = CoCreateInstance(CLSID_FilterMapper2, NULL, CLSCTX_INPROC_SERVER,
            IID_IFilterMapper2, (void **)&amp;pFM2);
    if (SUCCEEDED(hr))
    {
        hr = pFM2->RegisterFilter(
            CLSID_RLEFilter,                // Filter CLSID. 
            g_wszName,                       // Filter name.
            NULL,                            // Device moniker. 
            &amp;CLSID_VideoCompressorCategory,  // Video compressor category.
            g_wszName,                       // Instance data.
            &amp;rf2FilterReg                    // Filter information.
            );
        pFM2->Release();
    }
    return hr;
}

STDAPI DllUnregisterServer()
{
    HRESULT hr = AMovieDllRegisterServer2(FALSE);
    if (FAILED(hr))
    {
        return hr;
    }
    IFilterMapper2 *pFM2 = NULL;
    hr = CoCreateInstance(CLSID_FilterMapper2, NULL, CLSCTX_INPROC_SERVER,
            IID_IFilterMapper2, (void **)&amp;pFM2);
    if (SUCCEEDED(hr))
    {
        hr = pFM2->UnregisterFilter(&amp;CLSID_VideoCompressorCategory, 
            g_wszName, CLSID_RLEFilter);
        pFM2->Release();
    }
    return hr;
}
```



Also, filters do not have to be packaged inside DLLs. In some cases, you might write a specialized filter that is designed only for a specific application. In that case, you can compile the filter class directly in your application, and create it with the `new` operator, as shown in the following example:


```C++
#include "MyFilter.h"  // Header file that declares the filter class.
// Compile and link MyFilter.cpp.
int main()
{
    IBaseFilter *pFilter = 0;
    {
        // Scope to hide pF.
        CMyFilter* pF = new MyFilter();
        if (!pF)
        {
            printf("Could not create MyFilter.\n");
            return 1;
        }
        pF->QueryInterface(IID_IBaseFilter, 
            reinterpret_cast<void**>(&amp;pFilter));
    }
    
    /* Now use pFilter as normal. */
    
    pFilter->Release();  // Deletes the filter.
    return 0;
}
```



## Related topics

<dl> <dt>

[Intelligent Connect](intelligent-connect.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> <dt>

[Writing Transform Filters](writing-transform-filters.md)
</dt> </dl>

 

 



