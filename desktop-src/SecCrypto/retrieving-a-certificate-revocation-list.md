---
Description: Demonstrates how to retrieve a certificate revocation list.
ms.assetid: b8fbffae-d968-453d-81f0-af9d60be5fa9
title: Retrieving a Certificate Revocation List
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving a Certificate Revocation List

A [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA) is responsible for publishing its [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL). The current CRL can be retrieved by using the [**ICertAdmin2::GetCRL**](/windows/win32/Certadm/nf-certadm-icertadmin-getcrl?branch=master) method. In cases where a CA's certificate has been renewed, you might need to retrieve CRLs for the previous CA certificates. For information about CA renewal, see [Certification Authority Renewal](certification-authority-renewal.md). Additionally, a CA might publish delta CRLs. To retrieve CRLs for renewed CA certificates or delta CRLs, use either the [**ICertAdmin2::GetCAProperty**](/windows/win32/Certadm/nf-certadm-icertadmin2-getcaproperty?branch=master) or [**ICertRequest2::GetCAProperty**](/windows/win32/Certcli/nf-certcli-icertrequest2-getcaproperty?branch=master) methods.

The following example shows retrieving the current CRL.


```C++
    ICertAdmin2 * pCertAdmin2 = NULL;  // pointer to interface object
    BSTR bstrCA = NULL;  // variable for computer\CAname
    BSTR bstrCRL = NULL;  // variable to contain the retrieved CRL
    HRESULT hr;

    // Initialize COM.
    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr))
    {
        printf("Failed CoInitializeEx [%x]\n", hr);
        goto error;
    }

    // Create the CertAdmin object,
    // and get a pointer to its ICertAdmin interface.
    hr = CoCreateInstance( CLSID_CCertAdmin,
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           IID_ICertAdmin2,
                           (void **)&amp;pCertAdmin2;);
    if (FAILED(hr))
    {
        printf("Failed CoCreateInstance pCertAdmin2 [%x]\n", hr);
        goto error;
    }

    // Note the use of two '\' in C++ to produce one '\'.
    bstrCA = SysAllocString(L"<COMPUTERNAMEHERE>\\<CANAMEHERE>");
    if (FAILED(hr))
    {
        printf("Failed to allocate memory for bstrCA\n");
        goto error;
    }

    // Retrieve the CRL.
    hr = pCertAdmin2->GetCRL( bstrCA, CR_OUT_BINARY, &amp;bstrCRL );
    if (FAILED(hr))
    {
        printf("Failed GetCRL [%x]\n", hr);
        goto error;
    }
    else
        printf("CRL retrieved successfully\n");
        // Use the CRL as needed...

    // Processing is finished.

error:

    // Free BSTR values.
    if (NULL != bstrCA)
        SysFreeString(bstrCA);

    if (NULL != bstrCRL)
        SysFreeString(bstrCRL);

    // Clean up object resources.
    if (NULL != pCertAdmin2)
        pCertAdmin2->Release();

    // Free COM resources.
    CoUninitialize();
```



The following example shows retrieving base and delta CRLs, including those for CA certificates that have been renewed. The example uses [**ICertAdmin2::GetCAProperty**](/windows/win32/Certadm/nf-certadm-icertadmin2-getcaproperty?branch=master), although [**ICertRequest2::GetCAProperty**](/windows/win32/Certcli/nf-certcli-icertrequest2-getcaproperty?branch=master) provides similar functionality.


```C++
    LONG nCACertCount, nIndex, nCRLState;
    VARIANT    variant;

    VariantInit(&amp;variant);
    // Determine the number of CA certificates.
    hr = pCertAdmin2->GetCAProperty(bstrCA, 
                                CR_PROP_CASIGCERTCOUNT,
                                0,
                                PROPTYPE_LONG, 
                                CR_OUT_BINARY, 
                                &amp;variant);
    if (FAILED(hr))
    {
        printf("Failed call to GetCAProperty - "
            "CR_PROP_CASIGCERTCOUNT\n");
        goto error;
    }
    nCACertCount = variant.lVal;

    for (nIndex = 0; nIndex < nCACertCount; nIndex++)
    {
           // Determine the CRL state for each certificate index.
           pCertAdmin2->GetCAProperty(bstrCA, 
                               CR_PROP_CRLSTATE, 
                               nIndex, 
                               PROPTYPE_LONG, 
                               CR_OUT_BINARY, 
                               &amp;variant);
        if (FAILED(hr))
        {
            printf("Failed call to GetCAProperty - "
                "CR_PROP_CRLSTATE\n");
            goto error;
        }
        nCRLState = variant.lVal;

        // Process certificate indices only when 
        // the CRL state is valid.
        if (CA_DISP_VALID == nCRLState)
        {
           // Retrieve the base CRL.
           hr = pCertAdmin2->GetCAProperty(bstrCA,
                                   CR_PROP_BASECRL, 
                                   nIndex, 
                                   PROPTYPE_BINARY,
                                   CR_OUT_BINARY, 
                                   &amp;variant);
           if (FAILED(hr))
           {
               printf("Failed call to GetCAProperty - "
                   "CR_PROP_BASECRL\n");
               goto error;
           }

           // Use the base CRL as needed (not shown).
           // ...

           // Retrieve the delta CRL.
           hr = pCertAdmin2->GetCAProperty(bstrCA, 
                                   CR_PROP_DELTACRL, 
                                   nIndex, 
                                   PROPTYPE_BINARY, 
                                   CR_OUT_BINARY, 
                                   &amp;variant);
           if (FAILED(hr))
           {
               printf("Failed call to GetCAProperty - "
                   "CR_PROP_DELTACRL\n");
               goto error;
           }

           // Use the delta CRL as needed (not shown).
           // ...

       }        
    }
    
    // Processing is finished.

error:

    // Clean up object resources.
    if ( NULL != pCertAdmin2 )
        pCertAdmin2->Release();

    // Free BSTR variables.
    if ( NULL != bstrCA )
        SysFreeString ( bstrCA );

    // Clear the variant.
    VariantClear(&amp;variant);
```



 

 



