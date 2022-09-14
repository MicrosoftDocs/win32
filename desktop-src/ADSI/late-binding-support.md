---
title: Late Binding Support
description: When late binding support is in place, each function call must go through the ADSI IDispatch interface, before it is rerouted to the appropriate extension.
ms.assetid: fbdc6234-9381-4d64-bf02-05e393b3e0bd
ms.tgt_platform: multiple
keywords:
- extensions ADSI ,late binding support
- ADSI ADSI ,example code Visual Basic ,late binding support
- binding AD ,late binding support
ms.topic: article
ms.date: 05/31/2018
---

# Late Binding Support

When late binding support is in place, each function call must go through the ADSI [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface, before it is rerouted to the appropriate extension.

Consider the following code example.


```C++
Set x = GetObject("LDAP://CN=JeffSmith, OU=Sales, 
                   DC=Fabrikam,DC=COM")
x.SetPassword("newPassword")
 
 
x.MyNewMethod( "\\srv\public")
x.MyProperty = "Hello World"
 
x.OtherMethod()
x.OtherProperty = 4362
 
Debug.Print x.LastName
```



There are no explicit calls to the **QueryInterface** method to get to the extensions. The extensions must reroute their [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) calls to the ADSI **IDispatch** interface. ADSI makes the decision and resolves any conflicts that occur, then it re-routes back to the appropriate extension using an interface called [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension). Therefore, any extension that supports late binding must implement **IADsExtension**.

 

 