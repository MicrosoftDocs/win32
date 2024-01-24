---
description: Explains the parts of the access control model.
ms.assetid: cca78195-90f5-45ee-9d16-c445d87e9f5e
title: Parts of the Access Control Model
ms.topic: article
ms.date: 05/31/2018
---

# Parts of the Access Control Model

There are two basic parts of the access control model:

-   [Access tokens](access-tokens.md), which contain information about a logged-on user
-   [Security descriptors](security-descriptors.md), which contain the security information that protects a [securable object](securable-objects.md)

When a user logs on, the system [*authenticates*](/windows/desktop/SecGloss/a-gly) the user's account name and password. If the logon is successful, the system creates an access token. Every [*process*](/windows/desktop/SecGloss/p-gly) executed on behalf of this user will have a copy of this access token. The access token contains [security identifiers](security-identifiers.md) that identify the user's account and any group accounts to which the user belongs. The token also contains a list of the [privileges](privileges.md) held by the user or the user's groups. The system uses this token to identify the associated user when a process tries to access a securable object or perform a system administration task that requires privileges.

When a securable object is created, the system assigns it a [*security descriptor*](/windows/desktop/SecGloss/s-gly) that contains security information specified by its creator, or default security information if none is specified. Applications can use functions to retrieve and set the security information for an existing object.

A security descriptor identifies the object's owner and can also contain the following [access control lists](access-control-lists.md):

-   A [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) that identifies the users and groups allowed or denied access to the object
-   A [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) that controls how the system [audits](audit-generation.md) attempts to access the object

An ACL contains a list of [access control entries](access-control-entries.md) (ACEs). Each ACE specifies a set of [access rights](access-rights-and-access-masks.md) and contains a SID that identifies a [trustee](trustees.md) for whom the rights are allowed, denied, or audited. A trustee can be a user account, group account, or [*logon session*](/windows/desktop/SecGloss/l-gly).

Use functions to manipulate the contents of security descriptors, SIDs, and ACLs rather than accessing them directly. This helps ensure that these structures remain syntactically accurate and prevents future enhancements to the security system from breaking existing code.

The following topics provide information about parts of the access control model:

-   [Access Tokens](access-tokens.md)
-   [Security Descriptors](security-descriptors.md)
-   [Access Control Lists](access-control-lists.md)
-   [Access Control Entries](access-control-entries.md)
-   [Access Rights and Access Masks](access-rights-and-access-masks.md)
-   [How AccessCheck Works](how-dacls-control-access-to-an-object.md)
-   [Centralized Authorization Policy](centralized-authorization-policy.md)
-   [Security Identifiers](security-identifiers.md)

 

 
