---
title: IADsExtension Interface
description: This article contains the C++ code definition of the IADsExtension interface and discussion of its methods. 
ms.assetid: fa94cc55-1ab2-4b6e-a3b6-8c20542adb42
ms.tgt_platform: multiple
keywords:
- IADsExtension ADSI ,using
- ADSI ADSI ,example code C/C++ ,using IADsExtension
- extensions ADSI ,IADsExtension
ms.topic: article
ms.date: 05/31/2018
---

# IADsExtension Interface

The [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension) interface is defined as follows:


```C++
IADsExtension : public IUnknown
    {
    public:
        virtual HRESULT STDMETHODCALLTYPE Operate( 
            /* [in] */ DWORD dwCode,
            /* [in] */ VARIANT varData1,
            /* [in] */ VARIANT varData2,
            /* [in] */ VARIANT varData3) = 0;
 
        virtual HRESULT STDMETHODCALLTYPE PrivateGetIDsOfNames( 
            /* [in] */ REFIID riid,
            /* [in] */ OLECHAR **rgszNames,
            /* [in] */ unsigned int cNames,
            /* [in] */ LCID lcid,
            /* [out] */ DISPID *rgDispid) = 0;
 
        virtual HRESULT STDMETHODCALLTYPE PrivateInvoke( 
            /* [in] */ DISPID dispidMember,
            /* [in] */ REFIID riid,
            /* [in] */ LCID lcid,
            /* [in] */ WORD wFlags,
            /* [in] */ DISPPARAMS *pdispparams,
            /* [out] */ VARIANT *pvarResult,
            /* [out] */ EXCEPINFO *pexcepinfo,
            /* [out] */ unsigned int *puArgErr) = 0;
    };
```



The aggregator (ADSI) calls the [**IADsExtension::Operate**](/windows/desktop/api/Iads/nf-iads-iadsextension-operate) method. The extension should interpret the *dwCode* parameter and each *varData* parameter, according to the provider's documentation.

The aggregator (ADSI), calls the [**IADsExtension::PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) method. It is called after ADSI determines the extension to service the dispatch. The extension could use the type information for getting the DISPID, that is, using the [**DispGetIDsOfNames**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-dispgetidsofnames) function.

ADSI normally calls the [**PrivateInvoke**](/windows/desktop/api/Iads/nf-iads-iadsextension-privateinvoke) method after calling the [**PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) function. The extension should call the actual method that it implements. Alternatively, the extension can use type information and call the [**DispInvoke**](/windows/win32/api/oleauto/nf-oleauto-dispinvoke) function.

All parameters have the same meaning as the parameters in the standard [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke) method.

 

 