---
description: Instructions for using the Authorization Manager API to create an authorization policy store in C++.
ms.assetid: a350f25a-7cda-4879-82d1-151a3da7d8ec
title: Creating an Authorization Policy Store in C++
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Authorization Policy Store in C++

Create an authorization policy before or during the installation of an application.

When you use the Authorization Manager API to create an authorization policy, follow the instructions provided in the following topics.



| Topic                                                                                                            | Description                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating an Authorization Policy Store Object in C++](creating-an-authorization-policy-store-object-in-c--.md) | An authorization policy store contains information about the security policy of an application or group of applications. The information includes the applications, operations, tasks, users, and groups of users associated with the store.              |
| [Creating an Application Object in C++](creating-an-application-object-in-c--.md)                               | An authorization policy store contains authorization policy information for one or more applications. For each application that uses that policy store, you must create an [**IAzApplication**](/windows/desktop/api/Azroles/nn-azroles-iazapplication) object and save it to a policy store. |
| [Defining Operations in C++](defining-operations-in-c--.md)                                                     | In Authorization Manager, an operation is a low-level function or method of an application.                                                                                                                                                               |
| [Grouping Operations into Tasks in C++](grouping-operations-into-tasks-in-c--.md)                               | In Authorization Manager, a task is a high-level action that users of an application need to complete. Tasks are made up of operations, which are low-level functions and methods of the application.                                                     |
| [Grouping Tasks into Roles in C++](grouping-tasks-into-roles-in-c--.md)                                         | In Authorization Manager, a role represents a category of users and the tasks those users are authorized to perform.                                                                                                                                      |
| [Defining Groups of Users in C++](defining-groups-of-users-in-c--.md)                                           | In Authorization Manager, an [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object represents a group of users. Roles can then be assigned to this group of users collectively.                                                                       |
| [Adding Users to an Application Group in C++](adding-users-to-an-application-group-in-c--.md)                   | In Authorization Manager, an application group is a group of users and user groups. An application group can contain other application groups, so groups of users can be nested.                                                                          |



 

 

 



