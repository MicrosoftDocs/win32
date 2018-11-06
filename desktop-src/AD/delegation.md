---
title: Delegation
description: Delegation is one of the most important security features of Active Directory Domain Services.
ms.assetid: ab8740c9-f5a2-40cc-abce-0ef80c3fca7a
ms.tgt_platform: multiple
keywords:
- Delegation AD
- security AD , delegation
ms.topic: article
ms.date: 05/31/2018
---

# Delegation

*Delegation* is one of the most important security features of Active Directory Domain Services. Delegation enables a higher administrative authority to grant specific administrative rights for containers and subtrees to individuals and groups. Domain administrators, with broad authority over large segments of users, are no longer required.

An ACE can grant specific administrative rights for the objects in a container to a user or group. Rights are granted for specific operations on specific object classes using ACEs in the container's ACL. For example, to enable a user named "user 1" to be an administrator of the "Corporate Accounting" organizational unit, add ACEs to the ACL on "Corporate Accounting" as follows:

""user 1";Grant ;Create, Modify, Delete;Object-Class User"user 1";Grant ;Create, Modify, Delete;Object-Class Group"user 1";Grant ;Write;Object-Class User; Attribute Password"

Now, user 1 can create new users and groups in Corporate Accounting and set the passwords on existing users, but user 1 cannot create any other object classes and cannot affect users in any other containers, unless, of course, user 1 is granted that access by ACEs on the other containers.

 

 




