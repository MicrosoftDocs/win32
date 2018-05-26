---
Description: Several functions are provided that retrieve access control information from an access control list (ACL).
ms.assetid: a0839c49-09e9-4407-8702-051b88ef2231
title: Getting Information from an ACL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Information from an ACL

Several functions are provided that retrieve access control information from an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL). These include functions for determining the access rights that an ACL grants or audits for a specified [trustee](trustees.md). Other functions enable you to extract information about the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an ACL.

The [**GetExplicitEntriesFromAcl**](/windows/win32/Aclapi/nf-aclapi-getexplicitentriesfromacla?branch=master) function retrieves an array of [**EXPLICIT\_ACCESS**](/windows/win32/AccCtrl/ns-accctrl-_explicit_access_a?branch=master) structures that describe the ACEs in an ACL. This can be useful when copying ACE information from one ACL to another. For example, a call to **GetExplicitEntriesFromAcl** to get information about the ACEs in one ACL can be followed by passing the returned **EXPLICIT\_ACCESS** structures in a call to the [**SetEntriesInAcl**](/windows/win32/Aclapi/nf-aclapi-setentriesinacla?branch=master) function to create equivalent ACEs in a new ACL.

The [**GetEffectiveRightsFromAcl**](/windows/win32/Aclapi/nf-aclapi-geteffectiverightsfromacla?branch=master) function enables you to determine the effective access rights that a DACL grants to a specified trustee. The trustee's effective access rights are the access rights that a DACL grants to the trustee or to any groups of which the trustee is a member. **GetEffectiveRightsFromAcl** checks all access-allowed and access-denied ACEs in the specified DACL.

**Use the following steps to determine a trustee's access rights to an object**

1.  Call the [**GetSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-getsecurityinfo?branch=master) or [**GetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-getnamedsecurityinfoa?branch=master) function to get a pointer to an object's DACL.
2.  Call the [**GetEffectiveRightsFromAcl**](/windows/win32/Aclapi/nf-aclapi-geteffectiverightsfromacla?branch=master) function to retrieve the access rights that the DACL grants to a specified trustee.

The [**GetAuditedPermissionsFromAcl**](/windows/win32/Aclapi/nf-aclapi-getauditedpermissionsfromacla?branch=master) function enables you to check a SACL to determine the audited access rights for a specified trustee or for any groups of which the trustee is a member. The audited rights indicate the types of access attempts that cause the system to generate an audit record in the security event log. The function returns two [*access masks*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-mask-gly): one containing the access rights monitored for failed access attempts, and another containing the access rights monitored for successful access. **GetAuditedPermissionsFromAcl** checks all system-audit ACEs in a SACL.

 

 



