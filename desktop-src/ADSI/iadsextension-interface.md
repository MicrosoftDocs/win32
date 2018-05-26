---
title: IADsExtension Interface
description: This topic contains C++ code examples for using the IADsExtension interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fa94cc55-1ab2-4b6e-a3b6-8c20542adb42
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IADsExtension ADSI ,using
- ADSI ADSI ,example code C/C++ ,using IADsExtension
- extensions ADSI ,IADsExtension
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IADsExtension Interface

The [**IADsExtension**](/windows/win32/Iads/nn-iads-iadsextension?branch=master) interface is defined as follows:


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



The aggregator (ADSI) calls the [**IADsExtension::Operate**](/windows/win32/Iads/nf-iads-iadsextension-operate?branch=master) method. The extension should interpret the *dwCode* parameter and each *varData* parameter, according to the provider's documentation.

The aggregator (ADSI), calls the [**IADsExtension::PrivateGetIDsOfNames**](/windows/win32/Iads/nf-iads-iadsextension-privategetidsofnames?branch=master) method. It is called after ADSI determines the extension to service the dispatch. The extension could use the type information for getting the DISPID, that is, using the [**DispGetIDsOfNames**](https://msdn.microsoft.com/library/windows/desktop/ms221309) function.

ADSI normally calls the [**PrivateInvoke**](/windows/win32/Iads/nf-iads-iadsextension-privateinvoke?branch=master) method after calling the [**PrivateGetIDsOfNames**](/windows/win32/Iads/nf-iads-iadsextension-privategetidsofnames?branch=master) function. The extension should call the actual method that it implements. Alternatively, the extension can use type information and call the [**DispInvoke**](69b89e5c-2a04-4a6a-beb0-18e68f8866ac) function.

All parameters have the same meaning as the parameters in the standard [**IDispatch::Invoke**](964ade8e-9d8a-4d32-bd47-aa678912a54d) method.

 

 




