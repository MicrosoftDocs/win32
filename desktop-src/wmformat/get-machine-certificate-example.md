---
title: Get Machine Certificate Example
description: Get Machine Certificate Example
ms.assetid: 4112e29e-7c86-4825-9798-dd1a81b82083
keywords:
- Windows Media Format SDK,machine certificates
- Windows Media Format SDK,certificates
- Windows Media Format SDK,example code
- Windows Media Format SDK,code examples
- digital rights management (DRM),machine certificates
- DRM (digital rights management),machine certificates
- digital rights management (DRM),certificates
- DRM (digital rights management),certificates
- digital rights management (DRM),example code
- DRM (digital rights management),example code
- digital rights management (DRM),code examples
- DRM (digital rights management),code examples
- DRM Client Extended APIs,machine certificates
- Client Extended APIs,machine certificates
- DRM Client Extended APIs,certificates
- Client Extended APIs,certificates
- DRM Client Extended APIs,example code
- Client Extended APIs,example code
- DRM Client Extended APIs,code examples
- Client Extended APIs,code examples
- certificates,code examples
ms.topic: article
ms.date: 05/31/2018
---

# Get Machine Certificate Example

The following example shows how to retrieve the machine certificate collection:


```C++
HRESULT GetMachineCert( BYTE **ppbCert, DWORD *pcbCert )
{
    HRESULT hr = S_OK;
    IWMDRMProvider *pProvider = NULL;
    IWMDRMSecurity *pSecurity = NULL;
    BYTE rgbVersion[4];

    // Create a provider object.
    hr = WMDRMCreateProvider( &pProvider );
    if( FAILED( hr ) ) goto EXIT;

    // Create a security object from a provider object.
    hr = pProvider->CreateObject( IID_IWMDRMSecurity, (void**) &pSecurity );
    if( FAILED( hr ) ) goto EXIT;

    // Query the security to get the machine certificate.
    hr = pSecurity->GetMachineCertificate( WMDRM_CERTIFICATE_TYPE_V2,
        rgbVersion, ppbCert, pcbCert );

    if( FAILED( hr ) ) goto EXIT;

EXIT:

    SAFE_RELEASE( pSecurity );
    SAFE_RELEASE( pProvider );

    return hr;
}
```



## Related topics

<dl> <dt>

[**DRM Import Examples**](drm-import-examples.md)
</dt> </dl>

 

 




