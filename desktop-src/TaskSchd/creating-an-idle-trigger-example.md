---
title: Creating an Idle Trigger Example
description: To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see Task Idle Conditions.
ms.assetid: d36a621c-4011-4c3d-b6f4-b56d1f50983c
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Idle Trigger Example

To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

After creating the idle trigger, call [**IPersistFile::Save**](https://msdn.microsoft.com/library/ms693701(v=VS.85).aspx) to save the new trigger to disk.

The following procedure describes how to create an idle trigger for a known task.

**To create an idle trigger for a known task**

1.  Call [**CoInitialize**](https://msdn.microsoft.com/library/ms678543(v=VS.85).aspx) to initialize the COM library and [**CoCreateInstance**](https://msdn.microsoft.com/library/ms686615(v=VS.85).aspx) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**SetIdleWait**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-setidlewait) to set how long the system must remain idle before the trigger will fire. (Note that **SetIdleWait** is inherited from [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem).)
4.  Define the [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger) structure and call [**CreateTrigger**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-createtrigger) to create the idle trigger. (Note that **CreateTrigger** is inherited from [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem).)
5.  Save the task with the new idle trigger to disk using [**IPersistFile::Save**](https://msdn.microsoft.com/library/ms693701(v=VS.85).aspx). (The [**IPersistFile**](https://msdn.microsoft.com/library/ms687223(v=VS.85).aspx) interface is a standard COM interface supported by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.)
6.  Call **ITask::Release** to release all resources. (Note that [**Release**](https://msdn.microsoft.com/library/ms682317(v=VS.85).aspx) is an [**IUnknown**](https://msdn.microsoft.com/library/ms680509(v=VS.85).aspx) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)



| For a code example of                         | See                                                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------|
| Creating an idle trigger for an existing task | [C/C++ Code Example: Creating an Idle Trigger](c-c-code-example-creating-an-idle-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




