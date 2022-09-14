---
description: Instructions for using the Authorization Manager API to create an authorization policy store in Script.
ms.assetid: bd9a995a-4195-4da4-a194-472448a0cb08
title: Creating an Authorization Policy Store in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating an Authorization Policy Store in Script

Create an authorization policy before or during the installation of an application.

When you use the Authorization Manager API to create an authorization policy, follow the instructions provided in the following topics.



| Topic                                                                                                                  | Description                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating an Authorization Policy Store Object in Script](creating-an-authorization-policy-store-object-in-script.md) | An authorization policy store contains information about the security policy of an application or group of applications.                                                                                                                                       |
| [Creating an Application Object in Script](creating-an-application-object-in-script.md)                               | For each application that uses an authorization policy store, you must create an [**IAzApplication**](/windows/desktop/api/Azroles/nn-azroles-iazapplication) object and save it to a policy store.                                                                                                |
| [Defining Operations in Script](defining-operations-in-script.md)                                                     | An operation is a low-level function or method of an application.                                                                                                                                                                                              |
| [Grouping Operations into Tasks in Script](grouping-operations-into-tasks-in-script.md)                               | A task is a high-level action that users of an application need to complete. Tasks are made up of operations, which are low-level functions and methods of the application.                                                                                    |
| [Grouping Tasks into Roles in Script](grouping-tasks-into-roles-in-script.md)                                         | A role represents a category of users and the tasks those users are authorized to perform.                                                                                                                                                                     |
| [Defining Groups of Users in Script](defining-groups-of-users-in-script.md)                                           | An [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object represents a group of users. Roles can then be assigned to this group of users collectively. An **IAzApplicationGroup** object can also include other **IAzApplicationGroup** objects as members. |
| [Adding Users to an Application Group in Script](adding-users-to-an-application-group-in-script.md)                   | An application group is a group of users and user groups. An application group can contain other application groups, so groups of users can be nested. An application group is represented by an [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object.    |



 

 

 



