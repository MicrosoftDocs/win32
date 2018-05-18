---
title: Terminating a Task Example
description: You can terminate a task while it is running by calling IScheduledWorkItem Terminate.
ms.assetid: 'f8401650-e196-4959-8f23-3d649a55f73d'
---

# Terminating a Task Example

You can terminate a task while it is running by calling [**IScheduledWorkItem::Terminate**](ischeduledworkitem-terminate.md).

The following procedure describes how to terminate a task if it is running.

**To terminate a task if it is running**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](itaskscheduler-activate.md) to get the [**ITask**](itask.md) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::GetStatus** to find out if the task is running. (Note that [**GetStatus**](ischeduledworkitem-getstatus.md) is an [**IScheduledWorkItem**](ischeduledworkitem.md) method inherited by [**ITask**](itask.md).)
4.  Check the status of the task and then call **ITask::Terminate** if the task is running. (Note that [**Terminate**](ischeduledworkitem-terminate.md) is an [**IScheduledWorkItem**](ischeduledworkitem.md) method inherited by [**ITask**](itask.md).)



| For a code example of                | See                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------|
| Verifying the status of a known task | [C/C++ Code Example: Terminating a Task](c-c-code-example-terminating-a-task.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




