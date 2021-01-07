---
description: An access control list (ACL) is a list of access control entries (ACE).
ms.assetid: c9aff246-fe11-4d82-b944-b10c3d9ae170
title: Access Control Lists
ms.topic: article
ms.date: 05/31/2018
---

# Access Control Lists

An [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL) is a list of [access control entries](access-control-entries.md) (ACE). Each ACE in an ACL identifies a [trustee](trustees.md) and specifies the [access rights](access-rights-and-access-masks.md) allowed, denied, or audited for that trustee. The [security descriptor](security-descriptors.md) for a [securable object](securable-objects.md) can contain two types of ACLs: a DACL and a SACL.

A [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) identifies the trustees that are allowed or denied access to a securable object. When a [*process*](/windows/desktop/SecGloss/p-gly) tries to access a securable object, the system checks the ACEs in the object's DACL to determine whether to grant access to it. If the object does not have a DACL, the system grants full access to everyone. If the object's DACL has no ACEs, the system denies all attempts to access the object because the DACL does not allow any access rights. The system checks the ACEs in sequence until it finds one or more ACEs that allow all the requested access rights, or until any of the requested access rights are denied. For more information, see [How DACLs Control Access to an Object](how-dacls-control-access-to-an-object.md). For information about how to properly create a DACL, see [Creating a DACL](/windows/desktop/SecBP/creating-a-dacl).

A [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) enables administrators to log attempts to access a secured object. Each ACE specifies the types of access attempts by a specified trustee that cause the system to generate a record in the security event log. An ACE in a SACL can generate audit records when an access attempt fails, when it succeeds, or both. For more information about SACLs, see [Audit Generation](audit-generation.md) and [SACL Access Right](sacl-access-right.md).

Do not try to work directly with the contents of an ACL. To ensure that ACLs are semantically correct, use the appropriate functions to create and manipulate ACLs. For more information, see [Getting Information from an ACL](getting-information-from-an-acl.md) and [Creating or Modifying an ACL](creating-or-modifying-an-acl.md).

ACLs also provide access control to Microsoft Active Directory directory service objects. Active Directory Service Interfaces (ADSI) include routines to create and modify the contents of these ACLs. For more information, see [Controlling Access to Active Directory Objects](/windows/desktop/AD/controlling-access-to-objects-in-active-directory-domain-services).

 

 
