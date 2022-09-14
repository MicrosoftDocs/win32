---
title: Inheritance and Delegation of Administration
description: Describes AD DS support for the inheritance of permissions down the object tree and also object-specific inheritance.
ms.assetid: db9cf8d9-6831-4456-b2a5-9f5b4f3e9100
ms.tgt_platform: multiple
keywords:
- administration inheritance and delegation Active Directory
- Active Directory Active Directory ,permissions inheritance
ms.topic: article
ms.date: 05/31/2018
---

# Inheritance and Delegation of Administration

Active Directory Domain Services supports the inheritance of permissions down the object tree to allow administration tasks to be performed at higher levels in the tree. This enables administrators to set up inheritable permissions on objects near the root, such as domain and organizational units, and have those permissions distributed to various objects in the tree.

Inheritance can be set on a per-ACE basis. The following table lists flags that can be specified in the **AceFlags** to control inheritance of the ACE.



| Flag                                                     | Description                                                                                                                                     |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **ADS\_ACEFLAG\_INHERIT\_ACE**<br/>                | Causes the ACE to be inherited down in the tree.<br/>                                                                                     |
| **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE**<br/> | Causes the ACE to be inherited down only one level in the tree.<br/>                                                                      |
| **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE**<br/>          | Causes the ACE to be ignored on the object it is specified on, only be inherited down, and be effective where it has been inherited.<br/> |



 

In addition to setting inheritance, Active Directory Domain Services supports object-specific inheritance. This allows the inheritable ACEs to be inherited down the tree, but be effective only on a specific type of object. This is extremely useful in delegating administration. For example, this can be used to set an object-specific inheritable ACE at an organizational unit that enables a group to have full control on all user objects in the organizational unit, but nothing else. Thereby, the management of users in that organizational unit gets delegated to the users in that group.

### Delegating Service Administration with Security Groups

Use Security groups to define and delegate administrative roles associated with your application server. For example, your service may be associated with a group MyService Administrators. Users who are identified as the MyService administrators will be added to MyService Administrators group. The setup program for MyService can set ACLs on the directory to enable MyService Administrators sufficient permissions to read/write MyService-related attributes or create MyService-specific objects for example.

### Roles in Security Groups for Computers Running Your Service

Use security groups to define the set of computers that are granted access to your service's objects in the directory. For example, your service may be associated with a group MyService Servers. All computers running the MyService server are added to MyService Servers group and this group can then be given access to parts of the directory where MyService servers need to read/write data. The setup program for MyService can set ACLs on the directory to enable MyService Servers sufficient permissions to read/write MyService-related attributes or create MyService-specific objects for example.

 

 





