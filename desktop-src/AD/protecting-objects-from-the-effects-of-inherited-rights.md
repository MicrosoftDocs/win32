---
title: Protecting Objects from the Effects of Inherited Rights
description: As discussed in the topic Inheritance and Delegation of Administration, ACEs can be set on a container object, such as an organizationalUnit, domainDNS, container, and so on, and propagated to child objects based on the ACE flags set on those ACEs.
ms.assetid: 3da000dd-3a32-4294-a636-ad077e618db2
ms.tgt_platform: multiple
keywords:
- Protecting Objects from the Effects of Inherited Rights AD
ms.topic: article
ms.date: 05/31/2018
---

# Protecting Objects from the Effects of Inherited Rights

As discussed in the topic [Inheritance and Delegation of Administration](inheritance-and-delegation-of-administration.md), ACEs can be set on a container object, such as an **organizationalUnit**, **domainDNS**, **container**, and so on, and propagated to child objects based on the ACE flags set on those ACEs.

If you have a secure object or an object whose ACEs you want to explicitly control, such as a private OU or a special user, you can prevent ACEs from being propagated to the object by its parent container or its parent container's predecessors.

Use the [**IADsSecurityDescriptor.Control**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) property to control whether DACLs and SACLs are inherited by the object from its parent container.

The [**IADsSecurityDescriptor.Control**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) property can be used to protect an object from the effects of inherited ACEs. The following flags force access control to be set explicitly on the object and prevent a user from modifying access control to the object by setting inheritable ACEs on the object's parent container, or its parent container's predecessors.



| Flag                               | Description                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SE\_DACL\_PROTECTED**<br/> | Prevents ACEs set on the DACL of the parent container, and any objects above the parent container in the directory hierarchy, from being applied to the object DACL.<br/> |
| **SE\_SACL\_PROTECTED**<br/> | Prevents ACEs set on the SACL of the parent container, and any objects above the parent container in the directory hierarchy, from being applied to the object SACL.<br/> |



 

Be aware that the **SE\_DACL\_PRESENT** flag must be present to set **SE\_DACL\_PROTECTED** and **SE\_SACL\_PRESENT** must be present to set **SE\_SACL\_PROTECTED**.

 

