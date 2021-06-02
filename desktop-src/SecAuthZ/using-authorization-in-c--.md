---
description: Use the Authorization Manager API to control access to application resources.
ms.assetid: 2485056c-b860-4247-9e7b-0157ca85d05d
title: Using Authorization in C++
ms.topic: article
ms.date: 05/31/2018
---

# Using Authorization in C++

You can use the Authorization Manager API to control access to application resources.

If you have an existing access control solution based on [*access control lists*](/windows/desktop/SecGloss/a-gly) (ACLs) and want to avoid converting this solution to use Authorization Manager, you can continue to use ACLs to control access to resources. For information about controlling access to resources using ACLs, see [Defining Permissions with ACLs in C++](defining-permissions-with-acls-in-c--.md), [Establishing a Client Context from a SID in C++](establishing-a-client-context-from-a-sid-in-c--.md), and [Verifying Client Access with ACLs in C++](verifying-client-access-with-acls-in-c--.md).

> [!Note]  
> For large enterprises, there is a trade-off between administrative overhead and performance. As the number of secured resources and users increases, the administration of ACLs becomes more complicated. Performance is not affected because all required information about access rights is distributed to the secured resources. The performance of Authorization Manager is affected by scaling.

 

For information about other authorization tasks, see [Supporting Tasks for Authorization in C++](supporting-tasks-for-authorization-in-c--.md).



| Topic                                                                                                                | Description                                                                                              |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [Defining Permissions in C++](defining-permissions-in-c--.md)                                                       | Define which users have access to which application resources by creating an authorization policy store. |
| [Verifying Client Access to a Requested Resource in C++](verifying-client-access-to-a-requested-resource-in-c--.md) | Check whether the client has access to one or more operations.                                           |
| [Delegating the Defining of Permissions in C++](delegating-the-defining-of-permissions-in-c--.md)                   | Delegate the administration of authorization policy stores that are stored in Active Directory.          |



 

 

 
