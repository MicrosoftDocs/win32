---
Description: Use the ICertServerPolicySetCertificateProperty method to set the subject properties of a certificate.
ms.assetid: 4cc20a59-d8e9-4c9b-9438-21bccbbe4a64
title: Setting Certificate Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting Certificate Properties

Use the [**ICertServerPolicy::SetCertificateProperty**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateproperty?branch=master) method to set the subject properties of a certificate. Subject properties are properties related to the owner of the certificate or the individual who requested the certificate. For a list of subject properties, see [Name Properties](name-properties.md).

You can also use the [**SetCertificateProperty**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateproperty?branch=master) method to set the NotBefore and NotAfter certificate properties. For a description of the NotBefore and NotAfter certificate properties, see [Certificate Properties](certificate-properties.md).

Use the [**ICertServerPolicy::SetCertificateExtension**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateextension?branch=master) method to add any number of extensions to the certificate. You can use extensions to add supplemental subject or usage information to the certificate. For more information, see [Extension Handlers](extension-handlers.md).

The following example sets a certificate property and extension on a certificate. You call the [**SetCertificateProperty**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateproperty?branch=master) and [**SetCertificateExtension**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateextension?branch=master) methods in your [**ICertPolicy2::VerifyRequest**](/windows/win32/Certpol/nf-certpol-icertpolicy-verifyrequest?branch=master) implementation. The example is not a complete **VerifyRequest** implementation; the example does not show verification logic.


```C++
#include <windows.h>
#include <stdio.h>

STDMETHODIMP CCertPolicy::VerifyRequest(
             BSTR const strConfig,
             LONG Context,
             LONG bNewRequest,
             LONG Flags,
             LONG __RPC_FAR *pDisposition)
{
    HRESULT hr = S_OK;
    ICertServerPolicy *pServer = NULL;
    BSTR bstrPropName = NULL;
    VARIANT vPropValue;
    BSTR bstrExtName = NULL;
    VARIANT vExtValue;


    // Retrieve an ICertServerPolicy interface pointer.
    hr = CoCreateInstance( CLSID_CCertServerPolicy,
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           IID_ICertServerPolicy,
                           (void **) &amp;pServer );
    if (FAILED( hr ))
    {
        printf("Failed CoCreateInstance for ICertServerPolicy "
            "- %x\n", hr );
        return hr;
    }

    // Set the context to which this request refers.
    hr = pServer->SetContext(Context);
    if (FAILED( hr ))
    {
        printf("Failed SetContext(%u) - %x\n", Context, hr );
        pServer->Release();
        return hr;
    }

    // Specify the subject property to set on the certificate.
    bstrPropName = SysAllocString(L"Subject.EMail");
    if ( NULL == bstrPropName )
    {
        hr = E_OUTOFMEMORY; 
        printf("Failed SysAllocString for bstrPropName "
            "(no memory)\n" );
        pServer->Release();
        return hr;
    }

    VariantInit( &amp;vPropValue );
    vPropValue.VT_BSTR;
    vPropValue.bstrVal = SysAllocString(L"someone@example.com");
    if ( NULL == vPropValue.bstrVal )
    {
        hr = E_OUTOFMEMORY; 
        printf("Failed SysAllocString for vPropValue "
            "(no memory)\n" );
        SysFreeString(bstrPropName);
        pServer->Release();
        return hr;
    }

    // Set the subject property on the certificate.
    hr = pServer->SetCertificateProperty( bstrPropName,
                                          PROPTYPE_STRING,
                                          &amp;vPropValue );
    SysFreeString(bstrPropName);
    VariantClear(&amp;vPropValue);
    if (FAILED(hr))
    {
        printf("Failed SetCertificateProperty - %x\n", hr);
        pServer->Release();
        return hr;
    }

    // Specify the extension property to set on the certificate.
    bstrExtName = SysAllocString(L"2.29.38.4");
    if ( NULL == bstrExtName )
    {
        hr = E_OUTOFMEMORY; 
        printf("Failed SysAllocString for bstrExtName "
            "(no memory)\n" );
        pServer->Release();
        return hr;
    }

    VariantInit( &amp;vExtValue );
    vExtValue.VT_BSTR;
    vExtValue.bstrVal = SysAllocString
        (L"http://example.microsoft.com");
    if ( NULL == vExtValue.bstrVal )
    {
        hr = E_OUTOFMEMORY; 
        printf("Failed SysAllocString for vExtValue (no memory)\n" );
        SysFreeString(bstrExtName);
        pServer->Release();
        return hr;
    }

    // Set the extension property on the certificate.
    hr = pServer->SetCertificateExtension( bstrExtName,
                                           PROPTYPE_STRING,
                                           EXTENSION_CRITICAL_FLAG,
                                           &amp;vExtValue );
    SysFreeString(bstrExtName);
    VariantClear(&amp;vExtValue);
    if (FAILED(hr))
    {
        printf("Failed SetCertificateExtension - %x\n", hr);
        pServer->Release();
        return hr;
    }

    pServer->Release();
    return(hr);

}
```



 

 



