---
title: Controlling Access to Objects and Their Properties
description: To control access to application objects, work with the object security descriptor, and specifically, with the discretionary access-control list (DACL) and its list of access-control entries (ACEs).
ms.assetid: cfcb0998-4400-45cd-bbee-415d43b96a99
ms.tgt_platform: multiple
keywords:
- object AD ,controlling access to
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Access to Objects and Their Properties

To control access to application objects, work with the object security descriptor, and specifically, with the discretionary access-control list (DACL) and its list of access-control entries (ACEs).

When an object is created, it receives a security descriptor. For more information, and a description of the rules that the system uses to create the DACL for a new object, see [How Security Descriptors are Set on New Directory Objects](how-security-descriptors-are-set-on-new-directory-objects.md). These rules reveal that you can:

-   Create a new security descriptor and attach it to the object at creation time. For more information, see [Creating a Security Descriptor for a New Directory Object](creating-a-security-descriptor-for-a-new-directory-object.md).
-   Apply an inheritable ACE, at any point in the directory hierarchy, such that an ACE is inherited by objects down the tree. An object can inherit an ACE from its parent container. For more information, see [Inheritance and Delegation of Administration](inheritance-and-delegation-of-administration.md).
-   Specify an ACE in the default DACL in the schema, if you have the necessary access rights. Every object class definition in the schema includes a default security descriptor that can have a default DACL. For more information, see [Default Security Descriptor](default-security-descriptor.md).

In addition the DACL of an existing object can be modified. You can:

-   Replace the DACL with a new one.
-   Read the existing DACL, modify it, and apply the modified DACL. For more information, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

The following list describes the most important function of an ACE in Active Directory Domain Services. With an ACE, you can:

-   Control who can perform specific operations on an object.
-   Control who has access to a specific property, or set of properties, of an object.
-   Control who can create child objects in a container, including who can create a specific type of child object.
-   Define private control-access rights for an object type and control who can perform the operations protected by the private rights.
-   Apply an ACE to a container object at the root of a directory subtree, such that the protections can be inherited automatically by all child objects down the tree.
-   Apply an ACE that is inherited automatically by a specific type of child object in a subtree.
-   Create an ACE that grants rights to a security group, rather than to a single user.
-   Apply an ACE to Group Policy Objects to control the accounts and computers affected by the policy.

 

 




