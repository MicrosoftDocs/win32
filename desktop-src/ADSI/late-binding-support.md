---
title: Late Binding Support
description: When late binding support is in place, each function call must go through the ADSI IDispatch interface, before it is rerouted to the appropriate extension.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fbdc6234-9381-4d64-bf02-05e393b3e0bd
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- extensions ADSI ,late binding support
- ADSI ADSI ,example code Visual Basic ,late binding support
- binding AD ,late binding support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Late Binding Support

When late binding support is in place, each function call must go through the ADSI [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface, before it is rerouted to the appropriate extension.

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



There are no explicit calls to the **QueryInterface** method to get to the extensions. The extensions must reroute their [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) calls to the ADSI **IDispatch** interface. ADSI makes the decision and resolves any conflicts that occur, then it re-routes back to the appropriate extension using an interface called [**IADsExtension**](/windows/win32/Iads/nn-iads-iadsextension?branch=master). Therefore, any extension that supports late binding must implement **IADsExtension**.

 

 




