---
description: Windows supports a set of functions that create an access control list (ACL) or modify the access control entries (ACEs) in an existing ACL.
ms.assetid: 71301aab-1040-4f61-855f-2b891c8b6077
title: Creating or Modifying an ACL
ms.topic: article
ms.date: 05/31/2018
---

# Creating or Modifying an ACL

Windows supports a set of functions that create an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL) or modify the [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) in an existing ACL.

The [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) function creates a new ACL. **SetEntriesInAcl** can specify a completely new set of ACEs for the ACL, or it can merge one or more new ACEs with the ACEs of an existing ACL. The **SetEntriesInAcl** function uses an array of [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structures to specify the information for the new ACEs. Each **EXPLICIT\_ACCESS** structure contains information that describes a single ACE. This information includes the access rights, the type of ACE, the flags that control ACE inheritance, and a [**TRUSTEE**](/windows/desktop/api/AccCtrl/ns-accctrl-trustee_a) structure that identifies the trustee.

**To add a new ACE to an existing ACL**

1.  Use the [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo) or [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) function to get the existing DACL or SACL from an object's [*security descriptor*](/windows/desktop/SecGloss/s-gly).
2.  For each new ACE, call the [**BuildExplicitAccessWithName**](/windows/desktop/api/Aclapi/nf-aclapi-buildexplicitaccesswithnamea) function to fill an [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structure with the information that describes the ACE.
3.  Call [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla), specifying the existing ACL and an array of [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structures for the new ACEs. The **SetEntriesInAcl** function allocates and initializes the ACL and its ACEs.
4.  Call the [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) or [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) function to attach the new ACL to the object's security descriptor.

If the caller specifies an existing ACL, [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) merges the new ACE information with the existing ACEs in the ACL. Consider the case, for example, in which the existing ACL grants access to a specified trustee and an [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structure denies access to the same trustee. In this case, **SetEntriesInAcl** adds a new access-denied ACE for the trustee and deletes or modifies the existing access-allowed ACE for the trustee.

For sample code that merges a new ACE into an existing ACL, see [Modifying the ACLs of an Object in C++](modifying-the-acls-of-an-object-in-c--.md).

 

 
