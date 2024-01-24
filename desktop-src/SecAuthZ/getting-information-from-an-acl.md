---
description: Several functions are provided that retrieve access control information from an access control list (ACL).
ms.assetid: a0839c49-09e9-4407-8702-051b88ef2231
title: Getting Information from an ACL
ms.topic: article
ms.date: 05/31/2018
---

# Getting Information from an ACL

Several functions are provided that retrieve access control information from an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL). These include functions for determining the access rights that an ACL grants or audits for a specified [trustee](trustees.md). Other functions enable you to extract information about the [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) in an ACL.

The [**GetExplicitEntriesFromAcl**](/windows/desktop/api/Aclapi/nf-aclapi-getexplicitentriesfromacla) function retrieves an array of [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structures that describe the ACEs in an ACL. This can be useful when copying ACE information from one ACL to another. For example, a call to **GetExplicitEntriesFromAcl** to get information about the ACEs in one ACL can be followed by passing the returned **EXPLICIT\_ACCESS** structures in a call to the [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) function to create equivalent ACEs in a new ACL.

The [**GetEffectiveRightsFromAcl**](/windows/desktop/api/Aclapi/nf-aclapi-geteffectiverightsfromacla) function enables you to determine the effective access rights that a DACL grants to a specified trustee. The trustee's effective access rights are the access rights that a DACL grants to the trustee or to any groups of which the trustee is a member. **GetEffectiveRightsFromAcl** checks all access-allowed and access-denied ACEs in the specified DACL.

**Use the following steps to determine a trustee's access rights to an object**

1.  Call the [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo) or [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) function to get a pointer to an object's DACL.
2.  Call the [**GetEffectiveRightsFromAcl**](/windows/desktop/api/Aclapi/nf-aclapi-geteffectiverightsfromacla) function to retrieve the access rights that the DACL grants to a specified trustee.

The [**GetAuditedPermissionsFromAcl**](/windows/desktop/api/Aclapi/nf-aclapi-getauditedpermissionsfromacla) function enables you to check a SACL to determine the audited access rights for a specified trustee or for any groups of which the trustee is a member. The audited rights indicate the types of access attempts that cause the system to generate an audit record in the security event log. The function returns two [*access masks*](/windows/desktop/SecGloss/a-gly): one containing the access rights monitored for failed access attempts, and another containing the access rights monitored for successful access. **GetAuditedPermissionsFromAcl** checks all system-audit ACEs in a SACL.

 

 
