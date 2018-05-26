---
Description: Using the Credential Cache
ms.assetid: b58d0a6e-ecae-48a1-a3af-d4246caa272b
title: Using the Credential Cache
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Credential Cache

Media Foundation provides a default implementation of the [**IMFNetCredentialCache**](/windows/win32/mfidl/nn-mfidl-imfnetcredentialcache?branch=master) interface. An application that implements the [**IMFNetCredentialManager**](/windows/win32/mfidl/nn-mfidl-imfnetcredentialmanager?branch=master) interface can use the default credential cache object to store the user's credentials.

To create the default credential cache object, call the [**MFCreateCredentialCache**](/windows/win32/mfidl/nf-mfidl-mfcreatecredentialcache?branch=master) function.


```C++
HRESULT hr = S_OK;
IMFNetCredentialCache *pCredentialCache = NULL;
hr = MFCreateCredentialCache(&amp;pCredentialCache);
```



After the credential cache is created, the application can use the following methods to get a credential object, set user credentials, and specify the caching options.

-   To get the credential object for a URL, call [**IMFNetCredentialCache::GetCredential**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-getcredential?branch=master).

    ```C++
    hr = pCredentialCache-> GetCredential(
            pszUrl,
            pszRealm,
            dwAuthenticationFlags,
            &amp;pCredential,
            &amp;dwRequirementsFlags);
    ```

    

    If the credentials for the specified URL do not exist in the credential cache, [**GetCredential**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-getcredential?branch=master) creates a new credential object with empty user name and password values.

-   To set the user name and password on the credential object, call [**IMFNetCredential::SetUser**](/windows/win32/mfidl/nf-mfidl-imfnetcredential-setuser?branch=master) and [**IMFNetCredential::SetPassword**](/windows/win32/mfidl/nf-mfidl-imfnetcredential-setpassword?branch=master).
-   To set the caching options on the credential object, call [**IMFNetCredentialCache::SetUserOptions**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions?branch=master).

    ```C++
    hr = pCredentialCache-> SetUserOptions( 
            pCredentialCache,
            MFNET_CREDENTIAL_SAVE);
    ```

    

    The *dwOptionsFlags* parameter values are defined in the [**MFNetCredentialOptions**](/windows/win32/mfidl/ne-mfidl-_mfnetcredentialoptions?branch=master) enumeration. To save user credentials for a URL in a persistent storage, set the MFNET\_CREDENTIAL\_SAVE flag. If the [**SetUserOptions**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions?branch=master) call completes successfully, then the subsequent call to [**GetCredential**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-getcredential?branch=master) searches for the credentials in the persistent storage. If a match is found, this method returns a pointer to the credential object that contains the information.

    By default, user credentials sent over the network are encrypted. To change this to clear text, set the MFNET\_CREDENTIAL\_ALLOW\_CLEAR\_TEXT flag.

    To remove information from the registry, call [**GetCredential**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-getcredential?branch=master) to get the credential object, and then call [**SetUserOption**](/windows/win32/mfidl/nf-mfidl-imfnetcredentialcache-setuseroptions?branch=master) and set *dwOptionsFlags* to MFNET\_CREDENTIAL\_DONT\_CACHE.

## Related topics

<dl> <dt>

[Network Source Authentication](network-source-authentication.md)
</dt> </dl>

 

 



