---
title: IADsPathname Interface
description: Parses and modifies various elements of an ADsPath.
ms.assetid: 1f820488-2e75-4257-90c7-9ec67aac4fe4
ms.tgt_platform: multiple
keywords:
- IADsPathname Interface ADSI
- IADsPathname ADSI , using
- ADSI ADSI , example code C/C++ , using IADsPathname
ms.topic: article
ms.date: 05/31/2018
---

# IADsPathname Interface

The [**IADsPathname**](/windows/desktop/api/Iads/nn-iads-iadspathname) interface parses and modifies various elements of an ADsPath. It also converts ADsPaths between various display formats.

The following code example extracts and returns the server name from a valid ADsPath for display to the user in a maintenance utility.


```C++
HRESULT GetServerName(BSTR adsPath, BSTR *adsServer)
{
    HRESULT hr = S_OK;
    IADsPathname *pIADsPathname = NULL;
 
    // Create the IADsPathname object.
    hr = CoCreateInstance(CLSID_Pathname,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IADsPathname,
                          (void**) &pIADsPathname);
    if (FAILED(hr))
    {
        if (pIADsPathname)
            pIADsPathname->Release();
        return (hr);
    }
 
    // Set the path.
    hr = pIADsPathname->Set(adsPath, ADS_SETTYPE_FULL);
    if (SUCCEEDED(hr))
        // Extract and return the server name.
        hr = pIADsPathname->Retrieve(ADS_FORMAT_SERVER, adsServer);
 
    // Cleanup.
    pIADsPathname->Release();
    return (hr);
}
```



The following code example helps to initialize a newly created ADSI object by setting the object's **Distinguished Name** property from its own ADsPath. Be aware that the calling routine must commit any changes to the underlying directory store by invoking the **SetInfo** method.


```C++
HRESULT SetDistinguishedName(IADs *pIADs)
{
    HRESULT hr = S_OK;
    CComBSTR sbstrADsPath;
    IADsPathname *pIADsPathname = NULL;
 
    // Get the ADsPath for this object.
    hr = pIADs->get_ADsPath(&sbstrADsPath);
    if (FAILED(hr))
        return (hr);
 
    // Create the IADsPathname object.
    hr = CoCreateInstance(CLSID_Pathname,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IADsPathname,
                          (void**) &pIADsPathname);
    if (FAILED(hr))
    {
        if (pIADsPathname)
            pIADsPathname->Release();
        return (hr);
    }
     // Set the path.
    hr = pIADsPathname->Set(sbstrADsPath, ADS_SETTYPE_FULL);
    if (SUCCEEDED(hr))
    {
        CComBSTR sbstrDNPath;

        // Convert the path to Distinguished Name format.
        hr = pIADsPathname->Retrieve(ADS_FORMAT_WINDOWS_DN,
                                     &sbstrDNPath);
 
        if (SUCCEEDED(hr))
        {
            // Set the distinguished name property.
            VARIANT var;
            VariantInit(&var);
            V_BSTR(&var) = sbstrDNPath;
            V_VT(&var) = VT_BSTR;
            hr = pIADs->Put(CComBSTR("distinguishedName"), var);
            VariantClear(&var);
        }
    }
 
    // Cleanup.
    pIADsPathname->Release();
    return (hr);
 
}
```



 

 




