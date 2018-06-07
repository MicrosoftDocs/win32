---
title: Creating a Task Using NewWorkItem Example
description: When creating a task, you will use two Task Scheduler interfaces ITaskScheduler and ITask.
ms.assetid: 1cbdba6a-e017-4f00-87cb-970686a69e0a
keywords:
- creating work items Task Scheduler
- work items Task Scheduler , creating tasks
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Task Using NewWorkItem Example

When creating a task, you will use two Task Scheduler interfaces: [**ITaskScheduler**](/windows/desktop/api/Mstask/nn-mstask-itaskscheduler) and [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask). You must provide a unique name for the task, the class identifier of the task object, and the interface identifier of **ITask**. The class identifier and interface identifier are shown in the code example following this topic.

> [!Note]  
> You can also create a task by calling [**ITaskScheduler::AddWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-addworkitem). When you take this route, it is your responsibility to create an instance of the **Task** object (which supports the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface) and then add the task with the name you supply.

 

> [!Note]  
> By default, only a member of the Administrators, Backup Operators, or Server Operators group can create tasks on Windows Server 2003. A member of the Administrators group may change the security descriptor of the Windows\\Task folder to let others create tasks.

 

The name you supply for the task must be unique within the Scheduled Tasks folder. If a task with the same name already exists, [**ITaskScheduler::NewWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-newworkitem) returns ERROR\_FILE\_EXISTS. If you get this return value, you should specify a different name and attempt to create the task again.

The following procedure describes how to create a new work item task.

**To create a new work item task**

1.  Call [**CoInitialize**](0f171cf4-87b9-43a6-97f2-80ed344fe376) to initialize the COM library and [**CoCreateInstance**](7295a55b-12c7-4ed0-a7a4-9ecee16afdec) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::NewWorkItem**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-newworkitem) to create a new task. (This method returns a pointer to an [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.)
3.  Save the new task to disk by calling [**IPersistFile::Save**](da9581e8-98c7-4592-8ee1-a1bc8232635b). (The [**IPersistFile**](7d34507f-8a16-43b4-8225-010798abc546) interface is a standard COM interface supported by the **ITask** interface.)
4.  Call **ITask::Release** to release all resources. (Note that [**Release**](4b494c6f-f0ee-4c35-ae45-ed956f40dc7a) is an [**IUnknown**](33f1d79a-33fc-4ce5-a372-e08bda378332) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)



| For a code example of  | See                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| Creating a single task | [C/C++ Code Example: Creating a Task Using NewWorkItem](c-c-code-example-creating-a-task-using-newworkitem.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




