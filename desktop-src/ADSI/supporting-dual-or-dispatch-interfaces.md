---
title: Supporting Dual or Dispatch Interfaces
description: Like the dispatch interface, all dual interfaces must inherit from IDispatch, which delegates all of its IDispatch functions (GetIDsOfNames, Invoke, GetTypeInfo, GetTypeInfoCount) back to the IDispatch of the aggregator (ADSI).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: abd0fcfc-f45c-4022-af95-60615be0adcc
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Supporting dual or dispatch interfaces ADSI
- extensions ADSI , dual or dispatch interfaces
- ADSI ADSI , example code C/C++ , delegating IDispatch methods to the aggregator
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supporting Dual or Dispatch Interfaces

Like the dispatch interface, all dual interfaces must inherit from [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5), which delegates all of its **IDispatch** functions ([**GetIDsOfNames**](https://msdn.microsoft.com/windows/desktop/6f6cf233-3481-436e-8d6a-51f93bf91619), [**Invoke**](https://msdn.microsoft.com/windows/desktop/964ade8e-9d8a-4d32-bd47-aa678912a54d), [**GetTypeInfo**](https://msdn.microsoft.com/windows/desktop/cc1ec9aa-6c40-4e70-819c-a7c6dd6b8c99), [**GetTypeInfoCount**](https://msdn.microsoft.com/windows/desktop/da876d53-cb8a-465c-a43e-c0eb272e2a12)) back to the **IDispatch** of the aggregator (ADSI). In order to delegate, an extension object should query for the **IDispatch** of the aggregator, call the appropriate aggregator method, and release the pointer after use.

If the extension can be a standalone component, verify that it is aggregated. If so, reroute the dispatch functions to the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) of the aggregator, otherwise you can call your internal implementation of **IDispatch**, or you can call your implementation of [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension).

The following code example shows how to reroute the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) call to the **IDispatch** of the aggregator. This code example assumes that the **m\_pOuterUnknown** member variable has been initialized to the **IUnknown** pointer of the aggregator.


```C++
/////////////////////////////////////////////////// 
// Delegating IDispatch Methods to the aggregator
///////////////////////////////////////////////////
STDMETHODIMP MyExtension::GetTypeInfoCount(UINT* pctinfo)
{
    IDispatch *pDisp = NULL;
    HRESULT    hr = S_OK;
    hr = m_pOuterUnknown->QueryInterface( IID_IDispatch, (void**) &amp;pDisp );
    if ( SUCCEEDED(hr) )
    {
        hr = pDisp->GetTypeInfoCount( pctinfo );
        pDisp->Release();
    }
    return hr;
}
 
 
STDMETHODIMP MyExtension::GetTypeInfo(UINT itinfo, LCID lcid, ITypeInfo** pptinfo)
{
    IDispatch *pDisp = NULL;
    HRESULT    hr = S_OK;
    hr = m_pOuterUnknown->QueryInterface( IID_IDispatch, (void**) &amp;pDisp );
    if ( SUCCEEDED(hr) )
    {
        hr = pDisp->GetTypeInfo( itinfo, lcid, pptinfo );
        pDisp->Release();
    }
    
    return hr;
}
 
STDMETHODIMP MyExtension::GetIDsOfNames(REFIID riid, LPOLESTR* rgszNames, UINT cNames, LCID lcid, DISPID* rgdispid)
{
    IDispatch *pDisp = NULL;
    HRESULT    hr = S_OK;
    hr = m_pOuterUnknown->QueryInterface( IID_IDispatch, (void**) &amp;pDisp );
    if ( SUCCEEDED(hr) )
    {
        hr = pDisp->GetIDsOfNames( riid, rgszNames, cNames, lcid, 
                 rgdispid);
        pDisp->Release();
    }
    
    return hr;
 
}
 
STDMETHODIMP MyExtension::Invoke(DISPID dispidMember, REFIID riid,
        LCID lcid, WORD wFlags, DISPPARAMS* pdispparams, VARIANT* 
                pvarResult, EXCEPINFO* pexcepinfo, UINT* puArgErr)
{
    IDispatch *pDisp = NULL;
    HRESULT    hr = S_OK;
    hr = m_pOuterUnknown->QueryInterface( IID_IDispatch, (void**) &amp;pDisp );
    if ( SUCCEEDED(hr) )
    {
        hr = pDisp->Invoke( dispidMember, riid, lcid, wFlags, 
                 pdispparams, pvarResult, pexcepinfo, puArgErr);
        pDisp->Release();
    }
    
    return hr;
}
```



Extension writers are strongly encouraged to support dual interfaces instead of dispatch interfaces in their extension objects. A dual interface enables a client to have faster access, as long as vtable access is enabled in the client. For more information, see [Late Binding vs. Vtable Access in the ADSI Extension Model](late-binding-vs--vtable-access-in-the-adsi-extension-model.md). Based on the current model, implementing dual interfaces should not be more difficult than implementing dispatch interfaces.

 

 




