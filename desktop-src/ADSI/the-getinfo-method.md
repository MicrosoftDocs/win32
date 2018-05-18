---
title: The GetInfo Method
description: The IADs GetInfo method loads all of the attribute values for an ADSI object into the local cache from the underlying directory service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b29f1156-7c38-4f5a-a88c-578ae6167758'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["GetInfo ADSI , using IADs GetInfo", "ADSI ADSI ,using,using the IADs GetInfo method"]
---

# The GetInfo Method

The [**IADs::GetInfo**](iads-getinfo.md) method loads all of the attribute values for an ADSI object into the local cache from the underlying directory service. The [**IADs::GetInfoEx**](iads-getinfoex.md) method is used to load specific attribute values into the local cache. For more information about using the **IADs::GetInfoEx** method, see [Optimization Using GetInfoEx](optimization-using-getinfoex.md).

ADSI will make an implicit [**IADs::GetInfo**](iads-getinfo.md) call when the [**IADs::Get**](iads-get.md) or [**IADs::GetEx**](iads-getex.md) method is called for a specific attribute and no value is found in the local cache. When **IADs::GetInfo** has been called, an implicit call is not repeated. If a value already exists in the property cache, however, calling the **IADs::Get** or **IADs::GetEx** method without first calling **IADs::GetInfo** will retrieve the cached value rather than the most current value from the underlying directory. This can cause updated attribute values to be overwritten if the local cache has been modified but the values have not been committed to the underlying directory service with a call to the [**IADs::SetInfo**](iads-setinfo.md) method. To avoid caching problems, commit attribute value changes by calling **IADs::SetInfo** before calling **IADs::GetInfo**.


```VB
Dim usr As IADs

' Bind to a specific user object.
Set usr = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
 
' This code example assumes that the property description has a single value in the directory.
' Be aware that this will IMPLICITLY call GetInfo because at this point GetInfo
' has not yet been called (implicitly or explicitly) on the usr object.
Debug.Print "User's title is " + usr.Get("title")

' Change the attribute value in the local cache.
usr.Put "title", "Vice President"
Debug.Print "User's title is " + usr.Get("title")

' Call GetInfo, which will overwrite the updated value because SetInfo has not 
' been called.
usr.GetInfo
Debug.Print "User's title is " + usr.Get("title")
```



Some directory services do not return all attribute values for an object in response to a [**IADs::GetInfo**](iads-getinfo.md) call. In these cases, use the [**IADs::GetInfoEx**](iads-getinfoex.md) method to load these values into the local cache.

 

 




