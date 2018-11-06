---
title: Example Code for Reading defaultSecurityDescriptor
description: The following code example reads the defaultSecurityDescriptor for a specified object class.
ms.assetid: 9462686d-654b-40bb-be10-80ca03790ad5
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , reading defaultSecurityDescriptor
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Reading defaultSecurityDescriptor

The following code example reads the **defaultSecurityDescriptor** for a specified object class.


```C++
//  Add adsiid.lib to your project
//  Add activeds.lib to your project

#include <stdio.h>
#include "stdafx.h"
#include "iads.h"
#include "adshlp.h"

//  Entry point to the application
int wmain(int argc, WCHAR* argv[])
{
    HRESULT hr;
    IADsContainer *pAbsSchema = NULL;   //  For the abstract schema
    IADsClass *pClass = NULL;           //  For class objects
    IADsProperty *pProp = NULL;         //  For attribute objects
    IADsSyntax *pSyntax = NULL;         //  For syntax objects
    IEnumVARIANT *pEnum = NULL;
    ULONG lFetch;
    VARIANT var;
    VARIANT_BOOL bMulti, bAbstract, bAux;
    BSTR bstrPI, bstrClass, bstrName;
    LONG lCount = 0;
    LONG lVarType = 0;
    IADs *pChild = NULL;
    DWORD dwUnknownClass = 0;

    CoInitialize(NULL);

    //  Bind to the abstract schema.
    hr = ADsGetObject(L"LDAP://schema",
                      IID_IADsContainer,
                      (void**)&pAbsSchema);
    if (FAILED(hr)) 
        goto cleanup;

    //  Enumerate the attribute and class entries in the abstract schema.
    hr = ADsBuildEnumerator(pAbsSchema, &pEnum);
    if (FAILED(hr)) 
        goto cleanup;

    VariantInit(&var);
    hr = ADsEnumerateNext(pEnum, 1, &var, &lFetch);
    while( hr == S_OK && lFetch == 1)
    {
        //  Identify whether this is a class, attribute, or syntax.
        hr = V_DISPATCH(&var)->QueryInterface(IID_IADs, 
                                             (void**) &pChild);
        if (FAILED(hr)) 
            goto cleanuploop;
        hr = pChild->get_Class(&bstrClass);
        if (FAILED(hr)) 
            goto cleanuploop;
        wprintf(L"%s", bstrClass );
        hr = pChild->get_Name(&bstrName);
        if (FAILED(hr)) 
            goto cleanuploop;
        wprintf(L",%s", bstrName);

        //  Retrieve data, depending on the type of schema element.
        if (_wcsicmp(L"Class", bstrClass)==0)
        {
            hr = pChild->QueryInterface(IID_IADsClass, 
                                        (void**) &pClass);
            if (FAILED(hr)) 
                goto cleanuploop;
            pClass->get_Abstract(&bAbstract);
            pClass->get_Auxiliary(&bAux);
            if (bAbstract)
                wprintf(L",Abstract");
            else if (bAux)
                wprintf(L",Auxiliary");
            else 
                wprintf(L",Structural");

            //  Retrieve the primary ADSI 
            //  interface to use with this class.
            pClass->get_PrimaryInterface(&bstrPI);
            if (_wcsicmp(L"{FD8256D0-FD15-11CE-ABC4-02608C9E7553}", 
                bstrPI)==0)
                wprintf(L",IID_IADS,%s", bstrPI);
            if (_wcsicmp(L"{B15160D0-1226-11CF-A985-00AA006BC149}", 
                bstrPI)==0)
                wprintf(L",IID_IADsPrintQueue,%s", bstrPI);
            if (_wcsicmp(L"{A2F733B8-EFFE-11CF-8ABC-00C04FD8D503}", 
                bstrPI)==0)
                wprintf(L",IID_IADsOU,%s", bstrPI);
            if (_wcsicmp(L"{A05E03A2-EFFE-11CF-8ABC-00C04FD8D503}", 
                bstrPI)==0)
                wprintf(L",IID_IADsLocality,%s", bstrPI);
            if (_wcsicmp(L"{3E37E320-17E2-11CF-ABC4-02608C9E7553}", 
                bstrPI)==0)
                wprintf(L",IID_IADsUser,%s", bstrPI);
            if (_wcsicmp(L"{27636B00-410F-11CF-B1FF-02608C9E7553}", 
                bstrPI)==0)
                wprintf(L",IID_IADsGroup,%s", bstrPI);
            if (_wcsicmp(L"{00E4C220-FD16-11CE-ABC4-02608C9E7553}", 
                bstrPI)==0)
                wprintf(L",IID_IADsDomain,%s", bstrPI);
            SysFreeString(bstrPI);
        }
        else if (_wcsicmp(L"Property",bstrClass)==0)
        {
            hr = pChild->QueryInterface(IID_IADsProperty, 
                (void**) &pProp);
            if (FAILED(hr)) 
                goto cleanuploop;
            pProp->get_MultiValued(&bMulti);
            wprintf(L",%s", bMulti ? L"Multi-Valued" : L"Single-Valued");
        }
        else if (_wcsicmp(L"Syntax", bstrClass)==0)
        {
            hr = pChild->QueryInterface(IID_IADsSyntax, 
                (void**) &pSyntax);
            if ( FAILED(hr) ) 
                goto cleanuploop;
            pSyntax->get_OleAutoDataType (&lVarType);
            wprintf(L",%u", lVarType);
        }
        else
            dwUnknownClass++;

cleanuploop:
        wprintf(L"\n");
        SysFreeString(bstrClass);
        SysFreeString(bstrName);
        pChild->Release();
        VariantClear(&var);
        if (SUCCEEDED(hr))
            hr = ADsEnumerateNext( pEnum, 1, &var, &lFetch );
    }

    wprintf(L"dwUnknownClass: %u\n", dwUnknownClass);
cleanup:
    if (pAbsSchema)
        pAbsSchema->Release();
    if (pEnum)
        pEnum->Release();
    VariantClear(&var);
    CoUninitialize();

    return hr;
}
```



 

 




