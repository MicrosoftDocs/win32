---
title: Optimization Using GetInfoEx
description: Used to load specific attribute values into the local cache from the underlying directory service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e6111957-22cb-4473-9814-5bcbc79583b2
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Optimization Using GetInfoEx ADSI
- GetInfoEx ADSI , Optimization Using IADs GetInfoEx
- ADSI ADSI , Using, Optimization Using the IADs GetInfoEx Method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Optimization Using GetInfoEx

The [**IADs.GetInfoEx**](/windows/win32/Iads/nf-iads-iads-getinfoex?branch=master) method is used to load specific attribute values into the local cache from the underlying directory service. This method only loads the specified attribute values into the local cache. The [**IADs.GetInfo**](/windows/win32/Iads/nf-iads-iads-getinfo?branch=master) method is used to load all attribute values into the local cache.

The [**IADs.GetInfoEx**](/windows/win32/Iads/nf-iads-iads-getinfoex?branch=master) method gets specific current values for the properties of an Active Directory object from the underlying directory store, refreshing the cached values.

If a value already exists in the property cache, however, calling the [**IADs.Get**](/windows/win32/Iads/nf-iads-iads-get?branch=master) or [**IADs.GetEx**](/windows/win32/Iads/nf-iads-iads-getex?branch=master) method without first calling [**IADs.GetInfoEx**](/windows/win32/Iads/nf-iads-iads-getinfoex?branch=master) for that attribute will retrieve the cached value rather than the most current value from the underlying directory. This can cause updated attribute values to be overwritten if the local cache has been modified, but the values have not been committed to the underlying directory service with a call to the [**IADs.SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master) method. The suggested method for avoiding caching problems is to always commit attribute value changes by calling **IADs.SetInfo** before calling [**IADs.GetInfo**](/windows/win32/Iads/nf-iads-iads-getinfo?branch=master).


```VB
Dim usr As IADs
Dim PropArray As Variant

On Error GoTo Cleanup

' Bind to a specific user object.
Set usr = GetObject("LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
 
' The code example assumes that the property description has a single value in the directory.
' Be aware that this will implicitly call GetInfo because, at this point, GetInfo
' has not yet been called (implicitly or explicitly) on the usr object.
Debug.Print "User's common name is " + usr.Get("cn")
Debug.Print "User's title is " + usr.Get("title")
Debug.Print "User's department is " + usr.Get("department")

' Change two of the attribute values in the local cache.
usr.Put "cn", "Jeff Smith"
usr.Put "title", "Vice President"
usr.Put "department", "Head Office"
Debug.Print "User's common name is " + usr.Get("cn")
Debug.Print "User's title is " + usr.Get("title")
Debug.Print "User's department is " + usr.Get("department")

' Initialize the array of properties to pass to GetInfoEx.
PropArray = Array("department", "title")
 
' Get the specified attribute values.
usr.GetInfoEx PropArray, 0

' The specific attributes values were overwritten, but the attribute
' value not retrieved has not changed.
Debug.Print "User's common name is " + usr.Get("cn")
Debug.Print "User's title is " + usr.Get("title")
Debug.Print "User's department is " + usr.Get("department")

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set usr = Nothing
```



## Retrieving Active Directory Constructed Attributes

In Active Directory, most of the constructed attributes are retrieved and cached when the [**IADs.GetInfo**](/windows/win32/Iads/nf-iads-iads-getinfo?branch=master) method is called ([**IADs.Get**](/windows/win32/Iads/nf-iads-iads-get?branch=master) performs an implicit **IADs.GetInfo** call if the cache is empty). Some constructed attributes, however, are not automatically retrieved and cached and, therefore, require that the [**IADs.GetInfoEx**](/windows/win32/Iads/nf-iads-iads-getinfoex?branch=master) method be called explicitly to retrieve them. For example, in Active Directory, the [**canonicalName**](https://msdn.microsoft.com/library/ms675436) attribute is not retrieved when the **IADs.GetInfo** method is called and **IADs.Get** will return **E\_ADS\_PROPERTY\_NOT\_FOUND**. The **IADs.GetInfoEx** method must be called to retrieve the **canonicalName** attribute. These same constructed attributes will also not be retrieved using the [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master) interface to enumerate the attributes.

For more information and a code example that shows how to retrieve all attribute values, see [Example Code for Reading a Constructed Attribute](example-code-for-reading-a-constructed-attribute.md).

 

 




