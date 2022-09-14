---
title: Retrieving an Object's SACL
description: The security descriptor of an object in Active Directory Domain Services may contain a system access-control list (SACL).
ms.assetid: b1da91a2-d9b0-48a3-9de5-1e588209032d
ms.tgt_platform: multiple
keywords:
- SACL AD
- SACL AD ,retrieving an object's SACL
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Object's SACL

The security descriptor of an object in Active Directory Domain Services may contain a system access-control list (SACL). A SACL contains access-control entries (ACEs) that specify the types of access attempts that generate audit records in the security event log of a domain controller. Be aware that a SACL generates log entries only on the domain controller where the access attempt occurred, not on every DC that contains a replica of the object.

To set or get the SACL from an object security descriptor, the **SE\_SECURITY\_NAME** privilege must be enabled in the access token of the requesting thread. The administrators group has this privilege by default, and it can be assigned to other users or groups. For more information, see [SACL Access Right](/windows/desktop/SecAuthZ/sacl-access-right).

To get and set the SACL of a directory object, use the [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface. Using C++, the [**IADsSecurityDescriptor::get\_SystemAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) method returns an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist) interface, and use the methods on that interface to access the individual ACEs in the SACL. For more information about the procedure for modifying a SACL, which is similar to that for modifying a DACL, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

To enumerate the ACEs in a SACL, use the [**IADsAccessControlList::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadsaccesscontrollist-get__newenum) method, which returns an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer. Call **QueryInterface** on that **IUnknown** pointer to get an [**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface. Use the [**IEnumVARIANT::Next**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-next) method to enumerate the ACEs in the ACL. Each ACE is returned as a **VARIANT** that contains an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer; be aware that the **vt** member is **VT\_DISPATCH**. Call **QueryInterface** on that **IDispatch** pointer to get an [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interface for the ACE. Use the **IADsAccessControlEntry** interface methods to set or get the components of an ACE.

For more information about SACLs, see:

-   [Access-Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists)
-   [Audit Generation](/windows/desktop/SecAuthZ/audit-generation)

 

 