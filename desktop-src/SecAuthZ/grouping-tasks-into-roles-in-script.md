---
description: In Authorization Manager a role represents a category of users and the tasks those users are authorized to perform.
ms.assetid: a4981774-0f5c-4032-8a7d-d9ef44c76abe
title: Grouping Tasks into Roles in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Grouping Tasks into Roles in Script

In Authorization Manager, a role represents a category of users and the tasks those users are authorized to perform. Tasks are grouped together and assigned to a role definition, which is represented by an [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object with its [**IsRoleDefinition**](/windows/desktop/api/Azroles/nf-azroles-iaztask-get_isroledefinition) property set to **True**. The role definition can then be assigned to an [**IAzRole**](/windows/desktop/api/Azroles/nn-azroles-iazrole) object, and users or groups of users are then assigned to that object. For more information about tasks and roles, see [Roles](roles.md).

The following example shows how to assign tasks to a role definition, create a role object, and assign the role definition to the role object. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C, that this store contains an application named Expense, and that this application contains tasks named Submit Expense and Approve Expense.


```VB
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 2, "msxml://C:\MyStore.xml"

'  Create an application object in the store.
Dim expenseApp
Set expenseApp = AzManStore.OpenApplication("Expense")

'  Create a task object to act as a role definition.
Dim roleTask
Set roleTask = expenseApp.CreateTask("Expense Admin")

'  Set the IsRoleDefinition property of roleTask to True.
roleTask.IsRoleDefinition = True

'  Add two tasks to the role definition.
roleTask.AddTask CStr("Submit Expense")
roleTask.AddTask CStr("Approve Expense")

'  Save the role definition to the store.
roleTask.Submit

'  Create a role object.
Dim role1
Set role1 = expenseApp.CreateRole("Expense Administrator")

'  Add the role definition to the role object.
role1.AddTask(roleTask.Name)

'  Save the role object to the store.
role1.Submit
```



 

 



