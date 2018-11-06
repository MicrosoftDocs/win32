---
title: Initialize DRM Import Example
description: Initialize DRM Import Example
ms.assetid: 46a64305-9aac-47df-992d-6aea8ecb54bf
keywords:
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,example code
- Windows Media Format SDK,code examples
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),initialize import
- DRM (digital rights management),initialize import
- digital rights management (DRM),example code
- DRM (digital rights management),example code
- digital rights management (DRM),code examples
- DRM (digital rights management),code examples
- DRM Client Extended APIs,initialize import
- Client Extended APIs,initialize import
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,example code
- Client Extended APIs,example code
- DRM Client Extended APIs,code examples
- Client Extended APIs,code examples
ms.topic: article
ms.date: 05/31/2018
---

# Initialize DRM Import Example

The following code example illustrates how to initialize a DRM writer object for DRM Import:


```C++
HRESULT InitializeImport( IWMDRMWriter3 *pDRMWriter )
{
    // Set this value to the desired number of bytes in an encrypted 
    //  session key.
    const int MODULUS_SIZE = 32;

    HRESULT hr = S_OK;
    WMDRM_IMPORT_INIT_STRUCT ImportInit;

    BYTE *pbEncryptedSessionKey = NULL;
    DWORD cbEncryptedSessionKey = 0;

    WMDRM_IMPORT_SESSION_KEY *pSessionKey = NULL;
    DWORD cbSessionKey = 0;

    WMDRM_IMPORT_CONTENT_KEY *pContentKey = NULL;
    DWORD cbContentKey = 0;
        
    // Allocate memory for the encrypted session key.
    pbEncryptedSessionKey = new BYTE[ MODULUS_SIZE ];
    if( NULL == pbEncryptedSessionKey )
    {
        hr = E_OUTOFMEMORY;
        goto EXIT;
    }
    cbEncryptedSessionKey = MODULUS_SIZE;

    hr = CreateSessionKey( &pSessionKey, &cbSessionKey );
    if( FAILED( hr ) ) goto EXIT;

    if( cbSessionKey > MODULUS_SIZE )
    if( FAILED( hr ) ) goto EXIT;

    hr = CreateContentKey( &pContentKey, &cbContentKey );
    if( FAILED( hr ) ) goto EXIT;

    // TODO: Encrypt the content key with the session Key.    
    // TODO: Encrypt the session key with the machine certificate public key.   

    ImportInit.dwVersion = 0;
    ImportInit.pbEncryptedSessionKeyMessage = pbEncryptedSessionKey;
    ImportInit.cbEncryptedSessionKeyMessage = cbEncryptedSessionKey;
    ImportInit.pbEncryptedKeyMessage = (BYTE*)pContentKey;
    ImportInit.cbEncryptedKeyMessage = cbContentKey;

    hr = pDRMWriter->SetProtectStreamSamples( &ImportInit );
    if( FAILED( hr ) ) goto EXIT;

EXIT:

    SAFE_ARRAY_DELETE( pContentKey );
    SAFE_ARRAY_DELETE( pSessionKey );

    return( hr );
}
```



## Related topics

<dl> <dt>

[**Create Content Key Example**](create-content-key-example.md)
</dt> <dt>

[**Create Session Key Example**](create-session-key-example.md)
</dt> <dt>

[**DRM Import Examples**](drm-import-examples.md)
</dt> </dl>

 

 




