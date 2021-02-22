---
description: Microsoft Media Foundation uses a mix of COM constructs, but is not a fully COM-based API.
ms.assetid: d58ca46f-8f3a-4a12-b948-1ea7ab568788
title: Media Foundation and COM
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation and COM

Microsoft Media Foundation uses a mix of COM constructs, but is not a fully COM-based API. This topic describes the interaction between COM and Media Foundation. It also defines some best practices for developing Media Foundation plug-in components. Following these practices can help you to avoid some common but subtle programming errors.

-   [Best Practices for Applications](#best-practices-for-applications)
-   [Best Practices for Media Foundation Components](#best-practices-for-media-foundation-components)
-   [Summary](#summary)
-   [Related topics](#related-topics)

## Best Practices for Applications

In Media Foundation, asynchronous processing and callbacks are handled by [work queues](work-queues.md). Work queues always have multithreaded apartment (MTA) threads, so an application will have a simpler implementation if it runs on an MTA thread as well. Therefore, it is recommended to call [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) with the **COINIT\_MULTITHREADED** flag.

Media Foundation does not marshal single-threaded apartment (STA) objects to work queue threads. Nor does it ensure that STA invariants are maintained. Therefore, an STA application must be careful to not pass STA objects or proxies to Media Foundation APIs. Objects that are STA-only are not supported in Media Foundation.

If you have an STA proxy to an MTA or free-threaded object, the object can be marshaled to an MTA proxy by using a work-queue callback. The [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function can return either a raw pointer or an STA proxy, depending on the object model defined in the registry for that CLSID. If an STA proxy is returned, you must not pass the pointer to a Media Foundation API.

For example, suppose that you want to pass an **IPropertyStore** pointer to the [**IMFSourceResolver::BeginCreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-begincreateobjectfromurl) method. You might call **PSCreateMemoryPropertyStore** to create the **IPropertyStore** pointer. If you are calling from an STA, you must marshal the pointer before passing it to **BeginCreateObjectFromURL**.

The following code shows how to marshal an STA proxy to a Media Foundation API.


```C++
class CCreateSourceMarshalCallback
    : public IMFAsyncCallback
{
public:
    CCreateSourceMarshalCallback(
        LPCWSTR szURL, 
        IMFSourceResolver* pResolver, 
        IPropertyStore* pSourceProps, 
        IMFAsyncCallback* pCompletionCallback, 
        HRESULT& hr
        )
        : m_szURL(szURL), 
          m_pResolver(pResolver), 
          m_pCompletionCallback(pCompletionCallback),
          m_pGIT(NULL),
          m_cRef(1)
    {
        hr = CoCreateInstance(CLSID_StdGlobalInterfaceTable, NULL, 
            CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&m_pGIT));

        if(SUCCEEDED(hr))
        {
            hr = m_pGIT->RegisterInterfaceInGlobal(
                pSourceProps, IID_IPropertyStore, &m_dwInterfaceCookie);
        }
    }
    ~CCreateSourceMarshalCallback()
    {
        SafeRelease(&m_pResolver);
        SafeRelease(&m_pCompletionCallback);
        SafeRelease(&m_pGIT);
    }


    STDMETHOD_(ULONG, AddRef)()
    {
        return InterlockedIncrement(&m_cRef);
    }

    STDMETHOD_(ULONG, Release)()
    {
        LONG cRef = InterlockedDecrement(&m_cRef);
        if (0 == cRef)
        {
            delete this;
        }
        return cRef;
    }

    STDMETHOD(QueryInterface)(REFIID riid, LPVOID* ppvObject)
    {
        static const QITAB qit[] = 
        {
            QITABENT(CCreateSourceMarshalCallback, IMFAsyncCallback),
            { 0 }
        };
        return QISearch(this, qit, riid, ppvObject);

    }

    STDMETHOD(GetParameters)(DWORD* pdwFlags, DWORD* pdwQueue)
    {
        return E_NOTIMPL;
    }

    STDMETHOD(Invoke)(IMFAsyncResult* pResult)
    {
        IPropertyStore *pSourceProps = NULL;

        HRESULT hr = m_pGIT->GetInterfaceFromGlobal(
            m_dwInterfaceCookie, 
            IID_PPV_ARGS(&pSourceProps)
            );

        if(SUCCEEDED(hr))
        {
            hr = m_pResolver->BeginCreateObjectFromURL(
                m_szURL, MF_RESOLUTION_MEDIASOURCE, pSourceProps, NULL, 
                m_pCompletionCallback, NULL);
        }

        SafeRelease(&pSourceProps);
        return hr;
    }

private:
    LPCWSTR m_szURL;
    IMFSourceResolver *m_pResolver;
    IMFAsyncCallback *m_pCompletionCallback;
    IGlobalInterfaceTable *m_pGIT;
    DWORD m_dwInterfaceCookie;
    LONG m_cRef;
};
```



For more information about the global interface table, see [**IGlobalInterfaceTable**](/windows/win32/api/objidl/nn-objidl-iglobalinterfacetable).

If you are using Media Foundation in-process, objects returned from Media Foundation methods and functions are direct pointers to the object. For cross-process Media Foundation, these objects may be MTA proxies, and should be marshaled into an STA thread if needed there. Similarly, objects obtained inside a callback — for example, a topology from the [MESessionTopologyStatus](mesessiontopologystatus.md) event — are direct pointers when Media Foundation is used in-process, but are MTA proxies when Media Foundation is used cross-process.

> [!Note]  
> The most common scenario for using Media Foundation cross-process is with the [Protected Media Path](protected-media-path.md) (PMP). However, these remarks apply to any situation when Media Foundation APIs are used through RPC.

 

All implementations of [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) should be MTA-compatible. These objects do not need to be COM objects at all. But if they are, they cannot run in the STA. The [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) function will be invoked on an MTA workqueue thread, and the provided [**IMFAsyncResult**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasyncresult) object will be either a direct object pointer or an MTA proxy.

## Best Practices for Media Foundation Components

There are two categories of Media Foundation objects that need to be concerned about COM. Some components, such as transforms or byte stream handlers, are full COM objects created by CLSID. These objects must follow the rules for COM apartments, for both in-process and cross-process Media Foundation. Other Media Foundation components are not full COM objects, but do need COM proxies for cross-process playback. Objects in this category include media sources and activation object. These objects can ignore apartment issues if they will be used only for in-process Media Foundation.

Although not all Media Foundation objects are COM objects, all Media Foundation interfaces derive from [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown). Therefore, all Media Foundation objects must implement **IUnknown** according to COM specifications, including the rules for reference counting and [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). All reference counted objects should also ensure that [**DllCanUnloadNow**](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow) will not allow the module to be unloaded while the objects still persist.

Media Foundation components cannot be STA objects. Many Media Foundation objects do not need to be COM objects at all. But if they are, they cannot run in the STA. All Media Foundation components must be thread-safe. Some Media Foundation objects must be free-threaded or apartment-neutral as well. The following table specifies the requirements for custom interface implementations:



| Interface                                                          | Category            | Required apartment       |
|--------------------------------------------------------------------|---------------------|--------------------------|
| [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate)                                 | Cross-process proxy | Free-threaded or neutral |
| [**IMFByteStreamHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler)               | COM object          | MTA                      |
| [**IMFContentProtectionManager**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager) | Cross-process proxy | Free-threaded or neutral |
| [**IMFQualityManager**](/windows/desktop/api/mfidl/nn-mfidl-imfqualitymanager)                     | COM object          | Free-threaded or neutral |
| [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)                           | Cross-process proxy | Free-threaded or neutral |
| [**IMFSchemeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfschemehandler)                       | COM object          | MTA                      |
| [**IMFTopoLoader**](/windows/desktop/api/mfidl/nn-mfidl-imftopoloader)                             | COM object          | Free-threaded or neutral |
| [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)                               | COM object          | MTA                      |



 

There may be additional requirements depending upon the implementation. For example, if a media sink implements another interface that enables the application to make direct function calls to the sink, the sink would need to be free-threaded or neutral, so that it could handle direct cross-process calls. Any object may be free-threaded; this table specifies the minimum requirements.

The recommended way to implement free-threaded or neutral objects is by aggregating the free-threaded marshaler. For more details, see the MSDN documentation on [**CoCreateFreeThreadedMarshaler**](/windows/win32/api/combaseapi/nf-combaseapi-cocreatefreethreadedmarshaler). In accordance with the requirement not to pass STA objects or proxies to Media Foundation APIs, free-threaded objects do not need to worry about marshaling STA input pointers in free-threaded components.

Components that use the long-function work queue (**MFASYNC\_CALLBACK\_QUEUE\_LONG\_FUNCTION**) must exercise more care. Threads in the long function workqueue create their own STA. Components that use the long function workqueue for callbacks should avoid creating COM objects on these threads, and need to be careful to marshal proxies to the STA as necessary.

## Summary

Applications will have an easier time if they interact with Media Foundation from an MTA thread, but it is possible with some care to use Media Foundation from an STA thread. Media Foundation does not handle STA components, and applications should be careful not to pass STA objects to Media Foundation APIs. Some objects have additional requirements, especially objects that run in a cross-process situation. Following these guidelines will help avoid COM errors, deadlocks, and unexpected delays in media processing.

## Related topics

<dl> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> </dl>

 

 
