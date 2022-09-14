---
title: The PutEx Method
description: The IADs PutEx method uses the name of a property to save a property with single or multiple values into the property cache.
ms.assetid: fb9a0610-e955-424b-a2b9-da4986d0ba5f
ms.tgt_platform: multiple
keywords:
- PutEx ADSI ,about
- ADSI ADSI ,example code Visual Basic ,using the PutEx method
- properties ADSI ,saving a single or multi-valued property to property cache
ms.topic: article
ms.date: 05/31/2018
---

# The PutEx Method

The [**IADs::PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method uses the name of a property to save a property with single or multiple values into the property cache. This overwrites any value currently in the property cache. The values in the cache are not written to the underlying directory service until an [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) occurs. The first argument of **PutEx** indicates whether you want to replace or add to any existing values for the property. In the following example, any existing values of the **description** attribute are erased in the cache when **PutEx** is called, and erased on the server when **SetInfo** is called.


```VB
Dim x As IADs
Set x = GetObject("LDAP://CN=Administrator,CN=Users,DC=Fabrikam,DC=com")
'----------------------------------------------
' Assume the otherHomePhoneNumber has the following values:
' 111-1111, 222-2222
'----------------------------------------------
x.PutEx ADS_PROPERTY_APPEND, "OtherhomePhone", Array("333-3333" )  
x.SetInfo              'Now the values are 111-1111,222-222,333-3333.
 
x.PutEx ADS_PROPERTY_DELETE, "OtherHomePhone", Array("111-1111", "222-2222")
x.SetInfo              'Now the values are 333-3333.
x.PutEx ADS_PROPERTY_UPDATE, "OtherHomePhone", Array("888-8888", "999-9999")
x.SetInfo              'Now the values are 888-8888,999-9999.
x.PutEx ADS_PROPERTY_CLEAR, "OtherHomePhone",  vbNull
x.SetInfo              'Now the property has no value.
```



 

 




