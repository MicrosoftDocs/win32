---
title: Media Sample Encryption Example
description: Media Sample Encryption Example
ms.assetid: f57f9ffc-47fd-47fb-b553-07b9cd6abb70
keywords:
- Windows Media Format SDK,media sample encryption
- Windows Media Format SDK,example code
- Windows Media Format SDK,code examples
- digital rights management (DRM),media sample encryption
- DRM (digital rights management),media sample encryption
- digital rights management (DRM),example code
- DRM (digital rights management),example code
- digital rights management (DRM),code examples
- DRM (digital rights management),code examples
- DRM Client Extended APIs,media sample encryption
- Client Extended APIs,media sample encryption
- DRM Client Extended APIs,example code
- Client Extended APIs,example code
- DRM Client Extended APIs,code examples
- Client Extended APIs,code examples
ms.topic: article
ms.date: 05/31/2018
---

# Media Sample Encryption Example

The following incomplete example demonstrates how to encrypt a media sample using DRM encryption. The RC4 encryption algorithm has been left out of the example due to space restrictions.


```C++
QWORD GetNextSalt(QWORD qwSalt)
{
   return InterlockedIncrement64( (volatile LONGLONG*)&qwSalt );
}

HRESULT EncryptSample( INSSBuffer *pSample )
{
    HRESULT hr = S_OK;
    INSSBuffer3 *pNSSBuffer3 = NULL;
    QWORD qwSalt = 0;
    BYTE *pbData = NULL;
    DWORD cbData = 0;

    hr = pSample->QueryInterface( IID_INSSBuffer3, (void**)&pNSSBuffer3 );
    if( FAILED( hr ) ) goto EXIT;

    hr = pSample->GetBufferAndLength( &pbData, &cbData );
    if( FAILED( hr ) ) goto EXIT;

    qwSalt = GetNextSalt(qwSalt);

    // TODO: Encrypt the sample by concatenating the initialization vector
    //   and using RC4 encryption.

    hr = pNSSBuffer3->SetProperty( 
        WM_SampleExtensionGUID_SampleProtectionSalt, 
        &qwSalt, sizeof( qwSalt ) );
    if( FAILED( hr ) ) goto EXIT;

EXIT:

    SAFE_RELEASE( pNSSBuffer3 );
    return hr;
}
```



## Related topics

<dl> <dt>

[**DRM Import Examples**](drm-import-examples.md)
</dt> </dl>

 

 




