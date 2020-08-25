---
title: Retrieving an Object's DACL
description: An object's security descriptor may contain a discretionary access-control list (DACL).
ms.assetid: 93b16094-9923-4886-804f-4e989fbf6977
ms.tgt_platform: multiple
keywords:
- DACL AD
- DACL AD ,retrieving an object's DACL
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Object's DACL

An object's security descriptor may contain a discretionary access-control list (DACL). A DACL contains zero or more access-control entries (ACEs) that identify the users and groups who can access the object. If a DACL is empty (that is, it contains zero ACEs), no access is explicitly granted, so access is implicitly denied. However, if an object's security descriptor does not have a DACL, the object is unprotected and everyone has complete access.

To retrieve an object's DACL, you must be the object's owner or have **READ\_CONTROL** access to the object.

To get and set the DACL of a directory object, use the [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface. Using C++, the [**IADsSecurityDescriptor::get\_DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method returns an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) interface, and use the methods on that interface to access the individual ACEs in the DACL. The procedure for modifying a DACL is described in [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

To enumerate the ACEs, use the [**IADsAccessControlList::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-get__newenum) method. The method returns an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface. Use the [**IEnumVARIANT::Next**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-next) method to enumerate the ACEs in the ACL. Each ACE is returned as a **VARIANT** containing an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer (the **vt** member is **VT\_DISPATCH**). Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface for the ACE. You can use the methods of the **IADsAccessControlEntry** interface to set or retrieve the components of an ACE.

For more information about DACLs and ACEs, see the following topics in the Platform Software Development Kit (SDK).

-   [Access-Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists)
-   [Access-Control Entries (ACEs)](/windows/desktop/SecAuthZ/access-control-entries)

 

 