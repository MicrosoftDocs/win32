---
title: Classifying Files
description: This sample demonstrates using FSRM to classify multiple files at once. This approach is much faster when dealing with many files, compared to setting the properties using an API call for each file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 94e382d6-3e18-4c80-aed2-4c2d58699236
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Classifying Files

This sample demonstrates using FSRM to classify multiple files at once. This approach is much faster when dealing with many files, compared to setting the properties using an API call for each file.

This is the source to Main.cpp.


```C++
#include "main.h"

STDMETHODIMP CClassificationSink::Invoke(
    __in DISPID dispidMember, 
    __in REFIID riid, 
    __in LCID lcid, 
    __in WORD wFlags, 
    __in DISPPARAMS* pdispparams, 
    __out_opt VARIANT* pvarResult, 
    __out_opt EXCEPINFO* pexcepinfo, 
    __out_opt UINT* puArgErr
    )
{
    UNREFERENCED_PARAMETER(riid);
    UNREFERENCED_PARAMETER(lcid);

    if (pexcepinfo)
    {
        ::ZeroMemory(pexcepinfo, sizeof(EXCEPINFO));
    }

    if (puArgErr)
    {
        *puArgErr = 0;
    }

    if (!pvarResult)
    {
        ::VariantInit(pvarResult);
    }

    HRESULT hr = S_OK;

    CComPtr<IFsrmCollection> spProperties;

    if (dispidMember != (FSRM_DISPID_CLASSIFICATION_EVENTS | 0x01))
    {
        fwprintf(stderr, 
                 L"Unknown DISPID, expecting 0x%08lx - this is an error.\n", 
                 (FSRM_DISPID_CLASSIFICATION_EVENTS | 0x01));
        hr = DISP_E_MEMBERNOTFOUND;
        goto end;
    }

    if (!(wFlags & DISPATCH_METHOD))
    {
        fwprintf(stderr, 
                 L"IDispatch::Invoke called unexpectedly with wFlags not set to DISPATCH_METHOD - this is an error.\n");
        hr = DISP_E_MEMBERNOTFOUND;
        goto end;
    }

    if (!pdispparams)
    {
        fwprintf(stderr, L"DISPPARAMS is NULL - this is an error\n");
        hr = DISP_E_PARAMNOTOPTIONAL;
        goto end;
    }

    if (!(pdispparams->rgvarg))
    {
        fwprintf(stderr, L"DISPPARAMS->rgVarg is NULL - this is an error\n");
        hr = DISP_E_PARAMNOTOPTIONAL;
        goto end;
    }

    if (pdispparams->cArgs != 4)
    {
        fwprintf(stderr, 
                 L"Expected parameters count is incorrect, found %d parameters but expecting 4\n", 
                 pdispparams->cArgs);
        hr = DISP_E_BADPARAMCOUNT;
        goto end;
    }

    if (pdispparams->rgvarg[0].vt != VT_DISPATCH ||
        pdispparams->rgvarg[1].vt != VT_BSTR ||
        pdispparams->rgvarg[2].vt != VT_I4 ||
        pdispparams->rgvarg[3].vt != VT_BSTR)
    {
        fwprintf(stderr, L"Expected parameters are not the correct varaiant types.\n");
        hr = DISP_E_TYPEMISMATCH;
        goto end;
    }

    if (pdispparams->cNamedArgs != 0)
    {
        fwprintf(stderr, L"Expected no named parameters but found %d\n", pdispparams->cNamedArgs);
        hr = DISP_E_NONAMEDARGS;
        goto end;
    }

    // Param 0: IDispatch for IFsrmCollection containing the properties on the file
    if (pdispparams->rgvarg[0].pdispVal != NULL)
    {
        hr = pdispparams->rgvarg[0].pdispVal->QueryInterface(&amp;spProperties);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"QueryInterface(IID_IFsrmCollection) failed with HR = 0x%08lx\n", hr);
            hr = DISP_E_TYPEMISMATCH;
            goto end;
        }
    }

    // Call OnFile to display the results
    hr = OnFile(pdispparams->rgvarg[3].bstrVal,           // Param 3: BSTR (File name)
                (HRESULT) pdispparams->rgvarg[2].lVal,    // Param 2: HRESULT = Classification result for the file
                pdispparams->rgvarg[1].bstrVal,           // Param 1: BSTR (File Messages)
                spProperties);
    if (FAILED(hr))
    {
        fwprintf(stderr, L"CClassificationSink::OnFile returned HR = 0x%08lx\n", hr);
        goto end;
    }

end:
    return hr;
}

HRESULT
CClassificationSink::OnFile(
    __in BSTR bstrFilePath,
    __in HRESULT hrFileResult,
    __in BSTR bstrFileMessages,
    __in_opt IFsrmCollection *pProperties
    )
{
    HRESULT hr = S_OK;

    long lCount = 0;

    CComPtr<IFsrmProperty> spProperty;

    if (::SysStringLen(bstrFilePath) == 0)
     {
        fwprintf(stderr, L"Classification OnFile event was received with empty file path\n");
        hr = E_INVALIDARG;
        goto end;;
     }

    wprintf(L"\n------------------------------------------------------\n");
    wprintf(L"Classification results for file: %ws\n", bstrFilePath);

    if (SUCCEEDED(hrFileResult))
    {
        wprintf(L"Status: Succeeded\n");
    }
    else
    {
        wprintf(L"Status: Failed with HR = 0x%08lx\n", hrFileResult);
        wprintf(L"Failure messages: %ws\n", bstrFileMessages);
    }

    wprintf(L"\nClassification properties returned for this file: \n\n");

    if(!pProperties)
    {
        wprintf(L"No properties were returned for the file\n");
        goto end;
    }

    hr = pProperties->get_Count(&amp;lCount);
    if (FAILED(hr))
    {
        fwprintf(stderr, L"IFsrmCollection::get_Count failed with 0x%08lx\n", hr);
        goto end;
    }

    for (long iProperty = 1; iProperty <= lCount; iProperty++)
    {
        CComVariant varProperty;

        hr = pProperties->get_Item(iProperty, &amp;varProperty);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"IFsrmCollection::get_Item failed with 0x%08lx\n", hr);
            goto end;
        }

        if (varProperty.vt != VT_DISPATCH)
        {
            fwprintf(stderr, 
                     L"IFsrmCollection::get_Item returned invalid element type, expected VT_DISPATCH.\n");
            hr = E_INVALIDARG;
            goto end;
        }

        if (!(varProperty.pdispVal))
        {
            fwprintf(stderr, L"IFsrmCollection::get_Item returned invalid element.\n");
            hr = E_INVALIDARG;
            goto end;
        }

        hr = varProperty.pdispVal->QueryInterface(&amp;spProperty);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"QueryInterface failed with 0x%08lx\n", hr);
            goto end;
        }

        long lPropertyFlags = 0;

        hr = spProperty->get_PropertyFlags(&amp;lPropertyFlags);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"IFsrmProperty::get_PropertyFlags failed with 0x%08lx\n", hr);
            goto end;
        }

        // Only show properties that are not marked as deleted
        if ((lPropertyFlags & FsrmPropertyFlags_Deleted) == 0)
        {
            CComBSTR bstrPropertyName;
            CComBSTR bstrPropertyValue;

            hr = spProperty->get_Name(&amp;bstrPropertyName);
            if (FAILED(hr))
            {
                fwprintf(stderr, L"IFsrmProperty::get_Name failed with 0x%08lx\n", hr);
                goto end;
            }

            hr = spProperty->get_Value(&amp;bstrPropertyValue);
            if (FAILED(hr))
            {
                fwprintf(stderr, L"IFsrmProperty::get_Value failed with 0x%08lx\n", hr);
                goto end;
            }

            wprintf(L"Property Name: %ws\n", bstrPropertyName);
            wprintf(L"Property Value: %ws\n\n", bstrPropertyValue);
        }
    }

    wprintf(L"\n------------------------------------------------------\n");

end:
    return hr;
}

HRESULT
CreateSafeArray(__in LONG cElements,
                __in const PCWSTR *ppwszElements,
                __out VARIANT *pvarElements
               )
{
    if (!pvarElements)
     {
      fwprintf(stderr, L"Invalid arguments specified to CreateSafeArray\n");
      return E_INVALIDARG;
     }

    ::VariantInit(pvarElements);

    if (!ppwszElements || (cElements <= 0))
     {
      fwprintf(stderr, L"Invalid arguments specified to CreateSafeArray\n");
      return E_INVALIDARG;
     }

    HRESULT hr = S_OK;

    SAFEARRAYBOUND sab = {cElements, 0};

    CComVariant varElements;
    V_ARRAY(&amp;varElements) = ::SafeArrayCreate(VT_VARIANT, 1, &amp;sab);

    if(!V_ARRAY(&amp;varElements))
    {
        fwprintf(stderr, L"SafeArrayCreate failed\n");
        hr = E_OUTOFMEMORY;
        goto end;
    }

    V_VT(&amp;varElements) = VT_ARRAY | VT_VARIANT;

    for(LONG iElement = 0; iElement < cElements; iElement++)
    {
        CComVariant varElement;

        if (ppwszElements[iElement] &amp;&amp; (ppwszElements[iElement][0] != L'\0'))
        {
            CComBSTR bstrElement(ppwszElements[iElement]);

            if (::SysStringLen(bstrElement) > 0)
            {
                V_BSTR(&amp;varElement) = bstrElement.Detach();
                V_VT(&amp;varElement) = VT_BSTR;
            }
            else
            {
                fwprintf(stderr, 
                         L"SafeArrayPutElement failed since it could not allocate memory - this is an error.\n");
                hr = E_OUTOFMEMORY;
                goto end;
            }
        }
        // else do not set. CComVariant would have initialized the value to VT_EMPTY

        hr = ::SafeArrayPutElement(V_ARRAY(&amp;varElements), &amp;iElement, &amp;varElement);
        if (FAILED(hr))
         {
          fwprintf(stderr, L"SafeArrayPutElement failed with HR = 0x%08lx\n", hr);
          goto end;
         }
    }

    hr = varElements.Detach(pvarElements);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"CComVariant::Detach failed with HR = 0x%08lx\n", hr);
      goto end;
     }

end:
    return hr;
}

void __cdecl wmain()
{
    HRESULT hr = S_OK;

    CComPtr<IFsrmClassificationManager2> spClsMgr;
    CComPtr<CComObject<CClassificationSink>> spClassificationSink;

    CComVariant varFilePaths;
    CComVariant varPropertyNames;
    CComVariant varPropertyValues;

    bool bInited = false;

    hr = ::CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"CoInitializeEx failed with HR = 0x%08lx\n", hr);
      goto end;
     }

    bInited = true;

    //
    // Pick and add file paths to classify
    //
    wprintf(L"Populating files paths to classify\n");

    PCWSTR pwszFilePaths[] = /* populate with file paths to classify. Eg. */ {L"P:\\Test.txt"};

    hr = CreateSafeArray(_countof(pwszFilePaths), pwszFilePaths, &amp;varFilePaths);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"PopulateFilePaths failed with HR = 0x%08lx\n", hr);
      goto end;
     }

    assert(V_ARRAY(&amp;varFilePaths));

    //
    // Pick and add property name and value pairs to classify with
    //
    wprintf(L"Populating property names and values to classify with\n");

    PCWSTR pwszPropertyNames[]  = /* populate with property names to classify with. Eg. */ 
                                  {L"Business Impact", L"Importance"};
    PCWSTR pwszPropertyValues[] = /* populate with property values to set/clear. 
                                     To set, specify the property value. 
                                     To clear, specify NULL. Eg. */ 
                                  {L"HBI", NULL};

    static_assert(_countof(pwszPropertyNames) == _countof(pwszPropertyValues), 
                                                          "Property names and values counts must match");

    hr = CreateSafeArray(_countof(pwszPropertyNames), pwszPropertyNames, &amp;varPropertyNames);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"CreateSafeArray failed with HR = 0x%08lx\n", hr);
      goto end;
     }

    hr = CreateSafeArray(_countof(pwszPropertyValues), pwszPropertyValues, &amp;varPropertyValues);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"CreateSafeArray failed with HR = 0x%08lx\n", hr);
      goto end;
     }

    assert(V_ARRAY(&amp;varPropertyNames) &amp;&amp; V_ARRAY(&amp;varPropertyValues));

    //
    // Instantiate classification manager
    //
    hr = spClsMgr.CoCreateInstance(__uuidof(FsrmClassificationManager), NULL, CLSCTX_SERVER);
    if (FAILED(hr))
     {
      fwprintf(stderr, L"CoCreateInstance for IFsrmClassificationManager2 failed with HR = 0x%08lx\n", hr);
      goto end;
     }

    assert(spClsMgr);

    //
    // Setup callback sink for classification
    //
    hr = CComObject<CClassificationSink>::CreateInstance(&amp;spClassificationSink);
    if (FAILED(hr))
    {
        fwprintf(stderr, L"CClassificationSink::CreateInstance failed with HR = 0x%08lx\n", hr);
        goto end;
    }

    assert(spClassificationSink);

    spClassificationSink.p->AddRef();

    hr = spClassificationSink->Initialize(spClsMgr);
    if (FAILED(hr))
    {
        fwprintf(stderr, L"CClassificationSink::Initialize failed with HR = 0x%08lx\n", hr);
        goto end;
    }

    //
    // First, invoke ClassifyFiles to enumerate all properties applied to the file paths
    // This could be done by not specifying any values for property names and values
    // FsrmGetFilePropertyOptions_NoRuleEvaluation simply reads properties as stored in 
    // the files/cache/storage modules without running any rules - this is faster
    // FsrmGetFilePropertyOptions_SkipOrphaned will skip properties whose property 
    // definitions are not available on the machine
    //
    wprintf(L"IFsrmClassificationManager2::ClassifyFiles is enumerating classification properties on files\n\n");

    hr = spClsMgr->ClassifyFiles(V_ARRAY(&amp;varFilePaths), 
                                 NULL,
                                 NULL,
                                 (FsrmGetFilePropertyOptions) (FsrmGetFilePropertyOptions_NoRuleEvaluation 
                                                             | FsrmGetFilePropertyOptions_SkipOrphaned));

    if (FAILED(hr))
    {
        fwprintf(stderr, L"IFsrmClassificationManager2::ClassifyFiles failed with HR = 0x%08lx\n", hr);
        goto end;
    }

    //
    // Second, invoke ClassifyFiles to set/clear properties to/from the file paths
    // Setting a property = specifying a property name and value pair
    // Clearing a property = specifying a property name with a corresponding 
    // VT_NULL/VT_EMPTY for the variant property value
    // The call back receives the set of properties set on the files after 
    // classification is completed with any errors that occurred during classification
    //
    wprintf(L"IFsrmClassificationManager2::ClassifyFiles is setting/clearing classification properties on files\n\n");

    hr = spClsMgr->ClassifyFiles(V_ARRAY(&amp;varFilePaths), 
                                 V_ARRAY(&amp;varPropertyNames), 
                                 V_ARRAY(&amp;varPropertyValues), 
                                 FsrmGetFilePropertyOptions_SkipOrphaned);

    if (FAILED(hr))
    {
        fwprintf(stderr, L"IFsrmClassificationManager2::ClassifyFiles failed with HR = 0x%08lx\n", hr);
        goto end;
    }

end:
    if (spClassificationSink)
    {
        assert(bInited);

        spClassificationSink->UnInitialize();
    }

    // Force release of references to the COM objects since we want to uninitialize COM before quitting wmain
    spClsMgr = NULL;
    spClassificationSink = NULL;

    if (bInited)
    {
        ::CoUninitialize();
    }

    wchar_t chTemp = L'\0';
    ::wprintf(L"Done. Press \"Enter\" to quit");
    ::wscanf_s(L"%c", &amp;chTemp, 1);
}
```



