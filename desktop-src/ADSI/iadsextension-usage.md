---
title: IADsExtension Usage
description: This topic contains C++ code examples for using the IADsExtension interface.
ms.assetid: 56bc87b4-f3cf-4177-90cb-e745889f8fef
ms.tgt_platform: multiple
keywords:
- extensions ADSI , IADsExtension
ms.topic: article
ms.date: 05/31/2018
---

# IADsExtension Usage

[**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension) is an optional interface implemented by the extension writer when at least one of the following conditions are met:

-   The extension component requires an initialization notification as defined by **ADSI\_EXT\_*dwCode*** in the [**Operate**](/windows/desktop/api/Iads/nf-iads-iadsextension-operate) method.
-   The extension supports a dual or dispatch interface.

If an extension component supports the [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension) interface for the first reason, the [**IADsExtension::PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) and [**IADsExtension::PrivateInvoke**](/windows/desktop/api/Iads/nf-iads-iadsextension-privateinvoke) methods can return **E\_NOTIMPL**. Alternatively, if an extension component supports a dual or dispatch interface , the [**Operate**](/windows/desktop/api/Iads/nf-iads-iadsextension-operate) method can ignore the data and return an **HRESULT** of **E\_NOTIMPL**.

The following code shows an extension implementing [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension).


```C++
STDMETHOD(Operate)(ULONG dwCode, VARIANT varData1, VARIANT varData2, VARIANT varData3)
{
    HRESULT hr = S_OK;
    switch (dwCode) 
    {
    case ADS_EXT_INIT:
         // Prompt for a credential.
         // MessageBox(NULL, "INITCRED", "ADsExt", MB_OK);
          break;
    default:
          hr = E_FAIL;
          break;
    }        
    return hr;        
}
 
STDMETHOD(PrivateGetIDsOfNames)(REFIID riid, OLECHAR ** rgszNames, unsigned int cNames, LCID lcid, DISPID  * rgdispid)
{        
      if (rgdispid == NULL)
      {
        return E_POINTER;
      }    
    return  DispGetIDsOfNames(m_pTypeInfo, rgszNames, cNames, rgdispid);
}
 
STDMETHOD(PrivateInvoke)(DISPID dispidMember, REFIID riid, LCID lcid, WORD wFlags, DISPPARAMS * pdispparams, VARIANT * pvarResult, EXCEPINFO * pexcepinfo, UINT * puArgErr)
{
 return DispInvoke( (IHelloWorld*)this, 
           m_pTypeInfo,
        dispidMember, 
        wFlags, 
        pdispparams, 
        pvarResult, 
        pexcepinfo, 
        puArgErr );
}
```



 

 




