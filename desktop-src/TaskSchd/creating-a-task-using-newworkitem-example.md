---
title: Creating a Task Using NewWorkItem Example
description: When creating a task, you will use two Task Scheduler interfaces ITaskScheduler and ITask.
ms.assetid: '1cbdba6a-e017-4f00-87cb-970686a69e0a'
keywords: ["creating work items Task Scheduler", "work items Task Scheduler , creating tasks"]
---

# Creating a Task Using NewWorkItem Example

When creating a task, you will use two Task Scheduler interfaces: [**ITaskScheduler**](itaskscheduler.md) and [**ITask**](itask.md). You must provide a unique name for the task, the class identifier of the task object, and the interface identifier of **ITask**. The class identifier and interface identifier are shown in the code example following this topic.

> [!Note]  
> You can also create a task by calling [**ITaskScheduler::AddWorkItem**](itaskscheduler-addworkitem.md). When you take this route, it is your responsibility to create an instance of the **Task** object (which supports the [**ITask**](itask.md) interface) and then add the task with the name you supply.

 

> [!Note]  
> By default, only a member of the Administrators, Backup Operators, or Server Operators group can create tasks on Windows Server 2003. A member of the Administrators group may change the security descriptor of the Windows\\Task folder to let others create tasks.

 

The name you supply for the task must be unique within the Scheduled Tasks folder. If a task with the same name already exists, [**ITaskScheduler::NewWorkItem**](itaskscheduler-newworkitem.md) returns ERROR\_FILE\_EXISTS. If you get this return value, you should specify a different name and attempt to create the task again.

The following procedure describes how to create a new work item task.

**To create a new work item task**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::NewWorkItem**](itaskscheduler-newworkitem.md) to create a new task. (This method returns a pointer to an [**ITask**](itask.md) interface.)
3.  Save the new task to disk by calling [**IPersistFile::Save**](_com_ipersistfile_save). (The [**IPersistFile**](_com_ipersistfile) interface is a standard COM interface supported by the **ITask** interface.)
4.  Call **ITask::Release** to release all resources. (Note that [**Release**](_com_iunknown_release) is an [**IUnknown**](_com_iunknown) method inherited by [**ITask**](itask.md).)



| For a code example of  | See                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| Creating a single task | [C/C++ Code Example: Creating a Task Using NewWorkItem](c-c-code-example-creating-a-task-using-newworkitem.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




