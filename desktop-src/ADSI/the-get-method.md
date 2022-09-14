---
title: The Get Method
description: The IADs Get method is used to retrieve individual named attributes from a directory object.
ms.assetid: e3754663-fe31-46f3-9dc1-a9c96ed53fde
ms.tgt_platform: multiple
keywords:
- Get ADSI , using IADs Get
- ADSI ADSI ,using,using the IADs Get method
ms.topic: article
ms.date: 05/31/2018
---

# The Get Method

The [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) method is used to retrieve individual named attributes from a directory object.

The following code example uses the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) method to retrieve a named attribute from an object.


```VB
Dim MyUser as IADs
Dim MyDistinguishedName as String

On Error GoTo Cleanup
 
' Bind to a specific user object.
set MyUser = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
 
' Get property.
MyDistinguishedName = MyUser.Get("distinguishedName")

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set MyUser = Nothing
```



In Automation languages, named attributes can also be accessed directly using the dot notation. For example, **object.Get("distinguishedName")** is identical to **object.distinguishedName**.

The following code example is identical to the previous example except that the **distinguishedName** attribute is accessed using the dot notation.


```VB
Dim MyUser as IADs
Dim MyDistinguishedName as String

On Error GoTo Cleanup
 
' Bind to a specific user object.
set MyUser = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
 
' Get property.
MyDistinguishedName = MyUser.distinguishedName

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set MyUser = Nothing
```



If a value is not set on the object, the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) method will return the error "Property not found in cache".

 

 




