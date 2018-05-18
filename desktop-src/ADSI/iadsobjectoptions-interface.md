---
title: IADsObjectOptions Interface
description: The IADsObjectOptions interface enables direct access to setting and retrieving provider-specific options.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b4ac114f-1a23-4be6-af02-0c0d34a8f78f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["IADsObjectOptions Interface ADSI", "IADsObjectOptions ADSI , using", "ADSI ADSI , example code C/C++ , using IADsObjectOptions"]
---

# IADsObjectOptions Interface

The [**IADsObjectOptions**](iadsobjectoptions.md) interface enables direct access to setting and retrieving provider-specific options.

One of the Active Directory object options is to return the host name of a server. The following code example uses the interface to retrieve the host name of the global catalog server.


```C++
HRESULT GetGCServerName(VARIANT *vGCServer) 
{
    HRESULT hr = S_OK
    HRESULT hre = S_OK;
    IADsContainer *pContainer = NULL;
    IUnknown *pUnk = NULL;
    IEnumVARIANT *pEnum = NULL;
    IDispatch *pDisp = NULL;
    IADsObjectOptions *pOpt = NULL;
    VARIANT var;
    ULONG lFetch = 0;

    VariantInit(&amp;var);
 
    // Bind to the global catalog using a serverless bind.
    hr = ADsOpenObject(L"GC:", NULL, NULL,
                       ADS_SECURE_AUTHENTICATION,
                       IID_IADsContainer, (void**) &amp;pContainer );
    if (FAILED(hr))
        return (hr);
 
    hr = pContainer->get__NewEnum(&amp;pUnk);
    if (SUCCEEDED(hr))
    {
        hr = pUnk->QueryInterface(IID_IEnumVARIANT, (void**) &amp;pEnum);
        if (SUCCEEDED(hr))
        {
            // Enumerate.
            hr = pEnum->Next(1, &amp;var, &amp;lFetch);
            if (SUCCEEDED(hr))
            {
                while (SUCCEEDED(hr))
                {
                    if (lFetch == 1)
                    {
                        pDisp = V_DISPATCH(&amp;var);
                        hre = pDisp->QueryInterface(
                                          IID_IADsObjectOptions,
                                          (void**)&amp;pOpt);
                        if (pDisp)
                            pDisp->Release();
                    }
                    VariantClear(&amp;var);
                    hr = pEnum->Next(1, &amp;var, &amp;lFetch);
                }
                // S_FALSE indicates that the row was read properly.
                if (hr == S_FALSE)
                    hr = hre;
            }
 
            if (SUCCEEDED(hr))
            {
                // There is a valid pOpt, so request the server name.
                VariantInit(vGCServer);
                hr = pOpt->GetOption(ADS_OPTION_SERVERNAME,vGCServer);
            }
        }
    }
 
// Cleanup.
    VariantClear(&amp;var);
    if (pOpt)
        pOpt->Release();
    if (pEnum)
        pEnum->Release();
    if (pUnk)
        pUnk->Release();
    if (pContainer)
        pContainer->Release();
    return (hr);
}
```



 

 




