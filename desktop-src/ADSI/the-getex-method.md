---
title: The GetEx Method
description: Some attributes can store one or more values.
ms.assetid: aaa5fa90-7e60-4668-bd23-1475c2e4d184
ms.tgt_platform: multiple
keywords:
- GetEx ADSI , using IADs GetEx
- ADSI ADSI ,using,using the IADs GetEx method
ms.topic: article
ms.date: 05/31/2018
---

# The GetEx Method

Some attributes can store one or more values. For example, the **otherTelephone** attribute of a user object in Active Directory is a property that can have zero, one, or many values. Attributes that have multiple values are known as "multi-valued attributes". If the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) method is used to retrieve a multi-valued attribute, the results must be processed differently than if the attribute has a single value. The results provided by the [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) method, however, are processed in the same manner, regardless if the attribute has a single or multiple values. In both cases, the **IADs::GetEx** method returns the values in an array.

The [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) method retrieves properties from the property cache. If the specified property is not found in the cache, **IADs::GetEx** performs an implicit [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) call.

The [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) method returns a variant array of variants regardless of the number of values returned from the server. This is true even if the attribute only contains one value.


```VB
Dim usr As IADs
On Error GoTo Cleanup

Set usr = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
homePhones = usr.GetEx("otherHomePhone")
For each phone in homePhones
    Debug.Print phone
Next

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set usr = Nothing
```



The [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) method can also be used for single-valued attributes. The results of a single-valued attribute are processed the same as the results for a multi-valued attribute.


```VB
Dim usr as IADs
On Error GoTo Cleanup

Set usr = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
sds = usr.GetEx("ntSecurityDescriptor")
For each sd in sds
    Set acl = sd.DiscretionaryACL
Next

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set usr = Nothing
```



If no value is set for the attribute, [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) returns the error "Property not found in cache".

 

 




