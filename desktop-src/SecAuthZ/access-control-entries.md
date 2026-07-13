---
description: An access control entry (ACE) is an element in an access control list (ACL). Learn about the types of ACEs, their components, and how they control access to objects in Windows security.
ms.assetid: 9cf4d796-3955-456b-9db9-ae9fa83752f6
title: Access Control Entries
ms.topic: concept-article
ms.date: 07/08/2025
# customer intent: As a Windows app developer, I want to understand access control entries (ACEs) in Windows security, so that I can manage access to objects in my applications effectively.
---

# Access control entries

An [access control entry](/windows/win32/SecGloss/a-gly) (ACE) is an element in an [access control list](/windows/win32/SecGloss/a-gly) (ACL). An ACL can have zero or more ACEs. Each ACE controls or monitors access to an object by a specified trustee. For information about adding, removing, or changing the ACEs in an object's ACLs, see [Modifying the ACLs of an Object in C++](modifying-the-acls-of-an-object-in-c--.md).

## Types of ACEs

There are six types of ACEs, three of which are supported by all securable objects. The other three types are [Object-specific ACEs](object-specific-aces.md) supported by directory service objects.

All types of ACEs contain the following access control information:

-   A [security identifier](security-identifiers.md) (SID) that identifies the [trustee](trustees.md) to which the ACE applies.
-   An [*access mask*](/windows/win32/SecGloss/a-gly) that specifies the [access rights](access-rights-and-access-masks.md) controlled by the ACE.
-   A flag that indicates the type of ACE.
-   A set of bit flags that determine whether child containers or objects can inherit the ACE from the primary object to which the ACL is attached.

The following table lists the three ACE types supported by all securable objects:

| Type | Description |
|------|-------------|
| Access-denied ACE | Used in a [discretionary access control list](/windows/win32/SecGloss/d-gly) (DACL) to deny access rights to a trustee. |
| Access-allowed ACE | Used in a DACL to allow access rights to a trustee. |
| System-audit ACE | Used in a [system access control list](/windows/win32/SecGloss/s-gly) (SACL) to generate an audit record when the trustee attempts to exercise the specified access rights. |

For a table of object-specific ACEs, see [Object-specific ACEs](object-specific-aces.md).

> [!NOTE]  
> System-alarm object ACEs are not currently supported.

## Related content

[Access control lists](access-control-lists.md)

[Object-specific ACEs](object-specific-aces.md)
