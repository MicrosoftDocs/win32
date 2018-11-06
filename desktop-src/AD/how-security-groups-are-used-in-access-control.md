---
title: How Security Groups are Used in Access Control
description: The security identifier (SID) is the object identifier of the user or security group when the user or group is used for security purposes.
ms.assetid: 3236c51f-21c1-4c07-9b76-2668ae72a42f
ms.tgt_platform: multiple
keywords:
- How Security Groups are Used in Access Control
- access control, security groups used in
ms.topic: article
ms.date: 05/31/2018
---

# How Security Groups are Used in Access Control

The security identifier (SID) is the object identifier of the user or security group when the user or group is used for security purposes. The name of the user or group is not used as the unique identifier within the system. The SID is stored in the **objectSid** attribute of user objects and security group objects. The Active Directory server generates the **objectSid** when the user or group is created. The system ensures that the SIDs are unique across a forest. Be aware that the **objectGuid** is the unique identifier of a user, group, or any other directory object. The SID changes if a user or group is moved to another domain; the **objectGuid** remains the same.

When a user or group is given permission to access a resource, such as a printer or a file share, the SID of the user or group is added to the access control entry (ACE) defining the granted permission in the resource's discretionary access control list (DACL). In Active Directory Domain Services, each object has an **nTSecurityDescriptor** attribute that stores a DACL defining the access to that particular object or attributes on that object. For more information about setting access control on objects in Active Directory Domain Services, see [Controlling Access to Objects in Active Directory Domain Services](controlling-access-to-objects-in-active-directory-domain-services.md).

When a user logs on to a Windows 2000 domain, the operating system generates an access token. This access token is used to determine which resources the user may access. The user access token includes the following data:

-   User SID.
-   SIDs of all global and universal security groups that the user is a member of.
-   SIDs of all nested global and universal security groups.

Every process executed on behalf of this user has a copy of this access token.

When the user attempts to access resources on a computer, the service through which the user accesses the resource will impersonate the user by creating a new access token based on the access token created at user logon time. This new access token will also contain the following SIDs:

-   SIDs for all domain local groups in the target domain that the user is a member of.
-   SIDs for all machine local groups on the target computer that the user is a member of.

The service uses this new access token to evaluate access to the resource. If a SID in the access token appears in any ACEs in the DACL, the service gives the user the permissions specified in those ACEs.

 

 




