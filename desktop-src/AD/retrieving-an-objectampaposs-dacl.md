---
title: Retrieving an Object's DACL
description: An object's security descriptor may contain a discretionary access-control list (DACL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 93b16094-9923-4886-804f-4e989fbf6977
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- DACL AD
- DACL AD ,retrieving an object's DACL
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Object's DACL

An object's security descriptor may contain a discretionary access-control list (DACL). A DACL contains zero or more access-control entries (ACEs) that identify the users and groups who can access the object. If a DACL is empty (that is, it contains zero ACEs), no access is explicitly granted, so access is implicitly denied. However, if an object's security descriptor does not have a DACL, the object is unprotected and everyone has complete access.

To retrieve an object's DACL, you must be the object's owner or have **READ\_CONTROL** access to the object.

To get and set the DACL of a directory object, use the [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) interface. Using C++, the [**IADsSecurityDescriptor::get\_DiscretionaryAcl**](https://msdn.microsoft.com/library/aa706131) method returns an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](https://msdn.microsoft.com/library/aa705953) interface, and use the methods on that interface to access the individual ACEs in the DACL. The procedure for modifying a DACL is described in [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

To enumerate the ACEs, use the [**IADsAccessControlList::get\_\_NewEnum**](https://msdn.microsoft.com/library/aa705956) method. The method returns an [**IUnknown**](33f1d79a-33fc-4ce5-a372-e08bda378332) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](https://msdn.microsoft.com/windows/desktop/139e3c93-faef-4003-9079-e0e94494db3e) interface. Use the [**IEnumVARIANT::Next**](https://msdn.microsoft.com/windows/desktop/691c1624-8d01-41e0-890e-a4782eba1f59) method to enumerate the ACEs in the ACL. Each ACE is returned as a **VARIANT** containing an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) pointer (the **vt** member is **VT\_DISPATCH**). Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interface for the ACE. You can use the methods of the **IADsAccessControlEntry** interface to set or retrieve the components of an ACE.

For more information about DACLs and ACEs, see the following topics in the Platform Software Development Kit (SDK).

-   [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/windows/desktop/aa374872)
-   [Access-Control Entries (ACEs)](https://msdn.microsoft.com/library/windows/desktop/aa374868)

 

 




