---
description: Using the Credential Cache
ms.assetid: b58d0a6e-ecae-48a1-a3af-d4246caa272b
title: Using the Credential Cache
ms.topic: article
ms.date: 05/31/2018
---

# Using the Credential Cache

Media Foundation provides a default implementation of the [**IMFNetCredentialCache**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialcache) interface. An application that implements the [**IMFNetCredentialManager**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialmanager) interface can use the default credential cache object to store the user's credentials.

To create the default credential cache object, call the [**MFCreateCredentialCache**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatecredentialcache) function.


```C++
HRESULT hr = S_OK;
IMFNetCredentialCache *pCredentialCache = NULL;
hr = MFCreateCredentialCache(&pCredentialCache);
```



After the credential cache is created, the application can use the following methods to get a credential object, set user credentials, and specify the caching options.

-   To get the credential object for a URL, call [**IMFNetCredentialCache::GetCredential**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-getcredential).

    ```C++
    hr = pCredentialCache-> GetCredential(
            pszUrl,
            pszRealm,
            dwAuthenticationFlags,
            &pCredential,
            &dwRequirementsFlags);
    ```

    

    If the credentials for the specified URL do not exist in the credential cache, [**GetCredential**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-getcredential) creates a new credential object with empty user name and password values.

-   To set the user name and password on the credential object, call [**IMFNetCredential::SetUser**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredential-setuser) and [**IMFNetCredential::SetPassword**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredential-setpassword).
-   To set the caching options on the credential object, call [**IMFNetCredentialCache::SetUserOptions**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions).

    ```C++
    hr = pCredentialCache-> SetUserOptions( 
            pCredentialCache,
            MFNET_CREDENTIAL_SAVE);
    ```

    

    The *dwOptionsFlags* parameter values are defined in the [**MFNetCredentialOptions**](/windows/desktop/api/mfidl/ne-mfidl-mfnetcredentialoptions) enumeration. To save user credentials for a URL in a persistent storage, set the MFNET\_CREDENTIAL\_SAVE flag. If the [**SetUserOptions**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions) call completes successfully, then the subsequent call to [**GetCredential**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-getcredential) searches for the credentials in the persistent storage. If a match is found, this method returns a pointer to the credential object that contains the information.

    By default, user credentials sent over the network are encrypted. To change this to clear text, set the MFNET\_CREDENTIAL\_ALLOW\_CLEAR\_TEXT flag.

    To remove information from the registry, call [**GetCredential**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-getcredential) to get the credential object, and then call [**SetUserOption**](/windows/desktop/api/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions) and set *dwOptionsFlags* to MFNET\_CREDENTIAL\_DONT\_CACHE.

## Related topics

<dl> <dt>

[Network Source Authentication](network-source-authentication.md)
</dt> </dl>

 

 



