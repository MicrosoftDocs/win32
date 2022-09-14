---
title: IADsNameTranslate Interface
description: The IADsNameTranslate interface is used to translate distinguished names between various formats. Name translations are performed on the directory server, and this interface is currently available only to objects in Active Directory.
ms.assetid: c5c6e821-f19b-4269-81de-34c79dd2731f
ms.tgt_platform: multiple
keywords:
- IADsNameTranslate Interface ADSI
- IADsTranslate ADSI , using
- ADSI ADSI , example code C/C++ , using IADsTranslate
ms.topic: article
ms.date: 05/31/2018
---

# IADsNameTranslate Interface

The [**IADsNameTranslate**](/windows/desktop/api/Iads/nn-iads-iadsnametranslate) interface is used to translate distinguished names between various formats. Name translations are performed on the directory server, and this interface is currently available only to objects in Active Directory.

The following code example converts an account name from Windows format into LDAP format.


```C++
HRESULT TranslateNTNameToLDAPName( BSTR * pNTName, BSTR * pLDAPName )
{
    IADsNameTranslate *pTrans;
    HRESULT hr = S_OK;
 
    hr = CoCreateInstance(CLSID_NameTranslate, 
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IADsNameTranslate,
                          (void**) &pTrans );
    if (FAILED(hr)) { return hr; }

    hr = pTrans->Init(ADS_NAME_INITTYPE_DOMAIN, 
                      CComBSTR("Fabrikam.com"));
    if (FAILED(hr)) { return hr; }

    hr = pTrans->Set(ADS_NAME_TYPE_NT4, *pNTName);
    if (FAILED(hr)) { return hr; }

    hr = pTrans->Get(ADS_NAME_TYPE_1779, pLDAPName);
    pTrans->Release();
    return hr;
}
```



 

 




