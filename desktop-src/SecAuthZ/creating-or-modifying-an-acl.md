---
Description: 'Windows supports a set of functions that create an access control list (ACL) or modify the access control entries (ACEs) in an existing ACL.'
ms.assetid: '71301aab-1040-4f61-855f-2b891c8b6077'
title: Creating or Modifying an ACL
---

# Creating or Modifying an ACL

Windows supports a set of functions that create an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) or modify the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an existing ACL.

The [**SetEntriesInAcl**](setentriesinacl.md) function creates a new ACL. **SetEntriesInAcl** can specify a completely new set of ACEs for the ACL, or it can merge one or more new ACEs with the ACEs of an existing ACL. The **SetEntriesInAcl** function uses an array of [**EXPLICIT\_ACCESS**](explicit-access.md) structures to specify the information for the new ACEs. Each **EXPLICIT\_ACCESS** structure contains information that describes a single ACE. This information includes the access rights, the type of ACE, the flags that control ACE inheritance, and a [**TRUSTEE**](trustee.md) structure that identifies the trustee.

**To add a new ACE to an existing ACL**

1.  Use the [**GetSecurityInfo**](getsecurityinfo.md) or [**GetNamedSecurityInfo**](getnamedsecurityinfo.md) function to get the existing DACL or SACL from an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly).
2.  For each new ACE, call the [**BuildExplicitAccessWithName**](buildexplicitaccesswithname.md) function to fill an [**EXPLICIT\_ACCESS**](explicit-access.md) structure with the information that describes the ACE.
3.  Call [**SetEntriesInAcl**](setentriesinacl.md), specifying the existing ACL and an array of [**EXPLICIT\_ACCESS**](explicit-access.md) structures for the new ACEs. The **SetEntriesInAcl** function allocates and initializes the ACL and its ACEs.
4.  Call the [**SetSecurityInfo**](setsecurityinfo.md) or [**SetNamedSecurityInfo**](setnamedsecurityinfo.md) function to attach the new ACL to the object's security descriptor.

If the caller specifies an existing ACL, [**SetEntriesInAcl**](setentriesinacl.md) merges the new ACE information with the existing ACEs in the ACL. Consider the case, for example, in which the existing ACL grants access to a specified trustee and an [**EXPLICIT\_ACCESS**](explicit-access.md) structure denies access to the same trustee. In this case, **SetEntriesInAcl** adds a new access-denied ACE for the trustee and deletes or modifies the existing access-allowed ACE for the trustee.

For sample code that merges a new ACE into an existing ACL, see [Modifying the ACLs of an Object in C++](modifying-the-acls-of-an-object-in-c--.md).

 

 



