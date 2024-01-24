---
description: An access control entry (ACE) is an element in an access control list (ACL).
ms.assetid: 9cf4d796-3955-456b-9db9-ae9fa83752f6
title: Access Control Entries
ms.topic: article
ms.date: 05/31/2018
---

# Access Control Entries

An [*access control entry*](/windows/desktop/SecGloss/a-gly) (ACE) is an element in an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL). An ACL can have zero or more ACEs. Each ACE controls or monitors access to an object by a specified trustee. For information about adding, removing, or changing the ACEs in an object's ACLs, see [Modifying the ACLs of an Object in C++](modifying-the-acls-of-an-object-in-c--.md).

There are six types of ACEs, three of which are supported by all securable objects. The other three types are [Object-specific ACEs](object-specific-aces.md) supported by directory service objects.

All types of ACEs contain the following access control information:

-   A [security identifier](security-identifiers.md) (SID) that identifies the [trustee](trustees.md) to which the ACE applies.
-   An [*access mask*](/windows/desktop/SecGloss/a-gly) that specifies the [access rights](access-rights-and-access-masks.md) controlled by the ACE.
-   A flag that indicates the type of ACE.
-   A set of bit flags that determine whether child containers or objects can inherit the ACE from the primary object to which the ACL is attached.

The following table lists the three ACE types supported by all securable objects.



| Type               | Description                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access-denied ACE  | Used in a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) to deny access rights to a trustee.                                       |
| Access-allowed ACE | Used in a DACL to allow access rights to a trustee.                                                                                                                                                                                              |
| System-audit ACE   | Used in a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) to generate an audit record when the trustee attempts to exercise the specified access rights. |



 

For a table of object-specific ACEs, see [Object-specific ACEs](object-specific-aces.md).

> [!Note]  
> System-alarm object ACEs are not currently supported.

 

 

 
