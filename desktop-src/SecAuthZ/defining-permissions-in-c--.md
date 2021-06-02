---
description: Instructions for using the Authorization Manager API to define permissions in C++ by creating an authorization policy store.
ms.assetid: 8a3bf625-7973-4905-a63c-e42e6682b7c2
title: Defining Permissions in C++
ms.topic: article
ms.date: 05/31/2018
---

# Defining Permissions in C++

In Authorization Manager, you define which users have access to which application resources by creating an authorization policy store.

For information about defining permissions with ACLs, see [Defining Permissions with ACLs in C++](defining-permissions-with-acls-in-c--.md).

**To define access permissions**

1.  Create the store where the authorization policy is defined:<dl>

[Creating an Authorization Policy Store Object in C++](creating-an-authorization-policy-store-object-in-c--.md)  
    </dl>
2.  Create a section in the authorization policy store for a specific application:<dl>

[Creating an Application Object in C++](creating-an-application-object-in-c--.md)  
    </dl>
3.  Define operations that the application implements to access and modify resources:<dl>

[Defining Operations in C++](defining-operations-in-c--.md)  
    </dl>
4.  Group operations into high-level tasks that users want to perform:<dl>

[Grouping Operations into Tasks in C++](grouping-operations-into-tasks-in-c--.md)  
    </dl>
5.  Define roles that consist of groups of tasks:<dl>

[Grouping Tasks into Roles in C++](grouping-tasks-into-roles-in-c--.md)  
    </dl>A user that is assigned to a role has permission to perform any task assigned to that role.
6.  Create scripts to qualify access to tasks at run time:<dl>

[Qualifying Access with Business Logic in C++](qualifying-access-with-business-logic-in-c--.md)  
    </dl>This step is optional.
7.  Define groups of users:<dl>

[Defining Groups of Users in C++](defining-groups-of-users-in-c--.md)  
    </dl>These groups can then be assigned to roles to determine which tasks they can perform.
8.  Add users to user groups:<dl>

[Adding Users to an Application Group in C++](adding-users-to-an-application-group-in-c--.md)  
    </dl>

 

 



