---
title: Create Session Key Example
description: Create Session Key Example
ms.assetid: 4347502b-3900-4306-b58c-16d151200e6c
keywords:
- Windows Media Format SDK,session keys
- Windows Media Format SDK,content keys
- Windows Media Format SDK,example code
- Windows Media Format SDK,code examples
- digital rights management (DRM),session keys
- DRM (digital rights management),session keys
- digital rights management (DRM),content keys
- DRM (digital rights management),content keys
- digital rights management (DRM),example code
- DRM (digital rights management),example code
- digital rights management (DRM),code examples
- DRM (digital rights management),code examples
- DRM Client Extended APIs,session keys
- Client Extended APIs,session keys
- DRM Client Extended APIs,content keys
- Client Extended APIs,content keys
- DRM Client Extended APIs,example code
- Client Extended APIs,example code
- DRM Client Extended APIs,code examples
- Client Extended APIs,code examples
- session keys
- content keys
ms.topic: article
ms.date: 05/31/2018
---

# Create Session Key Example

The session key is used to protect the content key. The following code demonstrates how to create a session key, but leaves out the details of random key generation.


```C++
HRESULT CreateSessionKey( WMDRM_IMPORT_SESSION_KEY **ppSessionKey, DWORD *pcbSessionKey )
{
    // TODO: Set this value to the desired number of bytes for the session key data. 
    const DWORD SESSION_KEY_DATA_SIZE = 20; 

    HRESULT hr = S_OK;
    WMDRM_IMPORT_SESSION_KEY *pSessionKey = NULL;

    if( NULL == ppSessionKey )
    {
        hr = E_POINTER;
        goto EXIT;
    }
    
    // Compute the size of the session key structure plus the session key.
    DWORD cbSessionKey = sizeof( WMDRM_IMPORT_SESSION_KEY ) + SESSION_KEY_DATA_SIZE;

    // Allocate memory for the session key.
    pSessionKey = (WMDRM_IMPORT_SESSION_KEY *)new BYTE[ cbSessionKey ];
    if( NULL == pSessionKey )
    {
        hr = E_OUTOFMEMORY;
        goto EXIT;
    }
    ZeroMemory( pSessionKey, cbSessionKey );

    // Set the key type and the key size.
    pSessionKey->dwKeyType = WMDRM_KEYTYPE_RC4;
    pSessionKey->cbKey = SESSION_KEY_DATA_SIZE;
    
    // Set the key to a random value. Note that the random number
    //  generator is not very good. It is only intended to be demonstrative
    //  and it is not recommended for use in shipping code.
    srand((unsigned int)time(NULL));
    BYTE* pKeyData = pSessionKey->rgbKey;
    for (size_t i = 0; i < SESSION_KEY_DATA_SIZE; ++i)
    {
        *pKeyData++ = (BYTE)(rand() & 0xFF); 
    }
    
    // If all has been successful set the parameters.
    *ppSessionKey = pSessionKey;
    pSessionKey = NULL;
    *pcbSessionKey = cbSessionKey;

EXIT:
    
    SAFE_ARRAY_DELETE( pSessionKey );
    return hr;
}
```



## Related topics

<dl> <dt>

[**DRM Import Examples**](drm-import-examples.md)
</dt> </dl>

 

 




