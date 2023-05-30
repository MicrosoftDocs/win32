---
title: Binding With ADsOpenObject and IADsOpenDSObject OpenDSObject
description: The ADsOpenObject function and the IADsOpenDSObject OpenDSObject method are used to bind to directory service objects when alternate credentials must be specified and when data encryption is required.
ms.assetid: 7b8ded11-e04f-40f5-a82a-5972c4df9dea
ms.tgt_platform: multiple
keywords:
- Binding With ADsOpenObject and IADsOpenDSObject OpenDSObject ADSI
- ADSI ADSI , using, binding with ADsOpenObject and IADsOpenDSObject OpenDSObject
ms.topic: article
ms.date: 03/17/2023
---

# Binding With ADsOpenObject and IADsOpenDSObject::OpenDSObject

The [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function and the [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method are used to bind to directory service objects when alternate credentials must be specified and when data encryption is required.

The credentials of the calling thread should be used when possible. However, if alternate credentials must be used, the [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function or the [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method must be used. If alternate credentials are used, it is important to not cache the password. Multiple bind operations can be performed by specifying the user name and password for the first bind operation and then specifying only the user name in subsequent binds. The system sets up a session on the first call and uses the same session on subsequent bind calls as long as the following conditions are met:

- The same user name in each bind operation.
- Implement serverless binding or bind to the same server in each bind operation.
- Maintain an open session by holding on to an object reference from one of the bind operations. The session is closed when the last object reference is released.

[ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) and [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) use the Windows NT [Security Support Provider Interfaces (SSPI)](/windows/win32/SecAuthN/sspi) to allow flexibility in authentication options. The major advantage of using these interfaces is to provide different types of authentication to Active Directory clients and to encrypt the session. Currently, ADSI does not allow certificates to be passed in. Therefore, you can use SSL for encryption and then Kerberos, NTLM, or simple authentication, depending on how the flags are set on the *dwReserved* parameter.

You cannot request a specific SSPI provider in ADSI, although you always get the highest preference protocol. In the case of a Windows client binding to a computer running Windows, the protocol is Kerberos. Not allowing a certificate for authentication is acceptable in the case of a webpage because authentication occurs prior to running the webpage.

Although Open operations allow you to specify a user and password, you should not do so. Instead, do not specify any credentials and implicitly use the credentials of the caller's security context. To bind to a directory object using the caller's credentials with [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) or [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject), specify `NULL` for both user name and password.

Finally, to bind with no authentication, use the **ADS\_NO\_AUTHENTICATION** flag. No authentication indicates that ADSI attempts to bind as an anonymous user to the target object and performs no authentication. This is equivalent to requesting anonymous binding in LDAP and indicates that all users are included in the security context.

If the authentication flags are set to zero, ADSI performs a simple bind, sent as plaintext.

> [!CAUTION]
> If a user name and password are specified without specifying authentication flags, the user name and password are transmitted over the network in plaintext, which is a security risk. Do not specify a user name and password without specifying authentication flags.

## Examples

The following Visual Basic code example shows how to use the [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method.

```VB
Const ADS_SECURE_AUTHENTICATION = 1
Dim openDS As IADsOpenDSObject
Dim usr As IADsUser
 
Set openDS = GetObject("LDAP:")
 
openDS.OpenDSObject("LDAP://CN=jeffsmith,DC=fabrikam,DC=com",
    vbNullString, 
    vbNullString,
    ADS_SECURE_AUTHENTICATION)
```

The following C++ code example shows how to use the [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function.

```C++
IADs *pObject;
HRESULT hr;

hr = ADsOpenObject(L"LDAP://CN=jeffsmith,DC=fabrikam,DC=com",
    NULL, 
    NULL,
    ADS_SECURE_AUTHENTICATION, 
    IID_IADs,
    (void**)&pObject);
if(SUCCEEDED(hr))
{
    // Use the object.

    // Release the object.
    pObject->Release()
}
```

The [IADsOpenDSObject](/windows/win32/api/Iads/nn-iads-iadsopendsobject) interface can also be used in C++, but it duplicates the [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function.

The following C++ code example shows how to use the [IADsOpenDSObject](/windows/win32/api/Iads/nn-iads-iadsopendsobject) interface to perform the same bind operation as in the code example above.

```C++
IADsOpenDSObject *pDSO;
HRESULT hr;
 
hr = ADsGetObject(L"LDAP:", IID_IADsOpenDSObject, (void**)&pDSO);
if(SUCCEEDED(hr))
{
    IDispatch *pDisp;

    hr = pDSO->OpenDSObject(CComBSTR("LDAP://CN=jeffsmith,DC=fabrikam,DC=com"),
        NULL,
        NULL,
        ADS_SECURE_AUTHENTICATION, 
        &pDisp);
    if(SUCCEEDED(hr))
    {
        IADs *pObject;

        hr = pDisp->QueryInterface(IID_IADs, (void**) &pObject);
        if(SUCCEEDED(hr))
        {
            // Use the object.

            // Release the object.
            pObject->Release();
        }

        pDisp->Release();
    }
    
    pDSO->Release();
}
```

## See also

[ADS_AUTHENTICATION_ENUM examples](/windows/win32/api/iads/ne-iads-ads_authentication_enum#examples)

[IADsOpenDSObject](/windows/win32/api/Iads/nn-iads-iadsopendsobject)

[ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject)
