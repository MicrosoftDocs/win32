---
title: IADsDeleteOps Interface
description: The IADsDeleteOps interface is used in supervisory and maintenance routines for the underlying directory store. It can delete leaf objects and entire subtrees in a single operation.
ms.assetid: 821b71c2-e9f5-4ca8-9366-e8a3f1907670
ms.tgt_platform: multiple
keywords:
- IADsDeleteOps Interface ADSI
- IADsDeleteOps ADSI , using
- ADSI ADSI , example code C/C++ , using IADsDeleteOps to delete entire groups
ms.topic: article
ms.date: 05/31/2018
---

# IADsDeleteOps Interface

The [**IADsDeleteOps**](/windows/desktop/api/Iads/nn-iads-iadsdeleteops) interface is used in supervisory and maintenance routines for the underlying directory store. It can delete leaf objects and entire subtrees in a single operation.

If this interface were not supported, deleting an object from Active Directory would require that each contained object be recursively enumerated and deleted. With this interface, any container object, with all its contained objects and subobjects, can be deleted with a single operation.

The following code example deletes the "Eng" container and all child objects.


```C++
HRESULT hr;
IADsDeleteOps *pDeleteOps;
LPWSTR pwszUsername = NULL;
LPWSTR pwszPassword = NULL;

// Insert code to securely retrieve the pwszUsername and pwszPassword
// or leave as NULL to use the default security context of the 
// calling application.
 
// Bind to the LDAP provider.
hr = ADsOpenObject(L"LDAP://CN=Eng,CN=Users,DC=Fabrikam,DC=Com", 
    pwszUsername,
    pwszPassword,
    0,
    ADS_SECURE_AUTHENTICATION,
    IID_IADsDeleteOps, 
    (void**)&pDeleteOps);
if(S_OK == hr)
{
    // Delete the container and all child objects.
    pDeleteOps->DeleteObject(0);

    // Release the interface.
    pDeleteOps->Release();
}

if(pwszUsername)
{
    SecureZeroMemory(pwszUsername, lstrlen(pwszUsername) * sizeof(TCHAR));
}
if(pwszPassword)
{
    SecureZeroMemory(pwszPassword, lstrlen(pwszPassword) * sizeof(TCHAR));
}
```



The following code example deletes the "Eng" container and all child objects.


```VB
Dim DeleteOps As IADsDeleteOps

' Bind to the LDAP provider.
Set DeleteOps = GetObject("LDAP://CN=Eng,CN=Users,DC=Fabrikam,DC=Com")

' Delete the container and all child objects.
DeleteOps.DeleteObject (0)
```



 

 




