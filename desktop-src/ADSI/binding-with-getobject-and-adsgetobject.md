---
title: Binding With GetObject and ADsGetObject
description: The GetObject and ADsGetObject functions are used to bind to directory service objects with no authentication.
ms.assetid: 15d8116a-8ec1-48b5-bf62-411fdff7c8b8
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,using,binding with GetObject and ADsGetObject
ms.topic: article
ms.date: 05/31/2018
---

# Binding With GetObject and ADsGetObject

The **GetObject** and [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) functions are used to bind to directory service objects with no authentication. The application is not required to provide credentials when accessing directory service data. ADSI uses the security context of the calling thread. However, if secure authentication fails, ADSI attempts to perform a simple bind with a null user name and null password. If the simple bind succeeds, the user context for the binding is Guest. A simple bind uses plaintext authentication. Because no user name or password is transmitted over the network, this is not a security issue.

The **GetObject** function is used to bind to directory service objects in languages that support automation, such as Visual Basic. The **GetObject** function requires a moniker string. In ADSI, the binding string is the moniker string.

In languages that do not directly support automation, such as C or C++, ADSI provides the [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) function to bind to directory service objects. Alternatively, the [**MkParseDisplayName**](/windows/win32/api/objbase/nf-objbase-mkparsedisplayname) and [**MkParseDisplayNameEx**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775113(v=vs.85)) functions can be used to achieve the same result as **GetObject**.

For a service running under the LocalSystem account, the security context used by **GetObject** and [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) depends on the computer on which the service is running. If the service is running as LocalSystem on a domain controller, the service has full system-level access to Active Directory. If the service is not running on a DC, the service has the access rights and privileges granted to the computer account for the computer on which the service is running; this is significantly less powerful than system-level access.

## Examples

The following Visual Basic code example shows how to use the **GetObject** function to bind to an object.


```VB
Dim myUser as IADs
Set myUser = GetObject("LDAP://CN=jeffsmith,DC=fabrikam,DC=com")
```



The following C++ code example shows how to use the [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) function to bind to an object.


```C++
IADs *pObject;
HRESULT hr;

// Initialize COM.
CoInitialize(NULL);

hr = ADsGetObject(L"LDAP://CN=jeffsmith,DC=fabrikam,DC=com", 
        IID_IADs,
        (void**) &pObject);

if(SUCCEEDED(hr))
{
    // Use the object.

    // Release the object.
    pObject->Release()
}

// Uninitialize COM.
CoUninitialize();
```



 

 