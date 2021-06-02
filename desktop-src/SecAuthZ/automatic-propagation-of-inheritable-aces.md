---
description: The SetNamedSecurityInfo and SetSecurityInfo functions support automatic propagation of inheritable access control entries (ACEs).
ms.assetid: 0aa49b9b-13e3-4ef9-921d-ea47a013e5a1
title: Automatic Propagation of Inheritable ACEs
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Propagation of Inheritable ACEs

The [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) and [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) functions support automatic propagation of inheritable [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs). For example, if you use these functions to add an inheritable ACE to a directory in an NTFS, the system applies the ACE as appropriate to the [*access control lists*](/windows/desktop/SecGloss/a-gly) (ACLs) of any existing subdirectories or files.

Directly applied ACEs have precedence over inherited ACEs. The system implements this precedence by placing directly applied ACEs ahead of inherited ACEs in a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL). When you call the [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) and [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) functions to set the security information of an object, the system imposes the current inheritance model on the ACLs of all objects in the hierarchy below the target object. For objects that have been converted to the current inheritance model, the SE\_DACL\_AUTO\_INHERITED and SE\_SACL\_AUTO\_INHERITED bits are set in the control field of the [*security descriptor*](/windows/desktop/SecGloss/s-gly) of the object.

When you build a new security descriptor that reflects the current inheritance model, care is taken not to change the semantics of the security descriptor. As such, allow and deny ACEs are never moved in relation to one another. If such movement is needed (for instance to place all noninherited ACEs at the front of an ACL), the ACL is marked as protected to prevent the semantic change.

The system uses the following rules when propagating inherited ACEs to child objects:

-   If a child object with no DACL inherits an ACE, the result is a child object with a DACL that contains only the inherited ACE.
-   If a child object with an empty DACL inherits an ACE, the result is a child object with a DACL that contains only the inherited ACE.
-   If you remove an inheritable ACE from a parent object, automatic inheritance removes any copies of the ACE that were inherited by child objects.
-   If automatic inheritance results in the removal of all ACEs from the DACL of a child object, the child object has an empty DACL rather than no DACL.

These rules can have the unexpected result of converting an object with no DACL to an object with an empty DACL. An object with no DACL allows full access, but an object with an empty DACL allows no access. As an example of how these rules can create an empty DACL, suppose you add an inheritable ACE to the root object of a tree of objects. Automatic inheritance propagates the inheritable ACE to all the objects in the tree. Child objects that started with no DACL now have a DACL with the inherited ACE. If you remove the inheritable ACE from the root object, the system automatically propagates the change to the child objects. Child objects that started with no DACL (allowing full access) now have an empty DACL (allowing no access).

To ensure that a child object with no DACL is not affected by inheritable ACEs, set the SE\_DACL\_PROTECTED flag in the security descriptor of the object.

For information about how to properly create a DACL, see [Creating a DACL](/windows/desktop/SecBP/creating-a-dacl).

 

 
