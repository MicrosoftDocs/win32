---
title: Retrieving an Object's SACL
description: The security descriptor of an object in Active Directory Domain Services may contain a system access-control list (SACL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b1da91a2-d9b0-48a3-9de5-1e588209032d
ms.tgt_platform: multiple
keywords:
- SACL AD
- SACL AD ,retrieving an object's SACL
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Object's SACL

The security descriptor of an object in Active Directory Domain Services may contain a system access-control list (SACL). A SACL contains access-control entries (ACEs) that specify the types of access attempts that generate audit records in the security event log of a domain controller. Be aware that a SACL generates log entries only on the domain controller where the access attempt occurred, not on every DC that contains a replica of the object.

To set or get the SACL from an object security descriptor, the **SE\_SECURITY\_NAME** privilege must be enabled in the access token of the requesting thread. The administrators group has this privilege by default, and it can be assigned to other users or groups. For more information, see [SACL Access Right](https://msdn.microsoft.com/library/windows/desktop/aa379321).

To get and set the SACL of a directory object, use the [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) interface. Using C++, the [**IADsSecurityDescriptor::get\_SystemAcl**](https://msdn.microsoft.com/library/aa706131) method returns an [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](https://msdn.microsoft.com/library/aa705953) interface, and use the methods on that interface to access the individual ACEs in the SACL. For more information about the procedure for modifying a SACL, which is similar to that for modifying a DACL, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

To enumerate the ACEs in a SACL, use the [**IADsAccessControlList::get\_\_NewEnum**](https://msdn.microsoft.com/library/aa705956) method, which returns an [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface. Use the [**IEnumVARIANT::Next**](https://msdn.microsoft.com/en-us/library/ms221369(v=VS.71).aspx) method to enumerate the ACEs in the ACL. Each ACE is returned as a **VARIANT** that contains an [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) pointer; be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interface for the ACE. Use the **IADsAccessControlEntry** interface methods to set or get the components of an ACE.

For more information about SACLs, see:

-   [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/windows/desktop/aa374872)
-   [Audit Generation](https://msdn.microsoft.com/library/windows/desktop/aa375723)

 

 




