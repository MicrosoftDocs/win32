---
title: Terminating a Task Example
description: You can terminate a task while it is running by calling IScheduledWorkItem Terminate.
ms.assetid: f8401650-e196-4959-8f23-3d649a55f73d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Terminating a Task Example

You can terminate a task while it is running by calling [**IScheduledWorkItem::Terminate**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-terminate?branch=master).

The following procedure describes how to terminate a task if it is running.

**To terminate a task if it is running**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/win32/Mstask/nf-mstask-itaskscheduler-activate?branch=master) to get the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::GetStatus** to find out if the task is running. (Note that [**GetStatus**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-getstatus?branch=master) is an [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master) method inherited by [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master).)
4.  Check the status of the task and then call **ITask::Terminate** if the task is running. (Note that [**Terminate**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-terminate?branch=master) is an [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master) method inherited by [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master).)



| For a code example of                | See                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------|
| Verifying the status of a known task | [C/C++ Code Example: Terminating a Task](c-c-code-example-terminating-a-task.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




