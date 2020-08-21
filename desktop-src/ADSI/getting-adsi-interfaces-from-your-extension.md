---
title: Getting ADSI Interfaces From Your Extension
description: An extension often needs to get data from the directory object it binds to.
ms.assetid: 2d2e6dc6-1eed-491b-9d6a-7f35c24a7ba8
ms.tgt_platform: multiple
keywords:
- extensions ADSI ,getting ADSI interfaces from your extension
- ADSI ADSI ,example code C/C++ ,getting ADSI interfaces from your extension
ms.topic: article
ms.date: 05/31/2018
---

# Getting ADSI Interfaces From Your Extension

An extension often needs to get data from the directory object it binds to. For example, an extension for a **computer** object may want to get the **dnsHostName** of the current object from the directory. This can be easily achieved by issuing a **QueryInterface** call on the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface for the aggregator.


```C++
HRESULT hr;
IADs *pADs; ' ADSI Interface to get/set attributes.
 
hr = m_pOuterUnk->QueryInterface(IID_IADs,(void**)&pADs);
 
if ( SUCCEEDED(hr) )
{
    VARIANT var;
    VariantInit(&var);
    hr  = pADs ->Get(_bstr_t("dnsHostName"), &var);
    if ( SUCCEEDED(hr) )
    { 
        printf("%S\n", V_BSTR(&var));
    }
    VariantClear(&var);
    pADs->Release();
}
```



You should release the interface immediately after using it. If the extension has an open reference to the aggregator, you have created a circular reference and the aggregator cannot release the extension. Therefore, the aggregator cannot be released and the result is memory leaks in your application.

 

 