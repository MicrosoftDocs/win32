---
title: How Security Affects Operations in Active Directory Domain Services
description: Active Directory Domain Services use access control to grant or deny access to objects, properties, and operations based on the identity of the user performing the access attempt.
ms.assetid: d5d53354-fa97-4e46-9632-20ac49f7db5a
ms.tgt_platform: multiple
keywords:
- Security Effects in Active Directory Domain Services Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# How Security Affects Operations in Active Directory Domain Services

Active Directory Domain Services use access control to grant or deny access to objects, properties, and operations based on the identity of the user performing the access attempt. When your application binds to the directory, it binds with specific user credentials. When authenticated, these credentials determine your application's security context. Regardless of whether the credentials are those of the logged-on user, a specified user, a service account, a computer account, or an unauthenticated user (Guest/Everyone), the Active Directory server verifies the user's right to access an object before any operation is performed on that object. The user may, or may not, have access to a particular object, its children, its properties, or operations on that object, which means that your application must handle the potential errors caused by denied access.

For more information about security contexts and the effects of access control on various operations, see:

-   [Access Control and Read Operations](access-control-and-read-operations.md)
-   [Access Control and Write Operations](access-control-and-write-operations.md)
-   [Access Control and Object Creation](access-control-and-object-creation.md)
-   [Access Control and Object Deletion](access-control-and-object-deletion.md)

 

 




