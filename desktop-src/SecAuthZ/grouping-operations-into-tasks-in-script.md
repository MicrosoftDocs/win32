---
description: In Authorization Manager, a task is a high-level action that users of an application need to complete.
ms.assetid: a266dde7-86f8-4537-99a5-be7142e765c6
title: Grouping Operations into Tasks in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Grouping Operations into Tasks in Script

In Authorization Manager, a task is a high-level action that users of an application need to complete. Tasks are made up of operations, which are low-level functions and methods of the application. A task is then assigned to those roles that must perform that task. A task is represented by an [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object. For more information about operations and tasks, see [Operations and Tasks](operations-and-tasks.md).

The following example shows how to group operations to create a task. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C, that this store contains an application named Expense, and that this application contains operations defined in the topic [Defining Operations in Script](defining-operations-in-script.md).


```VB
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 2, "msxml://C:\MyStore.xml"

'  Create an application object in the store.
Dim expenseApp
Set expenseApp= AzManStore.OpenApplication("Expense")

'  Create a task object.
Dim Task1
Set Task1 = expenseApp.CreateTask("Submit Expense")

'  Add operations to the task.
Task1.AddOperation CStr("RetrieveForm")
Task1.AddOperation CStr("EnqueRequest")
Task1.AddOperation Cstr("UseFormControl")

'  Save the task to the store.
Task1.Submit
```



 

 



