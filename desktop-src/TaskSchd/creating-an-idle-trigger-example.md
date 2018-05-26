---
title: Creating an Idle Trigger Example
description: To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see Task Idle Conditions.
ms.assetid: d36a621c-4011-4c3d-b6f4-b56d1f50983c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating an Idle Trigger Example

To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

After creating the idle trigger, call [**IPersistFile::Save**](_com_ipersistfile_save) to save the new trigger to disk.

The following procedure describes how to create an idle trigger for a known task.

**To create an idle trigger for a known task**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/win32/Mstask/nf-mstask-itaskscheduler-activate?branch=master) to get the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**SetIdleWait**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-setidlewait?branch=master) to set how long the system must remain idle before the trigger will fire. (Note that **SetIdleWait** is inherited from [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master).)
4.  Define the [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master) structure and call [**CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) to create the idle trigger. (Note that **CreateTrigger** is inherited from [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master).)
5.  Save the task with the new idle trigger to disk using [**IPersistFile::Save**](_com_ipersistfile_save). (The [**IPersistFile**](_com_ipersistfile) interface is a standard COM interface supported by the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface.)
6.  Call **ITask::Release** to release all resources. (Note that [**Release**](_com_iunknown_release) is an [**IUnknown**](_com_iunknown) method inherited by [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master).)



| For a code example of                         | See                                                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------|
| Creating an idle trigger for an existing task | [C/C++ Code Example: Creating an Idle Trigger](c-c-code-example-creating-an-idle-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