This is the header named Main.h used by the example above.


```C++
#pragma once

#include <stdio.h>
#include <objbase.h>
#include <assert.h>
#include <tchar.h>
#include <crtdbg.h>
#include <atlbase.h>
CComModule _Module;
#include <atlcom.h>

#include <fsrmpipeline.h>
#include <fsrmtlb.h>

//
// IFsrmClassificationManager2::ClassifyFiles publishes results for each file it classifies using DIFsrmClassificationEvents events
// CClassificationSink implements DIFsrmClassificationEvents callbacks and displays results for each file
//
class ATL_NO_VTABLE CClassificationSink :
    public CComObjectRootEx<CComMultiThreadModel>,    
    public IDispatch
{
    DECLARE_NO_REGISTRY()
    DECLARE_NOT_AGGREGATABLE(CClassificationSink)   

public:
    CClassificationSink()
        : m_dwConnectionPointCookie(0)
    {
    }

    virtual ~CClassificationSink()
    {
         //
         // Need to unintialize (invoke IConnectionPoint->Unadvise) outside destructor since IConnectionPoint is holding a reference to this object
         //
        assert(!m_spConnectionPoint);
        assert(m_dwConnectionPointCookie == 0);
    }

    void UnInitialize()
    {
        if (m_spConnectionPoint)
        {
            assert(m_dwConnectionPointCookie != 0);
            
            HRESULT hr = m_spConnectionPoint->Unadvise(m_dwConnectionPointCookie);
            if (FAILED(hr))
            {
                fwprintf(stderr, L"IConnectionPoint::Unadvise(DIFsrmClassificationEvents) failed with HR = 0x%08lx\n", hr);
            }
        }

        m_spConnectionPoint = NULL;
        m_dwConnectionPointCookie = 0;
    }

    HRESULT Initialize(
        __in IFsrmClassificationManager2 *pClsMgr
        )
    {
        assert(pClsMgr);
        
        CComPtr<IConnectionPointContainer> spConnPtContainer;
    
        // Setup connection for callbacks
        HRESULT hr = pClsMgr->QueryInterface(&amp;spConnPtContainer);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"IFsrmClassificationManager2::QueryInterface(IID_IConnectionPointContainer) failed with HR = 0x%08lx\n", hr);
            goto end;
        }

        hr = spConnPtContainer->FindConnectionPoint(DIID_DIFsrmClassificationEvents, &amp;m_spConnectionPoint);
        if (FAILED(hr))
        {
            fwprintf(stderr, L"IConnectionPoint::FindConnectionPoint(DIID_DIFsrmClassificationEvents) failed with HR = 0x%08lx\n", hr);
            goto end;
        }

        hr = m_spConnectionPoint->Advise(GetUnknown(), &amp;m_dwConnectionPointCookie); // Note that Advise will add a ref count to this object
        if (FAILED(hr))
        {
            fwprintf(stderr, L"IConnectionPoint::Advise(DIFsrmClassificationEvents) failed with HR = 0x%08lx\n", hr);
            goto end;
        }

        assert(m_dwConnectionPointCookie != 0);

    end:
        return hr;
    }

BEGIN_COM_MAP(CClassificationSink)
    COM_INTERFACE_ENTRY(IDispatch)
    COM_INTERFACE_ENTRY_IID(DIID_DIFsrmClassificationEvents, IDispatch)
END_COM_MAP()

public:

    // IDispatch
    STDMETHOD(GetTypeInfoCount) (
        __out UINT* pctinfo
        )
    {
        if (!pctinfo)
        {
            return E_POINTER;
        }

        *pctinfo = 0;

        return S_OK;
    }

     STDMETHOD(GetTypeInfo) (
        __in UINT itinfo, 
        __in LCID lcid, 
        __deref_out ITypeInfo** pptinfo
        )
    {
        UNREFERENCED_PARAMETER(itinfo);
        UNREFERENCED_PARAMETER(lcid);
        
        if (!pptinfo)
        {
            return E_POINTER;
        }

        *pptinfo = NULL;
        
        return E_NOTIMPL;
    }

     STDMETHOD(GetIDsOfNames)(
        __in REFIID riid, 
        __in LPOLESTR* rgszNames, 
        __in UINT cNames, 
        __in LCID lcid, 
        __out DISPID* rgdispid
        )
    {
        UNREFERENCED_PARAMETER(riid);
        UNREFERENCED_PARAMETER(rgszNames);
        UNREFERENCED_PARAMETER(cNames);
        UNREFERENCED_PARAMETER(lcid);
        
        if (!rgdispid)
        {
            return E_POINTER;
        }

        *rgdispid = 0;

        return E_NOTIMPL;
    }

     STDMETHOD(Invoke)(
        __in DISPID dispidMember, 
        __in REFIID riid, 
        __in LCID lcid, 
        __in WORD wFlags, 
        __in DISPPARAMS* pdispparams, 
        __out_opt VARIANT* pvarResult, 
        __out_opt EXCEPINFO* pexcepinfo, 
        __out_opt UINT* puArgErr
        );
     
private:
    HRESULT
    OnFile(
        __in BSTR bstrFilePath,
        __in HRESULT hrFileResult,
        __in BSTR bstrFileMessages,
        __in_opt IFsrmCollection *pProperties
        );

private:
    CComPtr<IConnectionPoint> m_spConnectionPoint;
    DWORD m_dwConnectionPointCookie;
};
```



## Related topics

<dl> <dt>

[Using FSRM](using-fsrm.md)
</dt> <dt>

[**DIFsrmClassificationEvents::OnFile**](difsrmclassificationevents-onfile.md)
</dt> <dt>

[**IFsrmClassificationManager2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager2?branch=master)
</dt> <dt>

[**IFsrmClassificationManager2::ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master)
</dt> <dt>

[**IFsrmCollection**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmcollection?branch=master)
</dt> <dt>

[**IFsrmCollection::Count**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmcollection-get_count?branch=master)
</dt> <dt>

[**IFsrmCollection::Item**](/windows/previous-versions/Fsrm/nf-fsrm-ifsrmcollection-get_item?branch=master)
</dt> <dt>

[**IFsrmProperty**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmproperty?branch=master)
</dt> <dt>

[**IFsrmProperty::Name**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmproperty-get_name?branch=master)
</dt> <dt>

[**IFsrmProperty::PropertyFlags**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmproperty-get_propertyflags?branch=master)
</dt> <dt>

[**IFsrmProperty::Value**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmproperty-get_value?branch=master)
</dt> </dl>

 

 




