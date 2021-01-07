---
description: Instructions for using the Authorization Manager API to define permissions in Script by creating an authorization policy store.
ms.assetid: 114426e8-03a7-41e2-96c9-e2da91aa7d84
title: Defining Permissions in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Defining Permissions in Script

In Authorization Manager, you define which users have access to which application resources by creating an authorization policy store.

**To define access permissions**

1.  Create the store where the authorization policy is defined:<dl>

[Creating an Authorization Policy Store in Script](creating-an-authorization-policy-store-object-in-script.md)  
    </dl>
2.  Create a section in the authorization policy store for a specific application:<dl>

[Creating an Application Object in Script](creating-an-application-object-in-script.md)  
    </dl>
3.  Define operations that the application implements to access and modify resources:<dl>

[Defining Operations in Script](defining-operations-in-script.md)  
    </dl>
4.  Group operations into high-level tasks that users want to perform:<dl>

[Grouping Operations into Tasks in Script](grouping-operations-into-tasks-in-script.md)  
    </dl>
5.  Define roles that consist of groups of tasks:<dl>

[Grouping Tasks into Roles in Script](grouping-tasks-into-roles-in-script.md)  
    </dl>A user that is assigned to a role has permission to perform any task assigned to that role.
6.  Create scripts to qualify access to tasks at run time:<dl>

[Qualifying Access with Business Logic in Script](qualifying-access-with-business-logic-in-script.md)  
    </dl>This step is optional.
7.  Define groups of users:<dl>

[Defining Groups of Users in Script](defining-groups-of-users-in-script.md)  
    </dl>These groups can then be assigned to roles to determine which tasks they can perform.
8.  Add users to user groups:<dl>

[Adding Users to an Application Group in Script](adding-users-to-an-application-group-in-script.md)  
    </dl>

 

 



