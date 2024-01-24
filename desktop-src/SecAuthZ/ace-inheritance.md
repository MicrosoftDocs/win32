---
description: An objects ACL can contain ACEs that it inherited from its parent container.
ms.assetid: a9e5ad4d-61c6-43ed-a162-460683bcdb16
title: ACE Inheritance
ms.topic: article
ms.date: 05/31/2018
---

# ACE Inheritance

An object's ACL can contain ACEs that it inherited from its parent container. For example, a registry subkey can inherit ACEs from the key above it in the registry hierarchy. Likewise, a file in an NTFS file system can inherit ACEs from the directory that contains it.

The [**ACE\_HEADER**](/windows/desktop/api/Winnt/ns-winnt-ace_header) structure of an ACE contains a set of inheritance flags that control ACE inheritance and the effect of an ACE on the object to which it is attached. The system interprets the inheritance flags and other inheritance information according to the [rules of ACE inheritance](ace-inheritance-rules.md).

These rules have been enhanced with the following features:

-   Support for [automatic propagation of inheritable ACEs](automatic-propagation-of-inheritable-aces.md).
-   A flag that differentiates between inherited ACEs and ACEs that were directly applied to an object.
-   Object-specific ACEs that allow you to specify the type of child object that can inherit the ACE.
-   The ability to prevent a DACL or SACL from inheriting ACEs by setting the SE\_DACL\_PROTECTED or SE\_SACL\_PROTECTED bits in the [*security descriptor's*](/windows/desktop/SecGloss/s-gly) control bits except for SYSTEM\_RESOURCE\_ATTRIBUTE\_ACE and SYSTEM\_SCOPED\_POLICY\_ID\_ACE.

 

 
