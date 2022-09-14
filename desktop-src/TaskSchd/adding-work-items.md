---
title: Adding Work Items
description: There are two ways to add work items to the Scheduled Tasksfolder. You can create a new work item within the folder, or you can add an existing work item to the folder.
ms.assetid: fad5e813-a2e9-40af-97a9-4f92debf1808
keywords:
- work items Task Scheduler , adding
- tasks Task Scheduler , adding
ms.topic: article
ms.date: 05/31/2018
---

# Adding Work Items

There are two ways to add [*work items*](w.md) to the [*Scheduled Tasksfolder*](s.md). You can create a new work item within the folder, or you can add an existing work item to the folder.

> [!Note]  
> Currently, only task objects can be added to the Scheduled Tasks folder. When adding a task, you must know the identifiers for the task class and the task interface [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).

 

You create new work items by calling the [**ITaskScheduler::NewWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-newworkitem) method. This method creates a new work item object using the name that you provide and adds the work item to the Scheduled Tasks folder. When you create a new work item, the Task Scheduler allocates the memory that is required for the new object.

To add existing work items to the Scheduled Tasks folder, call the [**ITaskScheduler::AddWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-addworkitem) method. When you call this method, you must create the object.

The names you supply for work items must be unique within the Scheduled Tasks folder. If a work item with the same name already exists when you call either the [**ITaskScheduler::NewWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-newworkitem) method or the [**ITaskScheduler::AddWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-addworkitem) method, the method returns an **ERROR\_FILE\_EXISTS** error. For more information, see [Creating a Task Using NewWorkItem Example](creating-a-task-using-newworkitem-example.md).

 

 




