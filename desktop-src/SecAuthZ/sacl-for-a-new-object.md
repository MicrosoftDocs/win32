---
description: SACL for a New Object
ms.assetid: 1d0d6fee-e5ec-4d8f-8ed8-10c725c57a6a
title: SACL for a New Object
ms.topic: article
ms.date: 05/31/2018
---

# SACL for a New Object

The system uses the following algorithm to build a SACL for most types of new securable objects:

1.  The object's SACL is the SACL from the [*security descriptor*](/windows/desktop/SecGloss/s-gly) specified by the object's creator. The system merges any inheritable ACEs into the specified SACL unless the SE\_SACL\_PROTECTED bit is set in the security descriptor's control bits. SYSTEM\_RESOURCE\_ATTRIBUTE\_ACEs and SYSTEM\_SCOPED\_POLICY\_ID\_ACEs from a parent object will be merged to a new object even if the SE\_SACL\_PROTECTED bit is set.
2.  If the creator does not specify a security descriptor, the system builds the object's SACL from inheritable ACEs.
3.  If there is no specified or inherited SACL, the object has no SACL.

To specify a SACL for a new object, the object's creator must have the SE\_SECURITY\_NAME [privilege](privileges.md) enabled. If the specified SACL for a new object contain only SYSTEM\_RESOURCE\_ATTRIBUTE\_ACEs, then the SE\_SECURITY\_NAME privilege is not required. The creator does not need this privilege if the object's SACL is built from inherited ACEs.

The system uses a different algorithm to build a SACL for a new Active Directory object. For more information, see [How Security Descriptors are Set on New Directory Objects](/windows/desktop/AD/how-security-descriptors-are-set-on-new-directory-objects).

 

 
